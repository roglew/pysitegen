#!/usr/bin/python

import os
import glob
import shutil
from jinja2 import Environment, FileSystemLoader

def create_dir(directory):
    if directory == '':
        return
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def directory_files(directory, source_path):
    files = []
    for dir_name, subdir_list, file_list in os.walk(directory):
        for f in file_list:
            files.append(os.path.relpath(os.path.join(dir_name, f), source_path))
    return files

def build_site(build_dir=None, source_dir=None, include_list=[]):
    build_dir = build_dir or '_site'
    source_dir = source_dir or '_source'

    files = set()
    # Strip filenames
    for i in include_list:
        files.add(i.rstrip())
    
    # Expand directories
    new_files = set()
    for i in files:
        if os.path.isdir(os.path.join(source_dir, i)):
            for f in directory_files(os.path.join(source_dir, i), source_dir):
                new_files.add(f)
        else:
            new_files.add(i)
    files = new_files

    files = [f.rstrip() for f in files]

    create_dir(build_dir)
    
    loader = FileSystemLoader(source_dir)
    env = Environment(loader=loader)

    for fname in files:
        fname = fname.strip()
        create_dir(os.path.join(build_dir, os.path.dirname(fname)))
        base, ext = os.path.splitext(fname)
        if ext == '.html' or ext == '.htm':
            print 'Rendering %s...' % fname
            template = env.get_template(fname)
            with open(os.path.join(build_dir, fname), 'w') as f:
                f.write(template.render())
        else:
            print 'Copying %s...' % fname
            shutil.copyfile(os.path.join(source_dir, fname), os.path.join(build_dir, fname))

def main():
    with open('buildlist.txt', 'r') as f:
        files = f.readlines()
    build_site(include_list=files)

if __name__ == '__main__':
    main()
