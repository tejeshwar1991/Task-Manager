############ GUI ##############
from tkinter import *   # Import everything from tkinter. 


# Inheriting Frame class from tkinter module
class Window(Frame):
    def init(self,master=None):
        Frame.__init__(self, master)
        self.master = master # This is the master widget
        self.init_window()

    # Creation of init window
    def init_window(self):
        self.master.title("GUI") # Changing title of master widget
        self.pack(fill=BOTH,expand=1) # Allowing the widget to take full space of the root window
        quitbutton = Button(self,text="Quit")
        quitbutton.place(x=0,y=0)
        

root = Tk()
root.geometry("400x300") # Size of window
app = Window(root) # Instance of Window
root.mainloop() # Continuous loop. Like while(1), terminated only by exciting application.


'''
def start_gui():
    root = Tk()
    root.geometry ("500x700")

    root.title("DSPG Melon Demo")
    main_frame = Frame(root)
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    #Fonts Settings
    options_font = tkFont.Font(root ,family="Helvetica", size=14, weight='bold')
    start_font = tkFont.Font(root ,family="Helvetica", size=20, weight='bold')
    font_b = tkFont.Font(root ,family="Helvetica", size=12, weight='bold')
    debug_headline_font = tkFont.Font(root ,family="Helvetica", size=12 ,underline=True)
    
    root.mainloop()
    
start_gui()    
'''



'''
from tkinter import font
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        print("In Init Routine")
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        print("In create widgets routine")
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hi_there["title"] = "Sample Application"
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


class example_application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.grid(row=100, column=100, columnspan=3)
        self.create_widgets()


    def create_widgets(self):
        self.widgetName = tk.Tcl("Sample Application", None)
        self.quitButton = tk.Button(self,text='QUIT', command=self.quit)
        self.quitButton.grid(row=0, column=2, columnspan=3)
            
           
if __name__ == "__main__":
    #appfont = font.font(family='Helvetica',size=36, weight='bold')
    app = example_application()
    #app.master.title('Sample Application')
    app.mainloop()

   
    
    root = tk.Tk() 
    app = Application(master=root)
    app.mainloop()
    
    
'''






