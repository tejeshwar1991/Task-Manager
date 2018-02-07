from tkinter import Tk, Label, Button, Toplevel, Message, Menu
from textwrap import fill
from tkinter.constants import BOTH

from processes_info import cpu_information

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.label = Label(master, text="Click on the below buttons to view respective information")
        self.label.pack()
        self.label.place(x=100,y=0)
        
        '''
        # Create a drop down Menu containing Author Info, Module Info, Version Info
        self.menubar = Menu(master)
        master.config(self.menubar)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.author)
        self.filemenu.add_command(label="Save", command=self.author)
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        '''        
        
        self.greet_button = Button(master, text="Greet", command=self.menu_info)
        self.greet_button.pack()
        self.greet_button.place(x=0,y=40)

        self.process_button = Button(master, text="Network Process", command=self.nw_process)
        self.process_button.pack()
        self.process_button.place(x=70,y=40)

        self.cpu_info_button = Button(master, text="CPU Information", command=self.cpu_information)
        self.cpu_info_button.pack()
        self.cpu_info_button.place(x=225,y=40)
        
        self.memory_info_button = Button(master, text="Memory Information", command=self.memory_info)
        self.memory_info_button.pack()
        self.memory_info_button.place(x=370,y=40)
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        self.close_button.place(x=250,y=300)

    def menu_info(self):
        '''
        # Create a drop down Menu containing Author Info, Module Info, Version Info
        self.menubar = Menu(self.master)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.author)
        self.filemenu.add_command(label="Save", command=self.author)
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        '''
        print("Greetings!")
        
    def author(self):
        print("Tejeshwar Chandra Kamaal")
        
    def nw_process(self):
        print("Network")

    def cpu_information(self):
        cpu_info = cpu_information()
        usage_info = cpu_info.cpu_usage_in_percentage(1)
        
        # Container widget displayed as a separate window
        self.top = Toplevel()
        self.top.title("CPU Utilization")
        
        self.msg = Message(self.top,text=usage_info)
        self.msg.pack()
        
        self.dismiss_button = Button(self.top, text="Dismiss", command=self.top.destroy)
        self.dismiss_button.pack()
        
        #print("CPU Information")    
        
    def memory_info(self):
        print("Memory Information")
        
root = Tk()
root.geometry("600x500")
my_gui = MyFirstGUI(root)
root.mainloop()