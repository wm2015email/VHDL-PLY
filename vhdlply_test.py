#!/usr/bin/python3

######################################################
# Testing VHDL paser using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

from vhdlply_lexer import lexer
from vhdlply_yacc  import parser

# Test cases

debug_printtree   = False
debug_printresult = False


def print_test(i, input):
    print(f"\n=> Test Case {i}:")
    
    lines = input.splitlines()
    for i, line in enumerate(lines, start=1):
        print(f"{i:<3}: {line}")
        

def print_tree(data, indent=0):
    if isinstance(data, list):
        for item in data:
            print_tree(item, indent + 2)
    else:
        print(' ' * indent + str(data))
        
        
def get_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found")
        return None
 
            
# Function to process each test case
def process_test_case(file_path):
    global log
    data = get_file(file_path);
    print_test(file_path, data)
    print(f"\n-> parse") 
    # Reset Lexer State between files
    lexer.file   = file_path
    lexer.lineno = 1
    lexer.input('')
    result = parser.parse(data,lexer=lexer,tracking=True,debug=log)
    
    if debug_printresult:
        print("\nResult:", result)
        print("\n" + "="*80 + "\n")
        
    if debug_printtree: print_tree(result)    

# Run the tests
print("START")

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()


#process_test_case("test_001.vhd")
#process_test_case("test_002.vhd")
#process_test_case("test_003.vhd")
process_test_case("test_005.vhd")

print("\n-> finished\n")

