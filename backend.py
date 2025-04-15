'''
this is a library of functions for backend manegement
'''

from dataclasses import dataclass
import json
import os
from glob import glob
import hashlib


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
    #todo: add the rest of the pakmen comands
    paks_list=[]
    for i in list_of_pakmen:
        if i == 'apt' | 'apt-get' | 'dpkg':
            debpaks=os.popen(' dpkg --get-selections | cut -f1').read()
        if i == 'snap':
            pass

#todo add ls limed to specifid folder to backup

#todo make hash file pair constuctors
#todo add simple file copying and pasting comand
#todo desine some siple vesion manegment system

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()
def directory_to_filelist(directory:str):
    list_of_paths_to_files=[]
    walk_of_directory =list( os.walk(directory))
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:

            list_of_paths_to_files.append(os.path.join(dirpath, f))
    return list_of_paths_to_files



def directory_to_file_hash_pair_dict(directory:str): #this needs legacy pairady at all times!!!!!!!!!!!!!!!!!!!!!!1
    list_of_paths_to_files = directory_to_filelist(directory)
    dict_of_files_in_directory_as_key_hash_as_value_pairs={}
    if len(list_of_paths_to_files) != len(set(list_of_paths_to_files)):
        raise Exception("two files share a name space but contain diferent data they will both be copied but there is no way to asure their not coruped ")
    for file_path in list_of_paths_to_files:
        hashbrowns=sha256sum(file_path)
        dict_of_files_in_directory_as_key_hash_as_value_pairs[file_path]=hashbrowns
    if len(list_of_paths_to_files) != len(dict_of_files_in_directory_as_key_hash_as_value_pairs):
        raise Exception('somthing is deeply fucked in the directory_to_file_hash_pair_file funtion deeeeeeply fucked!!!!!! previos exseption should have been raied')
    return dict_of_files_in_directory_as_key_hash_as_value_pairs




def main():
    print(os.popen(' dpkg --get-selections | cut -f1').read())
    print(directory_to_file_hash_pair_dict('testing/homedirectoryfortesting'))




if __name__=="__main__":
    main()
