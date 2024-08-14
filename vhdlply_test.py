#!/usr/bin/python3

######################################################
# Testing VHDL paser using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

import vhdlply_yacc
import vhdlply_lexer

#-----------------------------------
# Parameters: Debug Flags
#-----------------------------------
debug_lex              = False
vhdlply_yacc.debug_def = False
debug_printtree        = False
debug_printresult      = False
debug_file             = False

#-----------------------------------
# Parameters: Testcases to Run
#-----------------------------------
testcases = [
## STARTING_RULE          FILE
   ["design_file",        "test_001.vhd"],                  # Good: 1 entity
   ["design_file",        "test_005.vhd"],                  # Good: 4 entities and 4 empty arches
   #["design_file",       "test_002.vhd"],                  # Bad: 4 entities, 4 archs, 4 components, 4 component-instances
   #["design_file",       "test_003.vhd"],                  # Bad: 4 entities and 4 arch with 4 component-instances
   #["association_list",  "test_association_list__00.vhd"], # Bad: Ports of component-instance
]


#-----------------------------------
# Script Body
#-----------------------------------
if debug_lex:
    vhdlply_lexer.lexer_test1()
    exit(1);


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
def process_test_case(test_params):
    global debug_def
    
    start     = test_params[0]
    file_path = test_params[1]
    
    data = get_file(f"testsuite/{file_path}");
    if debug_file: print_test(file_path, data)
    
    print(f"\n-> parse: file:{file_path}  start:{start}\n") 
    
    # Reset Lexer State between files
    vhdlply_lexer.lexer.file   = file_path
    vhdlply_lexer.lexer.lineno = 1
    vhdlply_lexer.lexer.input('')
    vhdlply_yacc.new_parser(start)
    
    result = vhdlply_yacc.parser.parse(data,lexer=vhdlply_lexer.lexer,tracking=True, debug=vhdlply_yacc.log)
    
    if debug_printresult:
        print("\nResult:", result)
        print("\n" + "="*80 + "\n")
        
    if debug_printtree: print_tree(result)    



for test_params in testcases:
    process_test_case(test_params)
    

print("\n-> finished\n")

