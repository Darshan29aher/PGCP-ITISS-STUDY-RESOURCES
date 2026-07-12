"""
1 To find out Current directory of a file
2 To find out all folders & files inside given folder.
3 To find out absolute path and relative path.
4 To check if a file or folder exists or not.
5 To create/remove a Directory.
6 To check the permissions of given folder
7 To check the permissions of given file
8 Take file name from command line
"""

import os

print("Path at terminal when executing this file (Current working directory)")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("From full path get directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

print("To check if a file or folder exists or not.")
# full_path = input("Enter directory/file path to check")
print("Exists ::",os.path.exists(full_path))
print("File ::", os.path.isfile(full_path))
print("Dir ::", os.path.isdir(full_path))

print("Remove an empty directory")
# full_dir_path = input("Enter directory (empty) to be deleted")
# os.rmdir(full_dir_path) #removes an empty directory.

print("Remove a file")
# full_file_path = input("Enter file (empty) to be deleted")
# os.remove(full_file_path)# removes a file.


"""
6 To check the permissions of given folder
7 To check the permissions of given file
"""
import os
import stat
print("Permissions of day8 folder")
st = os.stat("C:/Python_codes/day8")
print(oct(st.st_mode))#rwxrwxrwx
st = os.stat("C:/Python_codes/day8/folder_directory_operations.py")
print(oct(st.st_mode))#rw-rw-rw-

################################################
# Accepting input from command line
import sys
print("List of all parameters ::", sys.argv)
Print("ALL Inputs come as a string")
for arg in sys.argv:
    print(arg)
