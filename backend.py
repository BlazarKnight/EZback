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

#command -v
def pakmandetect():
    installed_pakmen=[]
    for i in ['apk', 'app', 'apt', 'apt-get', 'cargo', 'dnf', 'dpkg', 'emerge', 'eopkg', 'flatpak', 'nala', 'moss', 'nix-env', 'pacman', 'pamac', 'portage', 'rpm', 'snap', 'xbps', 'yay', 'yum', 'zypper']:
        if os.popen(f'command -v {i}').read() != '':
            #path_to_pakman= str(os.popen(f'command -v {i}').read()).removesuffix('\n')
            installed_pakmen.append(i)
    return installed_pakmen

def packdetect(list_of_pakmen:list):
    paks_list=[]
    for i in list_of_pakmen:
        if i == 'apt' | 'apt-get' | 'dpkg':
            debpaks=os.popen(' dpkg --get-selections | cut -f1').read()
        if i == 'snap':
            pass
def main():
    print(os.popen(' dpkg --get-selections | cut -f1').read())




if __name__=="__main__":
    main()
