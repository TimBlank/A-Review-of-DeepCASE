import DeepCASE_Module_txt
from datetime import datetime
import Experiment
#import LogParser

if __name__ == "__main__":
    try:
        Time = datetime.now()
        textfile_name = 'Experiment-Logs/ExperimentRunLogs_' + Time.strftime("%d.%m.%Y_%H.%M") + '.txt'
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

# ----------------------------------------------------------------------------------------------------------------------
    preprocessor_data_path_original = 'data/Proccessed_data/security_events.txt_structured.csv'
    #input_dir
    #output_dir
    #log_file
    #log_format
    #LogParser.extractLog(input_dir,output_dir,log_file,log_format)
    #preprocessor_data_path = preprocessor_data_path_original
# ----------------------------------------------------------------------------------------------------------------------
    try:
        experiment_quantity = 40
        # experiment_quantity           --> Number of different Experiment in a Experiment Run
        i = 34
        # i                             --> Start Value for the Experiment standard is 0
        while i < experiment_quantity:
            preprocessor_data_path = 'data/DeepCASE/hdfs_test_normal_DeepCASE'  #later preprocessor_data_path_original
            # preprocessor_data_path        --> path to the experiment data,
            # in paper this was data/DeepLog/hdfs_test_normal_DeepCASE
            preprocessor_length = 10
            # preprocessor_length,          --> Number of events in context, in paper this was 10
            context_builder_input_size = 100
            # context_builder_input_size,   --> Number of input features to expect, in paper this was 30
            context_builder_hidden_size = 30
            # context_builder_hidden_size,  --> Number of nodes in hidden layer, in paper this was 128
            context_builder_epochs = 100
            # context_builder_epochs,       --> Number of epochs to train with, in paper this was 100
            context_builder_batch_size = 128
            # context_builder_batch_size,   --> Number of samples in each training batch, in paper this was 128
            context_builder_learning_rate = 0.01
            # context_builder_learning_rate --> Learning rate to train with, in paper this was 0.01

            print(str(i) + " - Experiment in Experiment Run -" + Time.strftime("%H:%M:%S"))
            # -------------------------------------preprocessor_data_path = 'data/DeepCASE/hdfs_test_normal_DeepCASE'---------------------------------------------------------------------
            if i == 0:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/Proccessed_data/HDFS_2k.log_templates.csv'
            elif i == 1:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/Proccessed_data/HDFS_2k.log_structured.csv'
            elif i == 2:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_test_abnormal_DeepLog'
            elif i == 3:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
            elif i == 4:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_train_DeepLog'
                # ----------------------------------- preprocessor_length = 10-----------------------------------------------------------------------
            elif i == 5:
                print("++++++++++++++++++++++++ExperimentRun-preprocessor_length++++++++++++++++++++++++")
                context_builder_epochs = 10
                preprocessor_length = 1
            elif i == 6:
                context_builder_epochs = 10
                preprocessor_length = 5
            elif i == 7:
                context_builder_epochs = 10
                preprocessor_length = 50
            elif i == 8:
                context_builder_epochs = 10
                preprocessor_length = 100
            elif i == 9:
                context_builder_epochs = 10
                preprocessor_length = 1000
                # ------------------------------context_builder_input_size = 100----------------------------------------------------------------------------
            elif i == 10:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_input_size++++++++++++++++++++++++")
                context_builder_epochs = 10
                context_builder_input_size = 10
            elif i == 11:
                context_builder_epochs = 10
                context_builder_input_size = 50
            elif i == 12:
                context_builder_epochs = 10
                context_builder_input_size = 150
            elif i == 13:
                context_builder_epochs = 10
                context_builder_input_size = 200
            elif i == 14:
                context_builder_epochs = 10
                context_builder_input_size = 500
                # ----------------------context_builder_hidden_size = 30------------------------------------------------------------------------------------
            elif i == 15:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_hidden_size++++++++++++++++++++++++")
                context_builder_epochs = 10
                context_builder_hidden_size = 3
            elif i == 16:
                context_builder_epochs = 10
                context_builder_hidden_size = 10
            elif i == 17:
                context_builder_epochs = 10
                context_builder_hidden_size = 20
            elif i == 18:
                context_builder_epochs = 10
                context_builder_hidden_size = 50
            elif i == 19:
                context_builder_epochs = 10
                context_builder_hidden_size = 100
                # ----------------------------------------context_builder_epochs = 100------------------------------------------------------------------
            elif i == 20:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_epochs++++++++++++++++++++++++")
                context_builder_epochs = 1
            elif i == 21:
                context_builder_epochs = 50
            elif i == 22:
                context_builder_epochs = 150
            elif i == 23:
                context_builder_epochs = 250
            elif i == 24:
                context_builder_epochs = 500
                # --------------------------------------context_builder_batch_size = 128--------------------------------------------------------------------
            elif i == 25:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_batch_size++++++++++++++++++++++++")
                context_builder_epochs = 10
                context_builder_batch_size = 1
            elif i == 26:
                context_builder_epochs = 10
                context_builder_batch_size = 64
            elif i == 27:
                context_builder_epochs = 10
                context_builder_batch_size = 100
            elif i == 28:
                context_builder_epochs = 10
                context_builder_batch_size = 150
            elif i == 29:
                context_builder_epochs = 10
                context_builder_batch_size = 200
                # --------------------------------------------context_builder_learning_rate = 0.01--------------------------------------------------------------
            elif i == 30:
                print("++++++++++++++++++++++++ExperimentRun-context_builder_learning_rate++++++++++++++++++++++++")
                context_builder_epochs = 10
                context_builder_learning_rate = 0.0001
            elif i == 31:
                context_builder_epochs = 10
                context_builder_learning_rate = 0.1
            elif i == 32:
                context_builder_epochs = 10
                context_builder_learning_rate = 1
            elif i == 33:
                context_builder_epochs = 10
                context_builder_learning_rate = 10
            elif i == 34:
                context_builder_epochs = 10
                context_builder_learning_rate = 100
                # --------------------------------------------Multi--------------------------------------------------------------
            elif i == 35:
                print("++++++++++++++++++++++++ExperimentRun-Multi++++++++++++++++++++++++")
                preprocessor_length = 1
                context_builder_input_size = 10
                context_builder_hidden_size = 3
                context_builder_epochs = 1
                context_builder_batch_size = 1
                context_builder_learning_rate = 0.0001
            elif i == 36:
                preprocessor_length = 1
                context_builder_input_size = 50
                context_builder_hidden_size = 10
                context_builder_epochs = 50
                context_builder_batch_size = 64
                context_builder_learning_rate = 0.1
            elif i == 37:
                preprocessor_length = 1
                context_builder_input_size = 150
                context_builder_hidden_size = 20
                context_builder_epochs = 150
                context_builder_batch_size = 100
                context_builder_learning_rate = 1
            elif i == 38:
                preprocessor_length = 1
                context_builder_input_size = 200
                context_builder_hidden_size = 50
                context_builder_epochs = 250
                context_builder_batch_size = 150
                context_builder_learning_rate = 10
            elif i == 39:
                preprocessor_length = 1
                context_builder_input_size = 500
                context_builder_hidden_size = 250
                context_builder_epochs = 500
                context_builder_batch_size = 200
                context_builder_learning_rate = 100
            #-----------------------------------------------------------------------------------------------------------
            try:
                Experiment.experiment(
                    textfile_name,
                    preprocessor_data_path,
                    preprocessor_length,
                    context_builder_input_size,
                    context_builder_hidden_size,
                    context_builder_epochs,
                    context_builder_batch_size,
                    context_builder_learning_rate,
                    i)
                i = i+1
            except Exception:
                print("Experiment Faild ")
                i = i + 1
        # --------------------------------------------------------------------------------------------------------------
    except:
        print(">>>>>>>>>>> ExperimentRun Faild <<<<<<<<<<<<<<<")
        textfile.write("\n" + "ExperimentRun Failed")
    finally:
        print("============ExperimentRun-END============")
        end = "\n" + "============ExperimentRun-END-"+ Time.strftime("%d.%m.%Y_%H:%M:%S") +   "============"
        textfile.write(end)
# ----------------------------------------------------------------------------------------------------------------------