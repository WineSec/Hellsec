#!/bin/bash

clear
echo "Installing Depandancys hold on"
sudo apt-get update
sudo apt-get install t50
sudo apt-get install nmap
sudo apt-get install zenmap
sudo apt-get install sqlmap
sudo apt-get install python3
chmod 777 Hellsec.sh
chmod 777 SqlEasy.sh
chmod 777 WineSpam.py
sleep 3
clear
echo "Installing python modules"
pip install termcolor
sleep 1
clear
echo "Installation finished, hold on"
./Hellsec.sh
