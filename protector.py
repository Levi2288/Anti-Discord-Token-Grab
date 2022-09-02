# coding: utf-8

from os import system
from os.path import exists

#from colorama import Fore
#import fade, psutil
import ctypes, random, string, subprocess, time, errno, os, stat, shutil, sys



#IF YOU WANT TO COMPILE ME REMOVE THE CODE FROM 14 TO 27 AND UNCOMMENT THE IMPORTS ABOVE
try:
    from colorama import Fore
    import psutil
    import fade

except ModuleNotFoundError:
    scriptPath = os.getcwd() + "\\" + os.path.basename(__file__)
    print("Please Wait. Installing dependencies")
    subprocess.call(f'pip install colorama==0.4.5', shell=True, creationflags=0x08000000)  ## Install requirements
    subprocess.call(f'pip install fade==0.0.9', shell=True, creationflags=0x08000000)  ## Install requirements
    subprocess.call(f'pip install psutil==5.9.1', shell=True, creationflags=0x08000000)  ## Install requirements
    print("Please run the script again!")
    exit(0)


__author__ = 'Levi2288'
__version__ = 1.0
__status__ = 'Beta'
_AppName_ = 'Discord Token Protector'

##VARS
APP_List = ["Discord.exe", "DiscordPTB.exe", "DiscordCanary.exe"]
MODULE_List = ["colorama", "psutil", "fade"]
LOCAL = os.getenv("LOCALAPPDATA")
APPDATA = os.getenv("APPDATA").replace("\\Roaming", "")
ASCII = """\n\n ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
  ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
  ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
  ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
  ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"""



DC_LOCAL_PATH = "\\Local\\Discord"
PTB_LOCAL_PATH = "\\Local\\DiscordPTB"
CANARY_LOCAL_PATH = "\\Local\\DiscordCanary"



DC_ROAMING_PATH = "\\Roaming\\discord"
PTB_ROAMING_PATH = "\\Roaming\\discordptb"
CANARY_ROMING_PATH = "\\Roaming\\discordcanary"

DC_INSTALLED = False
PTB_INSTALLED = False
CANARY_INSTALLED = False


##MISC



##############
####UTILS#####
##############


def get_folder(path, name):
    return [f for f in os.listdir(path) if os.path.isdir(path + "\\" + f) and f.find(name) != -1]

def get_discord_version(path, NAME):
    folder = get_folder(APPDATA + path, "app-")[0].split("-")[1]
    fullpath = APPDATA + path + "\\" + "app-" + folder

    ## Lets Make sure we only have 1 Discord version installed
    while exists(fullpath + "\\resources".strip()) == False:
        if (isProcessAlive(NAME)):
            subprocess.call(f"TASKKILL /F /IM {NAME}", shell=True, creationflags=0x08000000) # Taskill the specific app
        #print(f"We found some problems. Just lay back while we try to solve it.")
        time.sleep(3) # Wait for all processes to stop and let us use remove the stuff
        shutil.rmtree(fullpath, ignore_errors=False, onerror=handleRemoveReadonly)
        time.sleep(1) # wait for it to get removed
        folder = get_folder(APPDATA + path, "app-")[0].split("-")[1]
        fullpath = APPDATA + path + "\\" + "app-" + folder
    else:
        return folder

def id_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def syscheck():
    if os.name != 'nt':
        print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}This protector is not made for this operating system.")
        system("pause")
        exit(0)

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

def isProcessAlive(proc):
    for process in psutil.process_iter():
        if process.name() == proc:
            return True
    return False

def cmdOutput(cmd):

    result = subprocess.getoutput(cmd)
    return result


def uninstallNode():
    if ("not recognized") in cmdOutput("node -v"):
        print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Node.js is not installed. Uninstaller marked as completed{Fore.RESET}")
    else:
        scriptPath = os.getcwd()
        installerPath = scriptPath + "\\setup\\node-v16.17.0-x64.msi"
        print(installerPath)
        if (exists(installerPath)):  # Check Path
            print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}Installer found starting uninstalling...{Fore.RESET}")
            subprocess.call(f'MsiExec.exe /x \"{installerPath}\" /qn')  ## Install Node.js
            time.sleep(3)
            if ("not recognized") in cmdOutput("node -v"):
                print(f"{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Uninstalling was successful. No more Node.js{Fore.RESET}")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}Uninstalling failed.{Fore.RESET}")

def checkifNodeInstalled():
    if ("not recognized") in cmdOutput("node -v"):
        print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}Node.js is missing!{Fore.RESET}")
        time.sleep(1)
        print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}Installing Node.js...{Fore.RESET}")
        scriptPath = os.getcwd()
        installerPath = scriptPath + "\\setup\\node-v16.17.0-x64.msi"
        print(installerPath)
        if(exists(installerPath)): # Check Path
            print(f"{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}Installer found starting installing...{Fore.RESET}")
            subprocess.call(f'MsiExec.exe /i \"{installerPath}\" /qn') ## Install Node.js
            time.sleep(3)
            if ("not recognized") in cmdOutput("node -v"):
                print(f"{Fore.RED}CRITICAL{Fore.RESET}] {Fore.RED}Installation failed!{Fore.RESET}\nPlease Install Node.js manually.\nInstaller Location: {installerPath}")
            else:
                print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Installation has been successful.{Fore.RESET}")
    else:
        print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Node.js Found! We are good to go!{Fore.RESET}")



##############
##############
##############





def extract_files(resource):
    print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}Extracting app.asar...{Fore.RESET}")
    try:
        subprocess.call("npm i -g asar", shell=True, creationflags=0x08000000)
        subprocess.call("asar extract " + resource + "\\app.asar" + " " + resource + "\\tmp", shell=True, creationflags=0x08000000)
        time.sleep(1)
        patch_dc(resource)
    except Exception as e:
        print(f"[{Fore.RED}CRITICAL{Fore.RESET}] {Fore.RED}Extract error!{Fore.RESET}")
        print("\n\n1 | Return To Main Menu")
        print("2 | Uninstall Node & Quit")
        print("3 | Quit")
        choice = int(input("\n\nChoice > "))
        while choice == None:
            choice = int(input("Choice > "))
        else:
            if int(choice) == 1:
                main()
            elif int(choice) == 2:
                uninstallNode()
                time.sleep(3)
                exit(0)
            elif int(choice) == 3:
                exit(0)


def patch_dc(RESOURCES_PATH):
    patch = ""
    PATH_HASH = id_generator(random.randint(6,24))
    with open(RESOURCES_PATH+"\\tmp\\common\\paths.js", "r") as f:
        content = f.read()
        old_content = "return _path.default.join(userDataRoot, 'discord' + (buildInfo.releaseChannel == 'stable' ? '' : buildInfo.releaseChannel));"
        if (content.find(old_content) == -1):
            print(f"{Fore.RED}-{Fore.RESET}] {Fore.RED}This file is not original skipping...{Fore.RESET}")
            return None
        patch = content.replace(old_content, old_content.replace("'discord'", "'"+PATH_HASH+"'"))
    with open(RESOURCES_PATH+"\\tmp\\common\\paths.js", "w") as f:
        if f.write(patch):
            os.mkdir(APPDATA + "\\Roaming\\" +PATH_HASH)
            print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Patch applied!{Fore.RESET}")
    system("asar pack " + RESOURCES_PATH+"\\tmp" + " " + RESOURCES_PATH+"\\app.asar")

def protect_DC(LOCAL_PATH, ROAMING_PATH, VER, NAME, panel):
    NAME = NAME.replace(".exe", "")
    if not VER:
        print(f"[{Fore.RED}CRITICAL{Fore.RESET}] {Fore.RED}Invalid {NAME} version!{Fore.RESET}")
    else:
        resource_path = ""
        resource_path = APPDATA + LOCAL_PATH + "\\app-" + VER + "\\resources"
        if os.path.exists(resource_path) == False:
            print(f"[{Fore.RED}CRITICAL{Fore.RESET}] {Fore.RED}Something went wrong failed protecting {NAME}{Fore.RESET}")
        else:
            print(f"\n\n[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}{NAME} Version: {VER}{Fore.RESET}")
            print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}Protecting {NAME}...{Fore.RESET}")
            extract_files(resource_path)


        subprocess.call(f"TASKKILL /F /IM {NAME}.exe", shell=True, creationflags=0x08000000)

        if(os.path.exists(APPDATA + ROAMING_PATH)):
            try:
                shutil.rmtree(APPDATA + ROAMING_PATH, ignore_errors=False, onerror=handleRemoveReadonly)
                print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}{NAME} removed successfully!\n{Fore.RESET}")
                print(f"[{Fore.CYAN}i{Fore.RESET}] {Fore.CYAN}DO NOT FORGET TO LOG OUT FROM YOUR BROWSER! OR THIS PROTECTION WILL DO NOTHING.\nFr do not log into discord in your browser!{Fore.RESET}")
            except OSError as error:
                print(error)
                print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}File path can not be removed{Fore.RESET}")
                print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}Please remove {Fore.YELLOW}{APPDATA + ROAMING_PATH}{Fore.RESET} yourself! ASAP{Fore.RESET}")

    if panel:
        print("\n\n1 | Return To Main Menu")
        print("2 | Uninstall Node & Quit")
        print("3 | Quit")
        choice = int(input("\n\nChoice > "))
        while choice == None:
            choice = int(input("Choice > "))
        else:
            if int(choice) == 1:
                main()
            elif int(choice) == 2:
                uninstallNode()
                time.sleep(3)
                exit(0)
            elif int(choice) == 3:
                exit(0)



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False

def main():

    checkifNodeInstalled()
    global PTB_INSTALLED, DC_INSTALLED, CANARY_INSTALLED, APP_List
    DC_VER = ""
    PTB_VER = ""
    CANARY_VER = ""
    print(f''' {fade.purpleblue(ASCII)}''')

    print(f''' {fade.purpleblue("By:{}".format(__author__).center(110))}''')
    print("Wich Discord Do you Wish To Protect?\n")
    print("0 | Every Installed Discord")
    if (os.path.exists(APPDATA + DC_ROAMING_PATH)):
        DC_INSTALLED = True
        DC_VER = get_discord_version(DC_LOCAL_PATH, APP_List[0])
        print("1 | Discord")
    if (os.path.exists(APPDATA + PTB_LOCAL_PATH)):
        PTB_INSTALLED = True
        PTB_VER = get_discord_version(PTB_LOCAL_PATH, APP_List[1])
        print("2 | Discord PTB")
    if (os.path.exists(APPDATA + CANARY_LOCAL_PATH)):
        CANARY_INSTALLED = True
        CANARY_VER = get_discord_version(CANARY_LOCAL_PATH, APP_List[2])
        print("3 | Discord Canary")

    print("\n\n")
    choice = input("Choice > ")
    while choice == None:
        choice = input("Choice > ")
    else:
        if int(choice) == 0:

            if (DC_INSTALLED):
                protect_DC(DC_LOCAL_PATH, DC_ROAMING_PATH, DC_VER, APP_List[0], False)
            if (PTB_INSTALLED):
                protect_DC(PTB_LOCAL_PATH, PTB_ROAMING_PATH, PTB_VER, APP_List[1], False)
            if (CANARY_INSTALLED):
                protect_DC(CANARY_LOCAL_PATH, CANARY_VER, APP_List[2], False)
        elif int(choice) == 1:
            protect_DC(DC_LOCAL_PATH, DC_ROAMING_PATH, DC_VER, APP_List[0], True)

        elif int(choice) == 2:
            protect_DC(PTB_LOCAL_PATH, PTB_ROAMING_PATH, PTB_VER, APP_List[1], True)

        elif int(choice) == 3:
            protect_DC(CANARY_LOCAL_PATH, CANARY_ROMING_PATH, CANARY_VER, APP_List[2], True)

        if (choice == "quit") or (choice == "exit"):
            exit(0)




if __name__ == '__main__':
    os.system('cls')
    os.system('mode con: cols=150 lines=40')
    if is_admin():
        main()
    else:
        # Re-run the program with admin rights
        print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED}This Program requires Admin Rights!{Fore.RESET}")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        time.sleep(20)
        exit(0)