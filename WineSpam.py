#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Creator = wine
#Current instagram name @Deadconnections
import random
import smtplib
import time
import string
from time import sleep
def sleep():
    time.sleep(1)
def sendbots():
    context = MSG
    mail = smtplib.SMTP(Server,Port)
    mail.ehlo()
    mail.starttls()
    mail.login(USER,PASS)
    mail.sendmail(FROM,TO,MSG)
    mail.close()
    print("Wine sent your mail sucessfully")
#MADE BY WINE HIMSELF 03/11/2018
print("")
print("Hello User and welcome to an email spammer by")
print("                 # OPEN SOURCE #             ")
print(""" ██░ ██ ▓█████  ██▓     ██▓      ██████ ▓█████  ▄████▄  
▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▒██▀▀██░▒███   ▒██░    ▒██░    ░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▓█▒░██▓░▒████▒░██████▒░██████▒▒██████▒▒░▒████▒▒ ▓███▀ ░
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
 ░  ░░ ░   ░     ░ ░     ░ ░   ░  ░  ░     ░   ░        
 ░  ░  ░   ░  ░    ░  ░    ░  ░      ░     ░  ░░ ░      
                                               ░  W I N E      """)
print("########################################################  ")
print("1: Gmail       6: PRIVATE          11: PRIVATE              ")                     
print("2: PRIVATE     7: PRIVATE          12: PRIVATE              ")
print("3: PRIVATE     8: PRIVATE          13: PRIVATE            ")
print("4: PRIVATE     9: PRIVATE          14: PRIVATE             ")
print("5: To exit    10: MANUALPRIVATE    15: PRIVATE            ")                         
print("########################################################  ")
Server = input("please select which email you use 1-4: ")
if Server == '1':
    Server = 'smtp.gmail.com'
    Port = 587
else:
    print("Sorry these are private source")
    sleep()
    exit()
USER = input("What is your email: ")
PASS = input("What is your password: ")
FROM = USER # Becuase this wasnt working
TO = input("Who do you want to send the email too: ")
MSG = 'HELLSEC OWNS YOU'
print("SENDING 100 EMAILS")
print("########################################################")
print("IF GMAIL ERRORS PLEASE ALLOW LESS SECURE APPS OR TRY A DIFFERENT EMAIL")
print("AND MAKE SURE YOUR CREDENTIALS ARE CORRECT")
WINESPAM = 100
while WINESPAM > 0:
    sendbots()
    WINESPAM = WINESPAM-1




            
            
#Please log in via\n5.7.14 your web browser and then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 l4-v6sm51203760wrb.92 - gsmtp
#if you get an error life this just create a new gmail for it and allow less secure apps
