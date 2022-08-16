import os
import collections
import psutil
import requests
import windows_tools.antivirus
import shutil
import windows_tools.bitlocker
print("""
   __________    __________  ____  __ 
  / ___/ ___/   /_  __/ __ \/ __ \/ / 
  \__ \\__ \     / / / / / / / / / /  
 ___/ /__/ /    / / / /_/ / /_/ / /___r
/____/____/    /_/  \____/\____/_____/
        sstool made by patrickop#5498
                                      
""")
def downloadtool():
    os.system("mkdir ss_tool")
    URL = "https://cdn.discordapp.com/attachments/993511769949622372/1009103456793002076/ss.zip"
    response = requests.get(URL)
    open("ss_tool\\sstool.zip", "wb").write(response.content) 
    shutil.unpack_archive("ss_tool\\sstool.zip", "ss_tool")
    os.system("del ss_tool\\sstool.zip")
    menue()
    

def fsutil():
    os.system("mkdir fsutil")
    os.system("fsutil usn readjournal c: csv > fsutil\\AllTheJournal.txt")
    os.system("fsutil usn readjournal c: csv | findstr /i /c:.exe | findstr /i /c:0x80000200 >> fsutil\\DeletedExes.txt")
    os.system("fsutil usn readjournal c: csv | findstr /i /c:.exe | findstr /i /c:0x00000100 >> fsutil\\Createdfiles.txt")
    os.system("fsutil usn readjournal c: csv | findstr /i /c:.exe | findstr /i /c:0x00001000 >> fsutil\\oldnamefiles.txt")
    os.system("fsutil usn readjournal c: csv | findstr /i /c:.exe | findstr /i /c:0x00002000 >> fsutil\\newnamefiles.txt")
    menue()

def bitlockercheck():
    result = windows_tools.bitlocker.get_bitlocker_full_status()
    for drive in result:
        for designation, content in result[drive].items():
            print(designation, content)
    menue()

def antiviruscheck():
    result = windows_tools.antivirus.get_installed_antivirus_software()
    print(result)
    menue()


def dreamdetect():
    filesiyzeliste = []

    for path, subdirs, files in os.walk(r'C:\Windows\prefetch'):
        for name in files:
            pathprefetch = (os.path.join(path, name))
            file_size = os.path.getsize(pathprefetch)
            test = (file_size)
            filesiyzeliste.append(test)

    tktfrere = ([item for item, count in collections.Counter(filesiyzeliste).items() if count > 1])



    for path, subdirs, files in os.walk(r'C:\Windows\prefetch'):
        for name in files:
            pathprefetch2 = (os.path.join(path, name))
            file_size2 = os.path.getsize(pathprefetch2)
            if  str(file_size2) in str(tktfrere):
                print("same file size found : " +  str(pathprefetch2) + " file size is : " + str(file_size2) + "(verify if the name file is same)")
    print("if nothing appears it means that nothing was found")
    menue()


def servicecheck():
    def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    service = getService('sysmain')




    if service and service['status'] == 'running':
        print("sysmain service is running")
    else:
        print("sysmain service is not running")




    def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    service = getService('eventlog')



    if service and service['status'] == 'running':
        print("eventlog service is running")
    else:
        print("eventlog service is not running")

    def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    service = getService('diagtrack')




    if service and service['status'] == 'running':
        print("diagtrack service is running")
    else:
        print("diagtrack service is not running")


    def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    service = getService('pcasvc')




    if service and service['status'] == 'running':
        print("pcasvc service is running")
    else:
        print("pcasvc service is not running")

    def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    service = getService('sysmain')



    if service and service['status'] == 'running':
        print("sysmain service is running")
    else:
        print("sysmain service is not running")
    menue()





def menue():

    print("\n\n1) latest Dream guide\n2) services check\n3) antivirus\n4) bitlocker\n5) fsutil\n6) Download ss tool")
    choose = input("Choose Number : ")
    if choose == "1":
        os.system('cls')
        dreamdetect()

    elif choose == "2":
        os.system('cls')

        servicecheck()
    elif choose == "3":
        os.system('cls')
        antiviruscheck()

    elif choose == "4":
        os.system('cls')
        bitlockercheck()

    elif choose == "5":
        os.system('cls')
        fsutil()      

    elif choose == "6":
        os.system("cls")
        downloadtool()



    else:
        os.system('cls')
        menue()

menue()
