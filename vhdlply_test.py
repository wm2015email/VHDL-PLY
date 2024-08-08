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

# Function to process each test case
def process_test_case(i, data):
    print(f"\n=> Test Case {i}:")
    print(data)
    print(f"\n-> parse") 
    result = parser.parse(data)
    print("Result:", result)
    print("\n" + "="*80 + "\n")

# Function to test the parser
def test_parser(test_cases):
    process_test_case(1, test_cases[0])
    #for i, data in enumerate(test_cases, 1):
    #    process_test_case(i, data)                                 
    

# Run the tests
print("START")
test_parser(test_cases)
print("END")

