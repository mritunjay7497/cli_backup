# cli_backup
This script create the backup of the files/folder whose names/path are supplied , compresses it using zip, encrypt the compressed file and finally upload it to the google drive. In all this process the file permission,modification time,ownership and symlinks status (if any) remain preserved.
To run the program, simply execute:
python3 drive_upload.py 
or
./drive_upload.py
