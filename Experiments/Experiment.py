import subprocess
import experiment_hdfs
from datetime import datetime

if __name__ == "__main__":
    try:
        Time = datetime.now()
        textfile_name = 'Logs/ExperimentRunLogs_' + Time.strftime("%d.%m.%Y_%I.%M") + '.txt'
        textfile = open(textfile_name, 'x')
        begin = "============ExperimentRun-" + Time.strftime("%d.%m.%Y_%I.%M") + "-============"
        textfile.write("\n")
        textfile.write(begin)
        print("============New Experiment Run was creaeted: " + Time.strftime("%d.%m.%Y_%I.%M") + " ============")
    except:
        print ("Textdokument could not be createt your logs will be in Experiment-logs and should be manully copyed")
        textfile_name = "Experiment-logs.txt"
    finally:
        textfile = open('Logs/Experiment-logs.txt', 'a')

# -----------------------------------------------------------------------------------------------------------------------
    try:
        #print("New Experiment Run was started: " + Time.strftime("%d.%m.%Y_%I.%M") + " ============")
        textfile = open(textfile_name, 'a')
        i = 1
        experiment_quantity = 1                       # experiment_quantity          --> Number of different Experiment in a Experiment Run

        while (i <= experiment_quantity):
            preprocessor_data_path = 'data/hdfs/hdfs_test_normal'  #--> path to the experiment data, in paper this was data/hdfs/hdfs_test_normal
            preprocessor_length = 10                                # preprocessor_length,          --> Number of events in context, in paper this was 10
            context_builder_input_size = 100                        # context_builder_input_size,   --> Number of input features to expect, in paper this was 30
            context_builder_hidden_size = 30                        # context_builder_hidden_size,  --> Number of nodes in hidden layer, in paper this was 128
            context_builder_epochs = 100                            # context_builder_epochs,       --> Number of epochs to train with, in paper this was 100
            context_builder_batch_size = 128                        # context_builder_batch_size,   --> Number of samples in each training batch, in paper this was 128
            context_builder_learning_rate = 0.01                    # context_builder_learning_rate --> Learning rate to train with, in paper this was 0.01
            print(str(i) + " - Experiment in Experiment Run")

        # -----------------------------------------------------------------------------------------------------------------------
            if i ==1:
                context_builder_epochs = 1
            elif i == 2:
                context_builder_epochs = 2
            elif i == 3:
                context_builder_epochs = 1
            elif i == 4:
                context_builder_epochs = 1
            elif i == 5:
                context_builder_epochs = 1
            elif i == 6:
                preprocessor_length = 10
            elif i == 7:
                preprocessor_length = 10
            elif i == 8:
                preprocessor_length = 10
            elif i == 9:
                preprocessor_length = 10
            elif i == 10:
                preprocessor_length = 10
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

        #-----------------------------------------------------------------------------------------------------------------------

            content = experiment_hdfs.experiment_hdfs(preprocessor_data_path,preprocessor_length, context_builder_input_size, context_builder_hidden_size, context_builder_epochs, context_builder_batch_size, context_builder_learning_rate)
            begin = "--------" +str(i) + " - Experiment in Experiment Run" + "------"
            textfile.write("\n")
            textfile.write(begin)
            textfile.write("\n")
            textfile.writelines(content)
            textfile.write("\n")
            i += 1
        end = "============ExperimentRun-END" + "============"
        textfile.write(end)
    except:
        print("Experiments Faild")
    finally:
        print("============ExperimentRun-END============")


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