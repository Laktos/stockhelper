import os
import sys
from osascript import osascript
#Indenterar rader
def main(args):
    file_name = str
    file_name = osascript('/Users/albinjonfelt/Documents/programmering/aktier/scripts/return_any_file.scpt')
    first_row_to_indent = int(input('Input first row to indent in the form: 12\nInput: '))
    last_row_to_indent = int(input('Input last row to indent in the form: 42\nInput: '))
    
    all_lines = list()
    with open(file_name[1], 'r') as f: 
        full_file = f.readlines()
        for i in range (0, len(full_file)):
            if(i >= first_row_to_indent - 1  and i <= last_row_to_indent - 1):
                all_lines.append('\t' + full_file[i])
            else: 
                all_lines.append(full_file[i])
    f.close()
    with open(file_name[1], 'w') as f:
        f.writelines(all_lines)
    f.close()
    

if __name__ == "__main__":
   main(sys.argv[1:])
