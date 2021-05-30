#!/usr/bin/python3

'''
This script compresses the backed up file in the temporary directory and make 
it password protected
'''
import os
import sys
import time
import random
import string
import backup
from colorama import Fore as f
from colorama import Style as s
from colorama import init

init(autoreset=True)
info_dir = backup.tmp_dir
backup_file_path = backup.tmp_dir+'/'+backup.new_name
def random_password():
	randomSource = string.ascii_letters + string.digits
	password = random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	for i in range(10):
	    password += random.choice(randomSource)
	passwordList = list(password)
	random.SystemRandom().shuffle(passwordList)
	password = ''.join(passwordList)
	return password

print(f.RED+"[*]BEGINING COMPRESSION OF BACKED-UP FOLDERS AND FILES\n")
print(f.RED+"[*]THESE COMPRESSED FILES WILL BE ENCRYPTED BY THE PROGRAM\n[*]HOWEVER, USER MAY SELECT TO ENTER HIS OWN COMPRESSION PASSWORD\n")
print(f.BLUE+"\n[??]enter (y)es to supply your own password and (n)o to generate random (VERY STRONG) password\n")
choice = str(input(">>> : "))

if (choice =='y'or choice=='Y'):
	print(f.RED+"[*]you have selected to enter user-defined password\n[*]Enter password at next prompt\n")
	password = str(input("enter compression password: "))
	
elif(choice=='n' or choice=='N'):
	print(f.RED+"[*]you have opted for the program to generate a strong pasword\n")
	password = random_password()

def compress_func():
	
	compress_cmd = 'zip -P '+password+' '+'-y '+'-r '+backup_file_path+'.zip'+' '+backup_file_path
	print(f.YELLOW+"\n[*]compressing files using zip utility...\n")
	os.system(compress_cmd)
	time.sleep(2)
	print(f.BLUE+"\n[*]Listing compressed files\n\n")
	os.system('ls -lah '+backup.tmp_dir)
	time.sleep(2)
	


compress_func()

critical_info = {"backup_file: ":backup_file_path,"compression_password: ":password}

# create a folder to store back-ups
os.system('mkdir /home/$USER/backup')

print(f.GREEN+"Your back-up folder is /backup in your home directory...\n\n")

critical_info_cmd = 'cd /home/$USER/backup && echo '+str(critical_info)+' >> '+backup_file_path+'.txt'
os.system(critical_info_cmd)
