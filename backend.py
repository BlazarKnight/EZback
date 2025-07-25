'''
this is a library of functions for backend manegement
'''

from dataclasses import dataclass
import json
import os
from glob import glob
import hashlib
import shutil

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

def get_dir_size(directory:str):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def free_space_of_place(directory:str):
    stats = shutil.disk_usage(directory)
    return stats.free

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





#todo desine some siple vesion manegment system

def sha256sum(filename):
    list_of_failed_files=[]
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    try:
        with open(filename, 'rb', buffering=0) as f:
            while n := f.readinto(mv):
                h.update(mv[:n])
    except:
        list_of_failed_files.append(filename)
        pass
    print(list_of_failed_files)
    return h.hexdigest()

def directory_to_filelist(directory:str):
    list_of_paths_to_files=[]
    walk_of_directory =list( os.walk(directory))
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:

            list_of_paths_to_files.append(os.path.join(dirpath, f))
    return list_of_paths_to_files

def copy_directory_of_path1_to_path2(copy_from_path,copy_to_path,*,makeEZdir=False):
#    print( bool(get_dir_size(copy_from_path) < free_space_of_place(copy_to_path)))
    if bool(get_dir_size(copy_from_path) < free_space_of_place(copy_to_path)):
        if makeEZdir:
            shutil.copytree(copy_from_path, copy_to_path+'EZback/',dirs_exist_ok=True)

        else:
            shutil.copytree(copy_from_path, copy_to_path,dirs_exist_ok=True)


    else:
        print(bool( get_dir_size(copy_from_path) < free_space_of_place(copy_to_path)))
        print("Space error the directory is to big 109")
        raise "Space error the directory is to big 109"
        return "Space error the directory is to big 109"


    return 0


def directory_to_file_hash_pair_dict(directory:str): #this needs legacy pairady at all times!!!!!!!!!!!!!!!!!!!!!!1
    list_of_paths_to_files = directory_to_filelist(directory)
    dict_of_files_in_directory_as_key_hash_as_value_pairs={}
    if len(list_of_paths_to_files) != len(set(list_of_paths_to_files)):
        raise Exception("two files share a name space but contain diferent data they will both be copied but there is no way to asure their not coruped ")
    for file_path in list_of_paths_to_files:
        hashbrowns=sha256sum(file_path)
        dict_of_files_in_directory_as_key_hash_as_value_pairs[file_path]=hashbrowns
    if len(list_of_paths_to_files) != len(dict_of_files_in_directory_as_key_hash_as_value_pairs):
        raise Exception('somthing is deeply fucked in the directory_to_file_hash_pair_file funtion deeeeeeply fucked!!!!!! previos exseptions should have been raied')
    return dict_of_files_in_directory_as_key_hash_as_value_pairs

def dict_to_json(diton:dict,save_path):
    # this is a genaric dict to json fuction this will not write .EZback files
    file_path= save_path+'hash_file_pair.json'

    try:
        file = open(file_path, "x")

    except:
        file = open(file_path, "w")
    json.dump(diton,file)


    return 0

def dict_to_EZback(diton:dict,save_path):
    file_path= save_path+'hash_file_pair.json'

    try:
        file = open(file_path, "x")

    except:
        file = open(file_path, "w")
    json.dump(diton,file)

    # Source file path
    source = file_path

    # destination file path
    dest = save_path+'hash_file_pair.EZback'

    # Now rename the source path
    # to destination path
    # using os.rename() method
    os.rename(source, dest)
    return 0

def backup_EZback_file_compere_to_cuent_file_state(backup_json_file:str,home_directory_as_hash_file_pair_dict):

    with open(backup_json_file, "r") as file:
        contents = json.load(file)
    if contents == home_directory_as_hash_file_pair_dict:
        return(False,[]) #(was there any change?,list of changed files)
    if contents != home_directory_as_hash_file_pair_dict:
        changed_files_as_set = set(contents.values()) ^ set(home_directory_as_hash_file_pair_dict.values())
        changed_files_as_list= list(changed_files_as_set)
        return (True,changed_files_as_list,)#(was there any change?,list of changed files)

def create_new_backup(save_to_path, directory_to_be_backed_up):
    try:
        copy_directory_of_path1_to_path2(directory_to_be_backed_up, save_to_path,makeEZdir=True)
        dict_to_EZback(directory_to_file_hash_pair_dict(save_to_path + 'EZback/'), save_to_path + 'EZback/')
    except:
        print(copy_directory_of_path1_to_path2(directory_to_be_backed_up, save_to_path,makeEZdir=True))
        print("Space error the directory is to big 177")

        return 'error'
    finally:

        return 0
def find_EZback_file_in_directory(path,ret_path_to_dir=True):
    for root, dirs, files in os.walk(path):
        if 'hash_file_pair.EZback' in files:
            if ret_path_to_dir:
                return root+'/'
            else:
                return os.path.join(root,'hash_file_pair.EZback')

def main():
    def make_randomfile(path):
        import secrets as sec
        the_tropo = sec.token_urlsafe(7)
        file_path = path + 'IF-A-USER-SEES-THIS-THAN-SOMETHING-BAD-HAS-HAPPEND'+the_tropo+".wtf"

        try:
            file = open(file_path, "x")

        except:
            file = open(file_path, "w")
        file.write(sec.token_urlsafe(sec.randbelow(5000)))


        return 0
    external_drive_path= '/home/the-game/EZback/testing/homedirectoryfortesting/'
    internal_save_path= "/home/the-game/EZback/testing/homedirectoryfortesting/"
    #print(backup_json_compere_to_cuent_file_state("testing/place for test jsons/hash_file_pair.json",directory_to_file_hash_pair_dict("/home/the-game/EZback/testing")))

    #print(free_space_of_place("/home/the-game/EZback/testing/homedirectoryfortesting/"))
    #print(get_dir_size("/home/the-game/EZback/testing/homedirectoryfortesting/"))
    create_new_backup( external_drive_path,"/home/the-game/EZback/testing/homedirectoryfortesting/")
    print(create_new_backup( external_drive_path,"/home/the-game/EZback/testing/homedirectoryfortesting/"))
    print(get_dir_size('/home/the-game/EZback/testing/homedirectoryfortesting'))
    print(free_space_of_place(external_drive_path))
    #make_randomfile(internal_save_path)
    #make_randomfile(internal_save_path)
    print(backup_EZback_file_compere_to_cuent_file_state(find_EZback_file_in_directory(external_drive_path,ret_path_to_dir=False),directory_to_file_hash_pair_dict(internal_save_path)))


    #print(find_EZback_file_in_directory(external_drive_path,ret_path_to_dir=False))


if __name__=="__main__":
    main()
