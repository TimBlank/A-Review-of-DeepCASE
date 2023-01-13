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
    input_dir = 'data/raw-data/LogParser/HDFS/'  # The input directory of log file
    output_dir = 'data/'                                        # The output directory of parsing results
    log_file = 'HDFS_2k.log'                                            # The input log file name
    log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'   # HDFS log format



    ipaddress_pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    ip_address_list =[]
    logfile = open(input_dir + log_file, "r")
    for log in logfile:
        print(log)
        ip_add = re.search(ipaddress_pattern, log)
        if re.search(ipaddress_pattern, log) != None:
            print (ip_add.group())
            ip_address_list.append(ip_add.group())
    print (ip_address_list)