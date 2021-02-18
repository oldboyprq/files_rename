import os

path = os.getcwd()
name = input("修改前:")
rename = input("修改后:")
for filename in os.listdir(path):
    if name in filename:
        new_name = filename.replace(name, rename)
        os.rename(filename, new_name)
    else:
        pass
