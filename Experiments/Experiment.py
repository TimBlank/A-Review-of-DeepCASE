import DeepCASE_Module_txt
from datetime import datetime
from DeepCASE_Module_txt import experiment_hdfs
#from DeepCASE_Module_csv import experiment_hdfs
#import LogParser

def experiment(
               textfile_name,
               preprocessor_data_path,
               preprocessor_length,
               context_builder_input_size,
               context_builder_hidden_size,
               context_builder_epochs,
               context_builder_batch_size,
               context_builder_learning_rate,
               nummer):
        Time = datetime.now()
        # preprocessor_data_path        --> path to the experiment data,
        # in paper this was data/DeepLog/hdfs_test_normal_DeepCASE
        # preprocessor_length,          --> Number of events in context, in paper this was 10
        # context_builder_input_size,   --> Number of input features to expect, in paper this was 30
        # context_builder_hidden_size,  --> Number of nodes in hidden layer, in paper this was 128
        # context_builder_epochs,       --> Number of epochs to train with, in paper this was 100
        # context_builder_batch_size,   --> Number of samples in each training batch, in paper this was 128
        # context_builder_learning_rate --> Learning rate to train with, in paper this was 0.01

        textfile = open(textfile_name, 'a')
        begin = "--------" +str(nummer) + " - Experiment in Experiment Run started-" + Time.strftime("%H:%M:%S") + "------"
        textfile.write("\n")
        textfile.write(begin)
        textfile.write("\n")
        parameters = ("preprocessor_data_path = " + str(preprocessor_data_path),
                      "preprocessor_length = " + str(preprocessor_length),
                      "context_builder_input_size = " + str(context_builder_input_size),
                      "context_builder_hidden_size = " + str(context_builder_hidden_size),
                      "context_builder_epoch = " + str(context_builder_epochs),
                      "context_builder_batch_size = " + str(context_builder_batch_size),
                      "context_builder_learning_rate = " + str(context_builder_learning_rate))
        parameters = '\n'. join(parameters)
        textfile.writelines(parameters)
        textfile.write("\n")
        try:
            for g in range (1):
                #10 mal ausführen und den Durchschnitt zurück geben und speichern
                content = DeepCASE_Module_txt.experiment_hdfs(preprocessor_data_path,
                                                          preprocessor_length,
                                                          context_builder_input_size,
                                                          context_builder_hidden_size,
                                                          context_builder_epochs,
                                                          context_builder_batch_size,
                                                          context_builder_learning_rate)
            textfile.writelines(content)
            textfile.write("\n")
        except:
            print(">>>>>>>>>>> Experiment Faild <<<<<<<<<<<<<<<")
            textfile.write("\n" + "----------->ExperimentRun Failed<-----------")
        finally:
            print("------------Experiment END------------")
