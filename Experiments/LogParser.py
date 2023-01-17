#!/usr/bin/env python
import re
from datetime import datetime

"""
    Variables   
        log_format=     time+  machine +Event
    1 : Reading the file
    2 : Extract Time / ip adresses and Event
    3 : save the outpute into csv file
    4 : Run Experiments with the outpute
"""

if __name__ == "__main__":
    Time = datetime.now()
    time = Time.strftime("%d.%m.%Y_%H:%M:%S")
    input_dir = 'data/ATLAS/M1/h1/'  # The input directory of log file
    output_dir = 'data/Proccessed_data/'                                        # The output directory of parsing results
    log_file = 'firefox.txt'                                            # The input log file name
    log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'   # HDFS log format

    ipaddress_pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    Time_pattern = r"("
    log_list = []

    # ----------------------------------------------------------------------------------------------------------------------
    try:
        textfile = open(output_dir + log_file, 'x')
    except FileExistsError:
        print ("FileExistsError: A File withe the same name was already inside Experiements/data/Proccessed_data and will now be over written")
    finally:
        logfile = open(input_dir + log_file, "r")

    # ----------------------------------------------------------------------------------------------------------------------
    for log in logfile:
        #print(log)
        ip_add = re.search(ipaddress_pattern, log)
        if re.search(ipaddress_pattern, log) != None:
            print (ip_add.group())
            log_list.append(ip_add.group())
        log_list.append(log.split('UTC')[0])
    print (log_list)

    # ----------------------------------------------------------------------------------------------------------------------
    textfile = open(output_dir + log_file, 'w')
    content = '\n'.join(log_list)
    textfile.writelines(content)


