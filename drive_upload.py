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

zip_file = compression.backup_file_path+'.zip'

print(zip_file)
print(compression.critical_info)
gdrive_status = 0


def drive_upload():
    # auto upload function
    os.system('which gdrive')

    if(gdrive_status != os.system('echo $?')):
        print(f.WHITE+"[!!]Configure gdrive for linux and then try again\n")
        print(
            f.WHITE+"[*]Download gdrive for linux from https://github.com/gdrive-org/gdrive\n")
        print(
            f.WHITE+"[*]You will also have to enable Drive API v3 to get this software working\n")
        sys.exit(0)
    else:
        print(f.YELLOW+"[*]initiating upload on the google drive\n")
        parent_dir_id = parent_dir_id.parent_dir_id
        print(f.RED+parent_dir_id)
        upload_cmd = 'gdrive upload -p '+parent_dir_id+' '+zip_file
        os.system(upload_cmd)

    os.system("cd "+compression.info_dir+" && rm "+zip_file)
    os.system("cd "+compression.info_dir+" && mv " +
              compression.backup_file_path+".txt /home/$USER/backup")


print(f.WHITE+"Do you want to auto-upload the backed-up files to your drive?\n(y)es or (n)o")
auto_upload = input("Enter response: >> ")

if(auto_upload == 'y' or auto_upload == 'Y'):
    # auto upload function
    drive_upload()
else:
    # add manual upload function

    # move backup to backup folder, /home/$USER/backup
    print(f.WHITE+"Moving back-ups to your backup folder...")
    os.system("cd "+compression.info_dir+" && mv " +
              zip_file+" /home/$USER/backup")
    time.sleep(4)

    print(f.WHITE+"Moving critical info file to backfile")
    os.system("cd "+compression.info_dir+" && mv " +
              compression.backup_file_path+".txt /home/$USER/backup")

    print("\n\nBACKUP PROCESS COMPLETE...\n\nDeleting temorary files...\n\n")
    os.system("rm -rf "+compression.backup_file_path)

    print("Terminating process !!")
    sys.exit(0)
