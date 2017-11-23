
# File Manager (FM)
#   For reading from, writing, or appending to data files


# Local Modules
import LP

def get_all(filename):
    #Returns all values in data file,
    with open(filename + '.txt', 'r') as f:
        return f.readlines()

def get_substring(filename, index):
    with open(filename + '.txt', 'r') as f:
        content = f.readlines()
        return content[index]

def get_index(filename, substring):
    with open(filename + '.txt', 'r') as f:
        content = f.readlines()
        for i in range(0, len(content)):
            if substring == content[i]:
                return i
        return -1

def append_substring(filename, substring):
    with open(filename + '.txt', 'a') as f:
        f.write(substring)

def edit_substring(filename, index, substring):
    with open(filename + '.txt', 'r') as rf:
        entire = rf.read()
        start, end = lp.index_position(entire, index)
        with open(filename + '.txt', 'w') as wf:
            wf.write(entire[:start] + substring + entire[end:])


# Copyright 2017 Neil Graham
