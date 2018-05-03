#Setup Script 
import time
import imp
import os

def __main__():

        print("""\033[1;35;40m 

             ______         ____        _   ___                      _____       
            /_  __/______  / / / ____  | | / (_)_____ _____   ____  / ___/__ ___ 
             / / / __/ _ \/ / / /___/  | |/ / / __/ // (_-<  /___/ / (_ / -_) _ |
            /_/ /_/  \___/_/_/         |___/_/_/  \_,_/___/        \___/\__/_//_/
                                                                     

                                  || Setup ||      
    """)
    
        print("==========================================================")
        print("[+] Checking & Installing Required Modules...")
        print("==========================================================")
        time.sleep(2)
        print("==========================================================")
        print("[+] Checking if pynput exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('pynput')
            exists = True
        except ImportError:
            exists = False
        print("[+] Pynput Exists : ", exists)
        if(exists == False):
            print("[-] Pynput not installed, Installing..")
            pip.main(['install', 'pynput'])
        else:
            print("[+] Pynput is Installed.")
        print("==========================================================")
        print("[+] Checking if webbrowser exists..")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('webbrowser')
            exists = True
        except ImportError:
            exists = False
        print("[+] webbrowser Exists : ", exists)
        if(exists == False):
            print("[-] webbrowser not installed, Installing..")
            pip.main(['install', 'webbrowser'])
        else:
            print("[+] webbrowser is Installed.")
        print("==========================================================")
        print("[+] Checking if tkinter exists..")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('tkinter')
            exists = True
        except ImportError:
            exists = False
        print("[+] tkinter Exists : ", exists)
        if(exists == False):
            print("[-] tkinter not installed, Installing..")
            print("[*] It should be installed by Python but double checking is nessecary.")
            pip.main(['install', 'tkinter'])
        else:
            print("[+] tkinter is Installed.")

        print("==========================================================")
        print("[+] Checking if Ctypes exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('ctypes')
            exists = True
        except ImportError:
            exists = False
        print("[+] ctypes Exists : ", exists)
        if(exists == False):
            print("[-] ctypes not installed, Installing..")
            pip.main(['install', 'ctypes'])
        else:
            print("[+] Ctypes is Installed.")

        print("==========================================================")
        print("[+] Checking if time exists...")
        print("[*] It should be installed by Python but double checking is nessecary.")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('time')
            exists = True
        except ImportError:
            exists = False
        print("[+] time Exists : ", exists)
        if(exists == False):
            print("[-] time not installed, Installing..")
            pip.main(['install', 'time'])
        else:
            print("[+] time is Installed.")

        print("==========================================================")
        print("[+] Checking if pyinstaller exists..")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('pyinstaller')
            exists = True
        except ImportError:
            exists = False
        print("[+] pyinstaller Exists : ", exists)
        if(exists == False):
            print("[-] pyinstaller not installed, Installing..")
            pip.main(['install', 'pyinstaller'])
        else:
            print("[+] pyinstaller is Installed.")
        time.sleep(5)
        print("==========================================================")
        print("[+] Installation Completed.")
        input("[*] Hit Enter..")
        print("==========================================================")
        


if __name__ == '__main__':
    __main__()