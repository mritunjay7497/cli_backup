#!/usr/bin/env python3

'''
This script uploads the compressed and encrypted back-up zip file to the google drive.
The critical info such as back-up file name and decryption password are stored on the user 
system.
'''

import os
import sys
import time
import compression
import parent_dir_id
from colorama import Fore as f
from colorama import Style as s
from colorama import init

init(autoreset=True)

zip_file=compression.backup_file_path+'.zip'

print(zip_file)
print(compression.critical_info)
gdrive_status=0
os.system('which gdrive')

if(gdrive_status!=os.system('echo $?')):
	print(f.WHITE+"[!!]Configure gdrive for linux and then try again\n")
	print(f.WHITE+"[*]Download gdrive for linux from https://github.com/gdrive-org/gdrive\n")
	print(f.WHITE+"[*]You will also have to enable Drive API v3 to get this software working\n")
	sys.exit(0)
else:
	print(f.YELLOW+"[*]initiating upload on the google drive\n")
	parent_dir_id = parent_dir_id.parent_dir_id
	print(f.RED+parent_dir_id)
	upload_cmd = 'gdrive upload -p '+parent_dir_id+' '+zip_file
	os.system(upload_cmd)

os.system("cd "+compression.info_dir+" && rm "+zip_file)
os.system("cd "+compression.info_dir+" && mv "+compression.backup_file_path+".txt /root/projects/backup_python")