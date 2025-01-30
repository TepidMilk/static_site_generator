import os
import shutil

#This function recursively copies files from source dir to destination dir
def copy_dir_to(source, destination):
    if not os.path.exists(source):
        raise Exception
    if os.path.isfile(source):
        return shutil.copy(source, destination)
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for file in os.listdir(source):
        log = copy_dir_to(os.path.join(source, file), os.path.join(destination, file))