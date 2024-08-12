######################################################
# Testing VHDL paser using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

from vhdlply_lexer import lexer
from vhdlply_yacc  import parser

# Test cases
test_cases = [
    '''
    Library ieee;
    USE ieee.std_logic_vector.all;
    
    ENTITY MyEntity is
        port(
            clk : in std_logic;
            rst : in std_logic
        );
    end MyEntity;
    ''',
    '''
    entity AnotherEntity is
        port(
            a : in std_logic;
            b : out std_logic;
            c : inout std_logic
        );
    end AnotherEntity;
    ''',
    '''
    entity EmptyEntity is
    end EmptyEntity;
    '''
]

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
        
        
# Function to process each test case
def process_test_case(i, data):
    print_test(i, data)
    print(f"\n-> parse") 
    # Reset Lexer State between files
    lexer.file   = f"noname{i}.vhdl"
    lexer.lineno = 1
    lexer.input('')
    result = parser.parse(data,lexer=lexer,tracking=True)
    print("\nResult:", result)
    print("\n" + "="*80 + "\n")
    print_tree(result)
    
# Function to test the parser
def test_parser(test_cases):
    process_test_case(1, test_cases[0])
    #for i, data in enumerate(test_cases, 1):
    #    process_test_case(i, data)                                 
    

# Run the tests
print("START")
test_parser(test_cases)
print("END")

