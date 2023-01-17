import experiment_hdfs
from datetime import datetime
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
    preprocessor_data_path_original = 'data/DeepCASE/hdfs_test_normal_DeepCASE'
    #input_dir
    #output_dir
    #log_file
    #log_format
    #LogParser.extractLog(input_dir,output_dir,log_file,log_format)
# ----------------------------------------------------------------------------------------------------------------------
    try:
        #print("New Experiment Run was started: " + Time.strftime("%d.%m.%Y_%H:%M:%S") + "-============")
        textfile = open(textfile_name, 'a')
        i = 1
        experiment_quantity = 1
        # experiment_quantity          --> Number of different Experiment in a Experiment Run

        # --------------------------------------------------------------------------------------------------------------

        while (i <= experiment_quantity):
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
            # ----------------------------------------------------------------------------------------------------------
            if i ==1:
                context_builder_epochs = 10
            elif i == 2:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_test_abnormal_DeepLog'
            elif i == 3:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_test_normal_DeepLog'
            elif i == 4:
                context_builder_epochs = 10
                preprocessor_data_path = 'data/DeepLog/hdfs_train_DeepLog'
            elif i == 5:
                #should Fail
                context_builder_epochs = 10
                preprocessor_length = 10
            elif i == 6:
                context_builder_epochs = 10
                context_builder_input_size = 10
            elif i == 7:
                context_builder_epochs = 10
                context_builder_hidden_size = 3
            elif i == 8:
                context_builder_epochs = 10
                context_builder_batch_size = 125
            elif i == 9:
                context_builder_epochs = 10
                context_builder_learning_rate = 0.1
            elif i == 10:
                context_builder_epochs = 10
            elif i == 11:
                preprocessor_length = 10
            elif i == 12:
                preprocessor_length = 10
            elif i == 13:
                preprocessor_length = 10
            elif i == 14:
                preprocessor_length = 10
            elif i == 15:
                preprocessor_length = 10
            elif i == 16:
                preprocessor_length = 10
            elif i == 17:
                preprocessor_length = 10
            elif i == 18:
                preprocessor_length = 10
            elif i == 19:
                preprocessor_length = 10
            elif i == 20:
                preprocessor_length = 10
            elif i == 21:
                preprocessor_length = 10
            elif i == 22:
                preprocessor_length = 10
            elif i == 23:
                preprocessor_length = 10
            elif i == 24:
                preprocessor_length = 10
            elif i == 25:
                preprocessor_length = 10
            elif i == 26:
                preprocessor_length = 10
            elif i == 27:
                preprocessor_length = 10
            elif i == 28:
                preprocessor_length = 10
            elif i == 29:
                preprocessor_length = 10
            elif i == 30:
                preprocessor_length = 10
            #-----------------------------------------------------------------------------------------------------------
            begin = "--------" +str(i) + " - Experiment in Experiment Run started-" + Time.strftime("%H:%M:%S") + "------"
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
                #10 mal ausführen und den Durchschnitt zurück geben und speichern
                content = experiment_hdfs.experiment_hdfs(preprocessor_data_path,
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
            i += 1
        # --------------------------------------------------------------------------------------------------------------
    except:
        print(">>>>>>>>>>> ExperimentRun Faild <<<<<<<<<<<<<<<")
        textfile.write("\n" + "ExperimentRun Failed")
    finally:
        print("============ExperimentRun-END============")
        end = "\n" + "============ExperimentRun-END-"+ Time.strftime("%d.%m.%Y_%H:%M:%S") +   "============"
        textfile.write(end)
# ----------------------------------------------------------------------------------------------------------------------

#content = '\n'. join(content)
#print (content)
#cmd = 'experiment_hdfs.py'
#p = subprocess.Popen(cmd, shell=True)
#out, err = p.communicate()
#print(err)
#print(out)
#content = '\n'. join(content)
#textfile.writelines(p)
#textfile.write(content)