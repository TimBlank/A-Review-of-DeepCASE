# Other imports
from sklearn.metrics import classification_report
import numpy as np
import torch

# DeepCASE Imports
from deepCASE.deepcase_programm.preprocessing   import Preprocessor
from deepCASE.deepcase_programm.context_builder import ContextBuilder
from deepCASE.deepcase_programm                 import DeepCASE
def experiment_hdfs(preprocessor_data_path,preprocessor_length,context_builder_input_size,context_builder_features,context_builder_hidden_size,context_builder_epochs,context_builder_batch_size,context_builder_learning_rate):
    #if __name__ == "__main__":
        ########################################################################
        #                             Loading data                             #
        ########################################################################

        # Create preprocessor
        preprocessor = Preprocessor(
            length  = preprocessor_length,      # 10 events in context
            timeout = 86400,                    # Ignore events older than 1 day (60*60*24 = 86400 seconds)
        )

        # Load data from file
        context, events, labels, mapping = preprocessor.csv(
            path    = preprocessor_data_path,
            verbose = True,
        )

        # In case no labels are provided, set labels to -1
        # IMPORTANT: If no labels are provided, make sure to manually set the labels
        # before calling the interpreter.score_clusters method. Otherwise, this will
        # raise an exception, because scores == NO_SCORE cannot be computed.
        if labels is None:
            labels = np.full(events.shape[0], -1, dtype=int)

        # Cast to cuda if available
        if torch.cuda.is_available():
            events  = events .to('cuda')
            context = context.to('cuda')

        ########################################################################
        #                            Splitting data                            #
        ########################################################################

        # Split into train and test sets (20:80) by time - assuming events are ordered chronologically
        events_train  = events [:events.shape[0]//5 ]
        events_test   = events [ events.shape[0]//5:]

        context_train = context[:events.shape[0]//5 ]
        context_test  = context[ events.shape[0]//5:]

        labels_train  = labels [:events.shape[0]//5 ]
        labels_test   = labels [ events.shape[0]//5:]

        ########################################################################
        #                       Training ContextBuilder                        #
        ########################################################################

        # Create ContextBuilder
        context_builder = ContextBuilder(
            input_size    = context_builder_input_size,   # Number of input features to expect, in paper we set this to 10
            output_size   = context_builder_input_size,   # Same as input size
            hidden_size   = context_builder_hidden_size,   # Number of nodes in hidden layer, in paper we set this to 128
            max_length    = preprocessor_length,    # Length of the context, should be same as context in Preprocessor
        )

        # Cast to cuda if available
        if torch.cuda.is_available():
            context_builder = context_builder.to('cuda')

        # Train the ContextBuilder
        context_builder.fit(
            X             = context_train,                  # Context to train with
            y             = events_train.reshape(-1, 1),    # Events to train with, note that these should be of shape=(n_events, 1)
            epochs        = context_builder_epochs,         # Number of epochs to train with, in paper we set this to 100
            batch_size    = context_builder_batch_size,     # Number of samples in each training batch, in paper this was 128
            learning_rate = context_builder_learning_rate,  # Learning rate to train with, in paper this was 0.01
            verbose       = True,                           # If True, prints progress
        )

        ########################################################################
        #                  Get prediction from ContextBuilder                  #
        ########################################################################

        # Use context builder to predict confidence
        confidence, _ = context_builder.predict(
            X = context_test
        )

        # Get confidence of the next step, seq_len 0 (n_samples, seq_len, output_size)
        confidence = confidence[:, 0]
        # Get confidence from log confidence
        confidence = confidence.exp()
        # Get prediction as maximum confidence
        y_pred = confidence.argmax(dim=1)

        ########################################################################
        #                          Perform evaluation                          #
        ########################################################################

        # Get test and prediction as numpy array
        y_test = events_test.cpu().numpy()
        y_pred = y_pred     .cpu().numpy()

        # Print classification report
        #print(classification_report(
        #    y_true = y_test,
        #    y_pred = y_pred,
        #    digits = 4,
        #))
        return  classification_report(
            y_true = y_test,
            y_pred = y_pred,
            digits = 4,
        )

#-----------------------------------------------------------------------------------------------------------------------
# Experiment Module for proccessed Data
#-----------------------------------------------------------------------------------------------------------------------
def experiment_module(
        preprocessor_data_path,
        preprocessor_length,
        context_builder_input_size,
        context_builder_features,
        context_builder_hidden_size,
        interpreter_eps,
        interpreter_min_samples,
        interpreter_threshold,
        context_builder_epochs,
        context_builder_batch_size,
        context_builder_learning_rate,
        interpreter_iterations,
        interpreter_query_batch_size
        ):
    #if __name__ == "__main__":
        ########################################################################
        #                             Loading data                             #
        ########################################################################

    preprocessor = Preprocessor(
        length=preprocessor_length,  # 10 events in context
        timeout=86400,  # Ignore events older than 1 day (60*60*24 = 86400 seconds)
    )

    # Load data from file
    context, events, labels, mapping = preprocessor.csv(
        path=preprocessor_data_path,
        verbose=True,
    )

    # In case no labels are provided, set labels to -1
    if labels is None:
        labels = np.full(events.shape[0], -1, dtype=int)

    # Cast to cuda if available
    if torch.cuda.is_available():
        events = events.to('cuda')
        context = context.to('cuda')

    ########################################################################
    #                            Splitting data                            #
    ########################################################################

    # Split into train and test sets (20:80) by time - assuming events are ordered chronologically
    events_train = events[:events.shape[0] // 5]
    events_test = events[events.shape[0] // 5:]

    context_train = context[:events.shape[0] // 5]
    context_test = context[events.shape[0] // 5:]

    labels_train = labels[:events.shape[0] // 5]
    labels_test = labels[events.shape[0] // 5:]

    ########################################################################
    #                            Using DeepCASE                            #
    ########################################################################

    deepcase = DeepCASE(
        # ContextBuilder parameters
        input_size=context_builder_input_size,  # Number of input features to expect, in paper we set this to 10
        features=context_builder_features,  # Number of input features to expect
        max_length=preprocessor_length,  # Length of the context, should be same as context in Preprocessor
        hidden_size=context_builder_hidden_size,  # Number of nodes in hidden layer, in paper we set this to 128

        # Interpreter parameters
        eps=interpreter_eps,  # Epsilon value to use for DBSCAN clustering, in paper this was 0.1
        min_samples=interpreter_min_samples,  # Minimum number of samples to use for DBSCAN clustering, in paper this was 5
        threshold=interpreter_threshold,
        # Confidence threshold used for determining if attention from the ContextBuilder can be used, in paper this was 0.2
    )

    # Cast to cuda if available
    if torch.cuda.is_available():
        deepcase = deepcase.to('cuda')

    ########################################################################
    #                             Fit DeepCASE                             #
    ########################################################################

    # Train the ContextBuilder
    # Conveniently, the fit and fit_predict methods have the same API, so if you
    # do not require the predicted values on the train dataset, simply
    # substitute fit_predict with fit and it will run slightly quicker because
    # DeepCASE skip the prediction over the training dataset and simply return
    # the deepcase_programm object itself. Other than that, both calls are exactly the
    # same.
    prediction_train = deepcase.fit_predict(
        # Input data
        X=context_train,  # Context to train with
        y=events_train.reshape(-1, 1),  # Events to train with, note that these should be of shape=(n_events, 1)
        scores=labels_train,
        # Labels used to compute score (either as loaded by Preprocessor, or put your own labels here)

        # ContextBuilder-specific parameters
        epochs=context_builder_epochs,  # Number of epochs to train with
        batch_size=context_builder_batch_size,  # Number of samples in each training batch, in paper this was 128
        learning_rate=context_builder_learning_rate,  # Learning rate to train with, in paper this was 0.01

        # Interpreter-specific parameters
        iterations=interpreter_iterations,  # Number of iterations to use for attention query, in paper this was 100
        query_batch_size=interpreter_query_batch_size,  # Batch size to use for attention query, used to limit CUDA memory usage, in paper this was 1024
        strategy="max",  # Strategy to use for scoring (one of "max", "min", "avg")
        NO_SCORE=-1,  # Any sequence with this score will be ignored in the strategy.
        # If assigned a cluster, the sequence will inherit the cluster score.
        # If the sequence is not present in a cluster, it will receive a score of NO_SCORE.

        # Verbosity level
        verbose=True,  # If True, prints progress
    )

    ########################################################################
    #                        Predict with DeepCASE                         #
    ########################################################################

    # Compute predicted scores
    prediction_test = deepcase.predict(
        X=context_test,  # Context to predict
        y=events_test.reshape(-1, 1),  # Events to predict, note that these should be of shape=(n_events, 1)
        iterations=interpreter_iterations,  # Number of iterations to use for attention query, in paper this was 100
        batch_size=interpreter_query_batch_size,  # Batch size to use for attention query, used to limit CUDA memory usage
        verbose=True,  # If True, prints progress
    )

    ########################################################################
    #                          Perform evaluation                          #
    ########################################################################

    # Get test and prediction as numpy array
    y_test = events_test.cpu().numpy()
    y_pred = prediction_test.cpu().numpy()

    return classification_report(
        y_true = y_test,
        y_pred = y_pred,
        digits = 4,
    )