#This program reads in a text file and outputs the number of e's it contains.
#The program take the filename as an argument on the command line.
#Author : Prasanth Sukumar

import argparse
from pathlib import Path

parser = argparse.ArgumentParser() #ArgumentParser is used to get file path from command line (ref 1).  
parser.add_argument("file", type=Path)
args = parser.parse_args()

filename = args.file
with open (filename, 'rt', errors='ignore') as f: #errors ignore is used to ignore UnicodeDecodeError when the file contains other charactes e.g.€ 
    text = f.read().lower() # The file may contain both upper and lower e's. To count both, the file content is converted to lower case
    count = 0 #initiating the counter
    for char in text: #for loop to go through each charcter and if it is 'e' incriment the counter.
        if char == 'e':
            count += 1
print(count)


#References
# 1. https://stackoverflow.com/questions/14360389/getting-file-path-from-command-line-argument-in-python
# 2. https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character