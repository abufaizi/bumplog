
# File Manager (FM)
#   For reading from, writing, or appending to data files


# Local Modules
import LP

# NonLocal Modules
import os


def get_all(nfile):
    #Returns all values in data file,
    with open(nfile + '.txt', 'r') as f:
        objects = f.readlines()
        for i in range(0, len(objects)):
            objects[i] = objects[i][:-1]
        return objects

def get_substring(nfile, index):
    with open(nfile + '.txt', 'r') as f:
        content = f.readlines()
        return content[index][:-1]

def get_index(nfile, substring):
    with open(nfile + '.txt', 'r') as f:
        content = f.readlines()
        for i in range(0, len(content)):
            if substring == content[i]:
                return i
        return -1

def append_substring(nfile, substring):
    with open(nfile + '.txt', 'a') as f:
        f.write(substring)

def edit_substring(nfile, index, substring):
    with open(nfile + '.txt', 'r') as rf:
        entire = rf.read()
        start, end = LP.index_position(entire, index)
        with open(nfile + '.txt', 'w') as wf:
            wf.write(entire[:start] + str(substring) + entire[end:])


# New


def change_directory(ndirectory):
    os.chdir(ndirectory)

def list_all():
    names = []
    for name in os.listdir('.'):
        names.append(name)
    return names

def list_directories():
    #With respect to current directory, returns
    #a list of all subdirectories
    directories = []
    for name in os.listdir('.'):
        if os.path.isdir(name):
            directories.append(name)
    return directories

def list_files():
    files = []
    for name in os.listdir('.'):
        if os.path.isfile(name):
            files.append(name)
    return files

def index_length(nfile):
   with open(nfile + '.txt', 'r') as f:
       return len(f.readlines())


# Copyright 2017 Neil Graham


'''
# File Format

classes
    general.txt
        file,index,bumps
    programming.txt

logs
    1.txt
        holds 100 logs
    2.txt
        There is enormous value in exploiting common misconceptions.
    3.txt
        I don’t believe there can ever be anything more complex than reality


'''
