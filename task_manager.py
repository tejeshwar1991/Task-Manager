import psutil #Python package to determine running tasks
import time


class CPU_Information(object):
    
    def __init__(self):
        print("Provides CPU Utilization Information")

    def cpu_utilization_percentage(self, interval_time):
        '''
        Provides CPU Utilization in terms of percentage. Returns float value. 
        Interval time has to be more than zero.
        ''' 

        if(interval_time > 0):
            cpu_utilization_percent = psutil.cpu_percent(interval = interval_time)
            print(psutil.cpu_percent(interval = interval_time))
            return cpu_utilization_percent
        else:
            print("Interval time has to be greater than Zero")

class processes_information(object):
    
    def __init__(self):
        print("Provides information related to currently running processes")

    def pids_list_of_running_processes(self):
        '''
        Provides Pids of currently running processes.
        arg: None
        ret value: returns a list
        '''

        #print(psutil.pids())
        return psutil.pids()

    #def list_processes(self):
    #    '''
    #    Prints all currently running processes with username, pid, and process name
    #    '''
        #for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
            #print(proc.info)
            #print("STOP")

class disk_info(object):
    
    def __init__(self, *args):
        super(disk_info, self).__init__(*args)
        print("Provides Disk Information")

    def disk_usage(self):
        return psutil.disk_usage('/')

        
if __name__  == "__main__" :
    cpuInfoObj = CPU_Information()

    currrent_cpu_usage = cpuInfoObj.cpu_utilization_percentage(1)
    print("currrent_cpu_usage:",currrent_cpu_usage)

    processesInfoObj = processes_information()
    #processesInfoObj.pids_list_of_running_processes()
    
    pid = []
    pid = processesInfoObj.pids_list_of_running_processes()
    

    #processesInfoObj.list_processes() #prints all processes with username, pid, and process name

    diskInfoObj = disk_info()

    diskUsageInfo = ()
    diskUsageInfo = diskInfoObj.disk_usage()
    print(diskUsageInfo)
