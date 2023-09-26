from datetime import datetime
import Experiment

if __name__ == "__main__":
    '''
    In this snippet the experiments are writen down into a specific txt document with the date.
    To prevent that the document is overwriten and to log the experiments if the document can´t be created the document 
    Experiment-logs.txt was created where each run is loged under each other.
    The documents can be found in the folder Experiments/Experiment-Logs    
    '''
    try:
        Time = datetime.now()
        textfile_name = 'Experiment-Logs/ExperimentRunLogs_' + Time.strftime("%Y.%m.%d_%H.%M") + '.txt'
        textfile = open(textfile_name, 'x')
        begin = "============ExperimentRun-" + Time.strftime("%d.%m.%Y_%H:%M:%S") + "-============"
        textfile.write("\n")
        textfile.write(begin)
        print("============New Experiment Run was creaeted: " + Time.strftime("%d.%m.%Y_%H:%M:%S") + " ============")
    except:
        print ("Textdokument could not be createt your logs will be in Experiment-logs and should be manully copyed")
        textfile_name = "Experiment-logs.txt"
    finally:
        textfile = open('Experiment-Logs/Experiment-logs.txt', 'a')

    try:
        experiment_quantity = 5
        # experiment_quantity           --> Number of different Experiment in a Experiment Run current max:70.
        # Standard Value is Start Value +1
        Experiment_run_number = 10
        # Experiment_run_number         --> Start Value for the Experiment standard is 0
        while Experiment_run_number < experiment_quantity:
            preprocessor_data_path = 'data/DeepCASE/hdfs_test_normal_DeepCASE'  #later preprocessor_data_path_original
            # preprocessor_data_path        --> path to the experiment data,
            # in paper this was data/DeepLog/hdfs_test_normal_DeepCASE
            preprocessor_length = 10
            # preprocessor_length,          --> Number of events in context, in paper this was 10
            context_builder_input_size = 30
            # context_builder_input_size,   --> Number of input features to expect, in paper this was 30
            context_builder_features = 300
            # context_builder_features,   --> Number of input features to expect, in paper it was set to 300
            context_builder_hidden_size = 128
            # context_builder_hidden_size,  --> Number of nodes in hidden layer, in paper this was 128
            context_builder_epochs = 100
            # context_builder_epochs,       --> Number of epochs to train with, in paper this was 100
            context_builder_batch_size = 128
            # context_builder_batch_size,   --> Number of samples in each training batch, in paper this was 128
            context_builder_learning_rate = 0.01
            # context_builder_learning_rate --> Learning rate to train with, in paper this was 0.01
            interpreter_eps = 0.1
            # interpreter_eps --> # Epsilon value to use for DBSCAN clustering, in paper this was 0.1
            interpreter_min_samples= 5
            # interpreter_min_samples --> Minimum number of samples to use for DBSCAN clustering, in paper this was 5
            interpreter_threshold = 0.2
            # interpreter_threshold --> Confidence threshold used for determining if attention from the ContextBuilder can be used, in paper this was 0.2
            interpreter_iterations = 100
            # interpreter_iterations --> Number of iterations to use for attention query, in paper this was 100
            interpreter_query_batch_size = 1024
            # interpreter_query_batch_size --> Batch size to use for attention query, used to limit CUDA memory usage, in paper this was 1024
            Time = datetime.now()
            print(str(Experiment_run_number) + " - Experiment in Experiment Run -" + Time.strftime("%H:%M:%S"))
            textfile = open(textfile_name, 'a')
            # -------------------------------------preprocessor_data_path = 'data/DeepCASE/hdfs_test_normal_DeepCASE'---------------------------------------------------------------------
            if Experiment_run_number == 0:
                print("++++++++++++++++++++++++ExperimentRun-preprocessor_data_path++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-preprocessor_data_path++++++++++++++++++++++++")
                preprocessor_data_path = 'data/Proccessed_data/firefox.txt_transformt.csv'
            elif Experiment_run_number == 1:
                preprocessor_data_path = 'data/Proccessed_data/firefox.txt_templates.csv'
            elif Experiment_run_number == 2:
                preprocessor_data_path = 'data/Proccessed_data/security_events.txt_templates.csv'
            elif Experiment_run_number == 3:
                preprocessor_data_path = 'data/Proccessed_data/security_events.txt_structured.csv'
            elif Experiment_run_number == 4:
                preprocessor_data_path = 'data/Proccessed_data/HDFS_2k.log_structured.csv'
                # ----------------------------------- preprocessor_length = 10-----------------------------------------------------------------------
            elif Experiment_run_number == 5:
                print("++++++++++++++++++++++++ExperimentRun-preprocessor_length++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-preprocessor_length++++++++++++++++++++++++")
                preprocessor_length = 50

            elif Experiment_run_number == 6:
                preprocessor_length = 52

            elif Experiment_run_number == 7:
                preprocessor_length = 55

            elif Experiment_run_number == 8:
                preprocessor_length = 57

            elif Experiment_run_number == 9:
                preprocessor_length = 1000
                # ------------------------------context_builder_input_size = 100----------------------------------------------------------------------------
            elif Experiment_run_number == 10:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_input_size++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-context_builder_input_size++++++++++++++++++++++++")
                context_builder_input_size = 10

            elif Experiment_run_number == 11:
                context_builder_input_size = 50

            elif Experiment_run_number == 12:
                context_builder_input_size = 55

            elif Experiment_run_number == 13:
                context_builder_input_size = 60

            elif Experiment_run_number == 14:
                context_builder_input_size = 100
                # ----------------------context_builder_hidden_size = 30------------------------------------------------------------------------------------
            elif Experiment_run_number == 15:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_hidden_size++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-context_builder_hidden_size++++++++++++++++++++++++")
                context_builder_hidden_size = 256

            elif Experiment_run_number == 16:
                context_builder_hidden_size = 260

            elif Experiment_run_number == 17:
                context_builder_hidden_size = 265

            elif Experiment_run_number == 18:
                context_builder_hidden_size = 270

            elif Experiment_run_number == 19:
                context_builder_hidden_size = 275
                # ----------------------------------------context_builder_epochs = 100------------------------------------------------------------------
            elif Experiment_run_number == 20:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_epochs++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-context_builder_epochs++++++++++++++++++++++++")
                context_builder_epochs = 100

            elif Experiment_run_number == 21:
                context_builder_epochs = 250

            elif Experiment_run_number == 22:
                context_builder_epochs = 255

            elif Experiment_run_number == 23:
                context_builder_epochs = 260

            elif Experiment_run_number == 24:
                context_builder_epochs = 500
                # --------------------------------------context_builder_batch_size = 128--------------------------------------------------------------------
            elif Experiment_run_number == 25:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_batch_size++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-context_builder_batch_size++++++++++++++++++++++++")
                context_builder_batch_size = 128

            elif Experiment_run_number == 26:
                context_builder_batch_size = 130

            elif Experiment_run_number == 27:
                context_builder_batch_size = 135

            elif Experiment_run_number == 28:
                context_builder_batch_size = 140

            elif Experiment_run_number == 29:
                context_builder_batch_size = 120
                # --------------------------------------------context_builder_learning_rate = 0.01--------------------------------------------------------------
            elif Experiment_run_number == 30:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_learning_rate++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-context_builder_learning_rate++++++++++++++++++++++++")
                context_builder_learning_rate = 0.008

            elif Experiment_run_number == 31:
                context_builder_learning_rate = 0.009

            elif Experiment_run_number == 32:
                context_builder_learning_rate = 0.01

            elif Experiment_run_number == 33:
                context_builder_learning_rate = 0.012

            elif Experiment_run_number == 34:
                context_builder_learning_rate = 0.015
                # --------------------------------------------Multi-hdfs--------------------------------------------------------------
            elif Experiment_run_number == 35:
                print("++++++++++++++++++++++++ExperimentRun-Multi-hdfs++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-Multi-hdfs++++++++++++++++++++++++")
                preprocessor_length = 50
                context_builder_input_size = 50
                context_builder_hidden_size = 256
                context_builder_epochs = 250
                context_builder_batch_size = 128
                context_builder_learning_rate = 0.01

            elif Experiment_run_number == 36:
                preprocessor_length = 50
                context_builder_input_size = 50

            elif Experiment_run_number == 37:
                context_builder_input_size = 50
                context_builder_hidden_size = 256
                context_builder_batch_size = 128

            elif Experiment_run_number == 38:
                preprocessor_length = 50
                context_builder_batch_size = 128
                context_builder_learning_rate = 0.01

            elif Experiment_run_number == 39:
                context_builder_epochs = 250
                context_builder_learning_rate = 0.05
                # --------------------------------------------interpreter_eps = 0.1--------------------------------------------------------------
            elif Experiment_run_number == 40:
                print("++++++++++++++++++++++++ExperimentRun-interpreter_eps++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-interpreter_eps++++++++++++++++++++++++")
                interpreter_eps = 0.01
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 41:
                interpreter_eps = 0.05
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 42:
                interpreter_eps = 0.1
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 43:
                interpreter_eps = 0.5
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 44:
                interpreter_eps = 1
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
                # --------------------------------------------interpreter_min_samples= 5--------------------------------------------------------------
            elif Experiment_run_number == 45:
                print("++++++++++++++++++++++++ExperimentRun-interpreter_min_samples++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-interpreter_min_samples++++++++++++++++++++++++")
                interpreter_min_samples = 1
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 46:
                interpreter_min_samples = 3
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 47:
                interpreter_min_samples = 5
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 48:
                interpreter_min_samples = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 49:
                interpreter_min_samples = 15
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
                # --------------------------------------------interpreter_threshold = 0.2--------------------------------------------------------------
            elif Experiment_run_number == 50:
                print("++++++++++++++++++++++++ExperimentRun-interpreter_threshold++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-interpreter_threshold++++++++++++++++++++++++")
                interpreter_threshold = 0.01
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 51:
                interpreter_threshold = 0.1
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 52:
                interpreter_threshold = 0.2
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 53:
                interpreter_threshold = 0.5
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 54:
                interpreter_threshold = 1
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
                # --------------------------------------------interpreter_iterations = 100--------------------------------------------------------------
            elif Experiment_run_number == 55:
                print("++++++++++++++++++++++++ExperimentRun-interpreter_iterations++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-interpreter_iterations++++++++++++++++++++++++")
                interpreter_iterations =  50
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 56:
                interpreter_iterations = 75
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 57:
                interpreter_iterations = 100
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 58:
                interpreter_iterations = 125
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 59:
                interpreter_iterations = 150
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
                # --------------------------------------------interpreter_query_batch_size = 1024--------------------------------------------------------------
            elif Experiment_run_number == 60:
                print("++++++++++++++++++++++++ExperimentRun-interpreter_query_batch_size++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-interpreter_query_batch_size++++++++++++++++++++++++")
                interpreter_query_batch_size = 256
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 61:
                interpreter_query_batch_size = 512
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 62:
                interpreter_query_batch_size = 1024
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 63:
                interpreter_query_batch_size = 2048
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 64:
                interpreter_query_batch_size = 4096
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
                # --------------------------------------------Multi--------------------------------------------------------------
            elif Experiment_run_number == 65:
                print("++++++++++++++++++++++++ExperimentRun-Multi++++++++++++++++++++++++")
                textfile.write("\n" + "++++++++++++++++++++++++ExperimentRun-Multi++++++++++++++++++++++++")
                interpreter_eps = 0.01
                interpreter_min_samples = 1
                interpreter_threshold = 0.01
                interpreter_iterations = 50
                interpreter_query_batch_size = 256
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 66:
                interpreter_eps = 0.05
                interpreter_min_samples = 3
                interpreter_threshold = 0.1
                interpreter_iterations = 75
                interpreter_query_batch_size = 512
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 67:
                interpreter_eps = 0.1
                interpreter_min_samples = 5
                interpreter_threshold = 0.2
                interpreter_iterations = 100
                interpreter_query_batch_size = 1024
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 68:
                interpreter_eps = 0.5
                interpreter_min_samples = 10
                interpreter_threshold = 0.5
                interpreter_iterations = 125
                interpreter_query_batch_size = 2048
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'

            elif Experiment_run_number == 69:
                interpreter_eps = 1
                interpreter_min_samples = 15
                interpreter_threshold = 1
                interpreter_iterations = 150
                interpreter_query_batch_size = 4096
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
            #-----------------------------------------------------------------------------------------------------------

            '''
            This snipied watches for the two destinced modes of DeepCASE
            The first is used for the prediction like in the "example hdfs"
            The second is for the main functionality needing a sutible data set.
            '''

            if preprocessor_data_path == 'data/DeepCASE/hdfs_test_normal_DeepCASE':
                try:
                    Experiment.experiment_hdfs_txt(textfile_name,
                                                    preprocessor_data_path,
                                                    preprocessor_length,
                                                    context_builder_input_size,
                                                    context_builder_hidden_size,
                                                    context_builder_epochs,
                                                    context_builder_batch_size,
                                                    context_builder_learning_rate,
                                                    Experiment_run_number)
                    Experiment_run_number = Experiment_run_number + 1
                except Exception:
                    print("Experiment Faild ")
                    Experiment_run_number = Experiment_run_number + 1
            else:
                try:
                    Experiment.experiment_module_csv(textfile_name,
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
                                                    interpreter_query_batch_size,
                                                    Experiment_run_number
                    )
                    Experiment_run_number = Experiment_run_number + 1
                except Exception:
                    print("Experiment Faild ")
                    Experiment_run_number = Experiment_run_number + 1
        # --------------------------------------------------------------------------------------------------------------
        '''
        If any runs can not be complete they will be shown as "Faild runs" while the other experiemnts are uneffected.   
        '''

    except:
        print(">>>>>>>>>>> ExperimentRun Faild <<<<<<<<<<<<<<<")
        textfile.write("\n" + "ExperimentRun Failed")
    finally:
        print("============ExperimentRun-END============")
        Time = datetime.now()
        end = "\n" + "============ExperimentRun-END-"+ Time.strftime("%d.%m.%Y_%H:%M:%S") +   "============"
        textfile.write(end)
# ----------------------------------------------------------------------------------------------------------------------