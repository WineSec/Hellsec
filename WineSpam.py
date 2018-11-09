#!/usr/bin/env python
#MADE BY WINE HIMSELF 03/11/2018 - Original private source
#MADE BY WINE HIMSELF 08/11/2018 - This source (Simplified as fuck)

import smtplib
import time
from time import sleep

Server = 'smtp.gmail.com' # SMTP SERVER
Port = 587 # CAN KEEP SAME USUALLY IS (SMTP PORT)


def sendbots(): # DEFINES TO SEND MSG
    mail = smtplib.SMTP(Server,Port) # Set SMTP server from the variables and the port
    mail.ehlo() #provide optimal use of bandwidth, reduce latency of message transport and improve error handling.
    mail.starttls() #Transport Layer Security (TLS) encrypts msgs so ur password isnt exposed
    mail.login(USER,PASS) # Login as user and password variables that you enter
    mail.sendmail(FROM,TO,MSG) #Sends mail as the from to and msg variables
    mail.close() #end connection
    print("Wine sent your mail sucessfully")

# Change to your liking
MSG = 'Hellsec Owns You'
FROM = 'Hellsec' # Not sure if this does anything anymore


USER = input("Enter your username: ") # ENTER USERNAME
PASS = input("Enter your password: ") # ENTER PASSWORD 
TO = input("Who would you like to send this email to: ") # DESTINATION EMAIL
print("SENDING EMAILS AS LONG AS POSSIBLE")



LOOP = True
while LOOP == True: #LOOP IS CONSTANT
    try:
        sendbots() # TRY TO SEND MAIL
    except:        # IF FAILS
        print("Mission failed give it a little while")
        time.sleep(10) # WAIT 10 SECONDS AND RETRY 20 makes less freezes
        continue



# FOR YOUR INFORMATION THIS IS FASTER THAN THE PRIVATE SOURCE
# PLEASE DONT TELL ANYONE
# W I N E
# HELLSEC 09/11/2018


