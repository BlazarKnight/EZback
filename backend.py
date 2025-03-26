'''
this is a library of functions for backend manegement
'''
import subprocess
from dataclasses import dataclass
import json
import os

@dataclass
class home_files:
    file_names:list
    file_name_hash_pairs:list

class home_backup_files:
    file_names:list
    file_name_hash_pairs:list

class application_settings:
    path_to_backup_file:str
    path_to_home_file:str

class backup_info:
    info_json_path:str
    time_of_backup:str
    file_name_hash_pairs:str

def os_detect():
    #this will read what os it is runing on and return it
    home_sys=os.name
    return home_sys
def pakmandetect():
    installed_pakmen= subprocess.getoutput(['bash', 'pakmandetect.sh'])
    print(installed_pakmen)


def main():
    print(os_detect())
    pakmandetect()



if __name__=="__main__":
    main()
