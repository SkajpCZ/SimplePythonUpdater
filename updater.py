import subprocess, os, sys, time, threading

curversion = 1
os.system('cls' if os.name == 'nt' else 'clear')
def CheckForUpdates():
    if os.name == 'nt':
        try:
            concheck = subprocess.check_output("ping 1.1.1.1 -n 1", shell=True)
            conec = 1
        except: conec = 0
    else:
        try:
            concheck = subprocess.check_output("ping 1.1.1.1 -c 1", shell=True)
            conec = 1
        except: conec = 0
    if conec == 1: 
        subprocess.call("curl --silent https://pastebin.com/raw/test123 -o .version.txt ", shell=True)
        print()
    elif conec == 0: 
        print('\033[1;31m' + "\n No internet connection")
        time.sleep(5)
        exit() # or go to main function

    # Check if update
    with open(".version.txt", "r+") as f:
        bruhint = int(f.read())
        if int(curversion) == bruhint:
            print('\033[1;32m' + " Up to date")
            mainFunction()
        elif int(curversion) > bruhint: 
            print('\033[1;34m' + " Newer (testing)")
        else:
            print('\033[1;31m' + " Old")
            cho = input('\033[1;37m' + "\n \033[4;37mDo you want to download new version?\033[0;38;2;180;180;180m (Y/N)" + '\033[0;90m' + " > " + '\033[0;37m' +f"").lower()
            if cho == "y" or cho == "yes" or cho == "ye":
                # Downloads updated version
                print("\033[90m\n Download started...\n\033[37m")
                threading.Thread(subprocess.call("curl --progress-bar <link> -o <output>", shell=True)).start
                mainFunction() # or you can just exit program
            else:
                mainFunction() # or you can just exit program


def mainFunction():
    print("\033[37m Hello world")
    time.sleep(10)

CheckForUpdates()