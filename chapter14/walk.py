import os
from os.path import join, getsize



print(os.walk('C:\think_python\think_python\chapter14\walk.py'))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk('C:\think_python\think_python\chapter14\walk.py')
