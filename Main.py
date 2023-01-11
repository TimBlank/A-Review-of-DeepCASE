import subprocess
import example_hdfs

textfile = open ('Experiment-logs.txt', 'a')
#example_hdfs.experiment_hdfs(
# preprocessor_length,          --> 10 events in context
# context_builder_input_size,   --> Number of input features to expect, in paper we set this to 30
# context_builder_hidden_size,  --> Number of nodes in hidden layer, in paper we set this to 128
# context_builder_epochs,       --> Number of epochs to train with, in paper we set this to 100
# context_builder_batch_size,   --> Number of samples in each training batch, in paper this was 128
# context_builder_learning_rate --> Learning rate to train with, in paper this was 0.01
preprocessor_length = 10
context_builder_input_size = 100
context_builder_hidden_size = 30
context_builder_epochs = 100
context_builder_batch_size = 128
context_builder_learning_rate = 0.01

i = 0
while i < 7:
    content = example_hdfs.experiment_hdfs(preprocessor_length, context_builder_input_size, context_builder_hidden_size, context_builder_epochs, context_builder_batch_size, context_builder_learning_rate)
    begin = "--------Experiment-Begin------"
    textfile.write("\n")
    textfile.write(begin)
    textfile.write("\n")
    textfile.writelines(content)
    textfile.write("\n")
    i += 1

#content = '\n'. join(content)
#print (content)
#cmd = 'example_hdfs.py'
#p = subprocess.Popen(cmd, shell=True)
#out, err = p.communicate()
#print(err)
#print(out)
#content = '\n'. join(content)
#textfile.writelines(p)
#textfile.write(content)