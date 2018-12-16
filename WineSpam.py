#!/usr/bin/env python3
# Forged by Vulnrabililities
# @vulnrabilties on instagram
# 13/12/18, 16:51

#  _____                            _       
#  \_   \_ __ ___  _ __   ___  _ __| |_ ___ 
#   / /\/ '_ ` _ \| '_ \ / _ \| '__| __/ __|
#/\/ /_ | | | | | | |_) | (_) | |  | |_\__ \
#\____/ |_| |_| |_| .__/ \___/|_|   \__|___/
#                 |_|

import os
import sys
import smtplib
import time
from time import sleep
     
#  /_\  _ __ (_)_ __ ___   __ _| |_(_) ___  _ __  
# //_\\| '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \ 
#/  _  \ | | | | | | | | | (_| | |_| | (_) | | | |
#\_/ \_/_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|

def Animation():
    print("██╗    ██╗██╗███╗   ██╗███████╗ ")
    time.sleep(0.25)
    print("██║    ██║██║████╗  ██║██╔════╝ ")
    time.sleep(0.25)
    print("██║ █╗ ██║██║██╔██╗ ██║█████╗   ")
    time.sleep(0.25)
    print("██║███╗██║██║██║╚██╗██║██╔══╝   ")
    time.sleep(0.25)
    print("╚███╔███╔╝██║██║ ╚████║███████╗ ")
    time.sleep(0.25)
    print(" ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝ ")
    time.sleep(1)
     
#    ___      __ _                _                       
#   /   \___ / _(_)_ __   ___  __| | /\   /\__ _ _ __ ___ 
#  / /\ / _ \ |_| | '_ \ / _ \/ _` | \ \ / / _` | '__/ __|
# / /_//  __/  _| | | | |  __/ (_| |  \ V / (_| | |  \__ \
#/___,' \___|_| |_|_| |_|\___|\__,_|   \_/ \__,_|_|  |___/

#################################\
# Define SMTP Stuff             ##\
Gmail = 'smtp.gmail.com'         ##\
Gmailport = 587                  ###\
Yahoo = 'smtp.mail.yahoo.com'    ####\
Yahooport = 465                  #####\
Outlook = 'smtp-mail.outlook.com'######\
Outlookport = 587                #######\
iCloud = 'smtp.mail.me.com'      ########\
iCloudport = 587                 ########/
Gmx = 'server:mail.gmx.com'      #######/
Gmxport = 587                    ######/
Zoho = 'smtp.zoho.com'           #####/
Zohoport = 587                   ####/
AOL = 'smtp.aol.com'             ###/
AOLport = 587                    ##/
Hover = 'mail.hover.com'         #/
Hoverport = 587                 #/
################################/
################################\
# Credit to Cri for colour list #\
blue = "\x1b[1;34m"             ##\
white = "\x1b[1;37m"            ###\
cyan = "\x1b[0;36m"             ####\
orng = "\x1b[38;5;50m"          #####\
red = "\x1b[38;5;196m"          ######\
cyan = "\x1b[38;5;50m"          #######\
green = "\x1b[38;5;82m"         ########\
lwhite = "\x1b[1;37m"           #########\
lred = "\x1b[1;31m"             ##########\
lgreen = "\x1b[1;32m"           ##W#I#N#E##\ # NOT IN USE
lyellow = "\x1b[1;33m"          #2#0#1#8###/
lblue = "\x1b[1;34m"            ##########/
lpurple = "\x1b[1;35m"          #########/
lcyan = "\x1b[1;36m"            ########/
dwhite = "\x1b[0;37m"           #######/
dred = "\x1b[0;31m"             ######/
dgreen = "\x1b[0;32m"           #####/
dyellow = "\x1b[0;33m"          ####/
dblue = "\x1b[0;34m"            ###/
dpurple = "\x1b[0;35m"          ##/
dcyan = "\x1b[0;36m"            #/
################################/
#  /\/\   ___ _ __  _   _ 
# /    \ / _ \ '_ \| | | |
#/ /\/\ \  __/ | | | |_| |
#\/    \/\___|_| |_|\__,_|

def Menu():
    while True:
        print('################################')
        time.sleep(0.5)
        Animation()
        print('################################')
        time.sleep(0.5)
        print('1) Gmail 4) iCld  7) AOL   ')
        time.sleep(0.5)
        print('2) Yahoo 5) ZoHo  8) HELP    ')
        time.sleep(0.5)
        print('3) Outlk 6) Hover 9) CUSTOM ')
        time.sleep(1)
        Selection = input("Select an option: ")
        if Selection == '1':
            print("Hi")
            Server = Gmail
            Port = Gmailport
        if Selection == '2':
            Server = Yahoo
            Port = Yahooport
        if Selection == '3':
            Server = Outlook
            Port = Outlookport
        if Selection == '4':
            Server = iCloud
            Port = iCloudport
        if Selection == '5':
            Server = Zoho
            Port = Zohoport
        if Selection == '6':
            Server = Hover
            Port = Hoverport
        if Selection == '7':
            Server = AOL
            Port = AOLport
        if Selection == '8':
            HelpMenu()
            Menu()
        if Selection == '9':
            Server = input("Enter Server: ")
            Port = input("Enter Port: ")
       
        USER = input("Enter your email: ")
    
        PASS = input("Enter your password: ")
    
        TO = input("Enter your Target Email: ")

        MSG = input("What would you like to spam: ")

        print("\n")
        
        Errors = 0

        Loop = True
        
        while Loop == True:
            try:
                mail = smtplib.SMTP(Server,Port)
                mail.ehlo()
                mail.starttls()
                mail.login(USER,PASS)
                mail.sendmail(FROM,TO,MSG)
                mail.close()
                print("Wine sent your mail sucessfully")
                Errors = 0
            except:
                print("There was an error sending the email")
                print("Retrying in 10 seconds              ")
                sleep(1)
                Errors = Errors + 1
                print("\n")
                if Errors == 100:
                    print("\n" * 100)
                    print("Failed to send 100 emails continuously. Continuing")
                    print("\n")
                    Loop = False
                    
Menu()
    
