# Traverse a given directory using BFS
import os

def dfs(path,depth=0):
    indent = ' ' * depth
    if os.path.isdir(path):
        print(f'{indent}{os.path.basename(path)}/')
        for fname in os.listdir(path):
            fpath = os.path.join(path,fname)
            dfs(fpath, depth+1)
    else:
        print(f'{indent}{os.path.basename(path)}')

pardir = os.path.dirname(os.getcwd())
dfs(pardir)
