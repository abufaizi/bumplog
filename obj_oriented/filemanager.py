from treelib import Tree, Node
import os

import log
import FM

class tree():
    def __init__():
        ftree = tree()
        ftree.create_node('General', 'general')

        def new_directory(name):
            cwd = os.getcwd()
            mkdir(name)
            change_dir(name)
            ftree.create_node(name, name, parent=cwd)

        def change_dir(name):
                os.chdir(name)

        def new_file(file_name):
            # get the current script path.
            here = os.path.dirname(os.path.realpath(__file__))
            filepath = os.path.join(here, filename)
            # create an empty file.
            try:
                f = open(filepath, 'w')
                f.close()
            except IOError:
                print "Wrong path provided"
            ftree.create_node(file_name, file_name, data=log(filepath + "/" + file_name, 0), parent=os.getcwd())
