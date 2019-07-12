#!/usr/bin/env python3

'''
This script uses python3 to backup the files from the source directory
into the destinantion directory. The backup action is performed
by 'rsync' command line tool in linux , which has certain merits of it's own
such as delta-transfer(increamental-backups),preserving permissions and directory
structure as it is. Since it uses rsync to prepare the initial backup files, this
script is explicitly for linux operating systems.

As rsync already prepares the backup, this script compress(password-protected),
encrypt, get hash sums, store the critical info(such as compression key, encryption key and hash sum)
in a file and upload the encrypted backup file ONLY to the google drive. The file containing the info
about the  backed-up files are left there on the host, on the user dicretion. Also, all these process
uses time stamp as the file name to ease the process of restoring them
'''
import os
from colorama import Fore as f
from colorama import Style as s
from colorama import init
import sys
import datetime
import time

init(autoreset=True)

src_dir = ''
tmp_dir = ''
new_name = ''

def backup_dir_info():
	global src_dir
	global tmp_dir
	print(f.RED+"Enter the source directory path")
	src_dir = str(input("[*] src_directory >>:  "))
	print(f.BLUE+"\nEnter the destinantion directory to temporarily store the backed-up files.\n")
	print(f.BLUE+"Files in this temporary destinantion directory will be compressed,encrypted and uploaded to the drive")
	tmp_dir = str(input("[*] tmp_dest_directory >>:  "))

def dir_check():
	if(os.path.isdir(src_dir)):
		if(src_dir!=tmp_dir):
			if(os.path.isdir(tmp_dir)):
				backup_script()
			else:
				print(f.WHITE+"\n\n[!!]The temporary destinantion directory doesn't exist\n[!!]Creating now...\n[*]Directory created\n")
				time.sleep(1)
				backup_script()
		else:
			print(f.WHITE+"[!!] Source directory and temporary back up directory cannot be same\n[!!] Exiting now...\n")
			sys.exit(0)
	else:
		print(f.WHITE+"[!!]The source file doesn't exist.\n[!!]Enter correct directory\n")
		print(f.WHITE+"[??]Do you want to try again?\n[!!]press (y)es or (n)o...\n")
		ans = input()
		if(ans=='y' or ans=='Y'):
			backup_dir_info()
			dir_check()
		elif(ans=='n' or ans=='N'):
			print(f.WHITE+"[!!]TERMINATING PROGRAM !!\n")
			sys.exit(0)

def backup_script():
	global new_name
	print(f.RED+"Initiating backup program on %s"%src_dir)
	backup_cmd = 'rsync -uavz --progress '+src_dir+' '+' '+tmp_dir+'/'
	os.system(backup_cmd)
	time.sleep(2)
	print(f.YELLOW+"\nchanging backup files name to current date and time...\n")
	current_date = str(datetime.datetime.now()).replace(" ","___")
	time.sleep(2)
	name_change = 'mv'+' '+tmp_dir+'/*'+' '+tmp_dir+'/'+src_dir.replace('/','__')+"*****"+current_date
	os.system(name_change)
	print(f.YELLOW+"\n[*]Listing backed-up files\n")
	os.system('ls -lah'+' '+tmp_dir)
	new_name = src_dir.replace('/','__')+"*****"+current_date
	return new_name

backup_dir_info()
dir_check()


