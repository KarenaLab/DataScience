
# Libraries
import os
import sys
import shutil


def files_list(path=None):
    """
    Returns a list with only file(s) (remove folder(s)) from given path
    or the current path.
    
    """
    if(path != None):
        path_comeback = os.getcwd()
        os.chdir(path)

    content = os.listdir()
    
    files_list = []
    for f in content:
        if(os.path.isfile(f) == True):
            files_list.append(f)

    if(path != None):
        os.chdir(path_comeback)
        

    return files_list


def folders_list(path=None):
    """
    Returns a list with only folder(s) (remove file(s)) from given path
    or the current path.
    
    """
    if(path != None):
        path_comeback = os.getcwd()
        os.chdir(path)

    content = os.listdir()
    
    folders_list = []
    for f in content:
        if(os.path.isdir(f) == True):
            folders_list.append(f)

    if(path != None):
        os.chdir(path_comeback)
        

    return folders_list


def filter_by_extension(files_list, files_type):
    """
    Receives a **list with file(s)** from project source
    and a **list with extension(s)** allowed to copy for github destiny.
    Returns a list with files to copy/compare between project source and
    github destiny.

    enable_types is a string with the extensions, need to handle it.

    """
    # Select file extension(s) to keep (files_type)
    _files_type = []
    for i in files_type:
        extension = i
        extension = i.replace(".", "")

        _files_type.append(extension)

    files_type = _files_type[:]

    # Select files with extensions enabled
    new_list = []
    for f in file_list:
        name, extension = f.split(".")
        if(enable_types.count(extension) == 1):
            new_list.append(f)


    return new_list    


