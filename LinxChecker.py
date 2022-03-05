# -*- coding: utf-8 -*-
#Developed by DarkSide

import requests, os
from bs4 import BeautifulSoup
import re, sys
from termcolor import colored
import os, sys
import argparse

os.system("clear")
print(colored("""
 █████        ███                           █████████  █████                        █████                        
░░███        ░░░                           ███░░░░░███░░███                        ░░███                         
 ░███        ████  ████████   █████ █████ ███     ░░░  ░███████    ██████   ██████  ░███ █████  ██████  ████████ 
 ░███       ░░███ ░░███░░███ ░░███ ░░███ ░███          ░███░░███  ███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
 ░███        ░███  ░███ ░███  ░░░█████░  ░███          ░███ ░███ ░███████ ░███ ░░░  ░██████░  ░███████  ░███ ░░░ 
 ░███      █ ░███  ░███ ░███   ███░░░███ ░░███     ███ ░███ ░███ ░███░░░  ░███  ███ ░███░░███ ░███░░░   ░███     
 ███████████ █████ ████ █████ █████ █████ ░░█████████  ████ █████░░██████ ░░██████  ████ █████░░██████  █████    
░░░░░░░░░░░ ░░░░░ ░░░░ ░░░░░ ░░░░░ ░░░░░   ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                                                                 
                                                                                                                 
                                                                                                                 
""", "yellow"))

print("=============================================================================================================== \n")
#Funcion de Web Scrapling 
#def web_scrap(data):
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action='store', dest="url", help="The URL works as target to test")
parser.add_argument("-o", "--output", action='store', dest="output", help="Directs the output to a name of your choice")
args = parser.parse_args()


if len(sys.argv) < 2:
    print ("Usage: ./LinxChecker {URL to test}")
    sys.exit(2)
else:
    data = str(sys.argv[2])
    try:
        page = requests.get(data)
    except:
        print ("The target must be in URL format {http://, https://}\n")
        sys.exit(2)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    i=0
    tags = soup.find_all('a',  href=True)
    print("LIST OF FOUND LINKS:\n")
    
    for tag in tags:
        link = (tags)[i]['href']
        print (colored (" * " + link + " - Found! \n", "green"))
        if len(sys.argv) > 3:
            if(i==0):
                with open(args.output, 'w') as f:
                    f.write("REPORT:\n")
            else:
                with open(args.output, 'a') as f:
                    f.write(colored (" * " + link + "  - Found! \n", "green"))

        i=i+1
        