#! /usr/bin/env python

import time
import os
import logging
import psutil

class test(object):
    
    log_count = 0
    file = 0
    file_path = 0
    
    def __init__(self):
        self.log_count = 0
        self.file = 0
        self.file_path = 0
        
    def printCurrentTime(self):
        print("Current Time : ",time.localtime())
        
    def printHelloWorld(self):
        print("Hello World")
     
    def createFile(self, filename):
        print("file name : ", filename)
        
        modify_filePath, file = os.path.split(self.file_path)
        print("Modified file Path : ", modify_filePath)
        print("file : ", file)
        #file_handler = open(os.path.abspath(modify_filePath),"w")
        
        #file_obj = open("self.file_path\filename","w")
        #print(" ", file_obj)
        
    def logTime(self):
        test.file.write("time")
        
    def findDirPath(self):
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        print("Dir Path: ",self.file_path)
         


class cpu_information(object):
    
    def __init__(self):
        print("Provides Information regarding CPU Usage!")
        
    def cpu_usage_in_percentage(self, interval_time):
        '''
         Provide CPU Utilization in terms of percentage.
         arg : interval_time has to be more than 0.
         return type : float (CPU Utilization)
        '''
        
        if (interval_time > 0):
            cpu_usage = psutil.cpu_percent(interval = interval_time, percpu = False)
            cpu_usage = (int) (cpu_usage)            
            print("CPU usage in terms of percentage:",cpu_usage,"%")
            return cpu_usage
        else:
            print("Interval time provided is invalid!!!")
            
    def pids_of_running_tasks(self):
        '''
        Provides a list of pids of currently running tasks. 
        return type : list (List of pids)
        '''
        pids_list = psutil.pids()
        return pids_list
            
        
if __name__ == "__main__":
    createNewObj = test();
    createNewObj.printCurrentTime()
    createNewObj.printHelloWorld()
    createNewObj.findDirPath()
    test_file = "hello"
    createNewObj.createFile(test_file)
    
    cpuInfoObj = cpu_information()
    retCpuUsage = cpuInfoObj.cpu_usage_in_percentage(1)
    print("CPU Usage : ", retCpuUsage)
    
    pidslist = cpuInfoObj.pids_of_running_tasks()
    
    
    