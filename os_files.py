import os
import time

path = r'C:\Users\Programmer\Documents\GitHub\Urban'

for root, dirs, files in os.walk(path):
    for file in files:
        filepath = os.path.join(root, file)
        file_time = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.abspath(filepath)
        print(f'File: {file}, filepath: {filepath}, file size: {file_size} bites, '
              f'parent dir: {parent_dir}, last change: {formatted_time}')









