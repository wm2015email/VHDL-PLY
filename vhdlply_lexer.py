######################################################
# Attempting to make a VHDL lexer using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

import ply.lex as lex

# List of token names including the keywords
tokens = [
    'BASE_LITERAL',
    'BIT_STRING_LITERAL_BINARY',
    'BIT_STRING_LITERAL_OCTAL',
    'BIT_STRING_LITERAL_HEX',
    'REAL_LITERAL',
    'BASIC_IDENTIFIER',
    'EXTENDED_IDENTIFIER',
    'COMMENT',
    'TAB',
#    'SPACE',
    'NEWLINE',
    'CR',
    'CHARACTER_LITERAL',
    'STRING_LITERAL',
    'OTHER_SPECIAL_CHARACTER',
    'DOUBLESTAR',
    'ASSIGN',
    'LE',
    'GE',
    'ARROW',
    'NEQ',
    'VARASGN',
    'BOX',
    'DBLQUOTE',
    'SEMI',
    'COMMA',
    'AMPERSAND',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'MUL',
    'DIV',
    'PLUS',
    'MINUS',
    'LOWERTHAN',
    'GREATERTHAN',
    'EQ',
    'BAR',
    'DOT',
    'BACKSLASH',
    'EXPONENT',
    'HEXDIGIT',
    'INTEGER',
    'DIGIT',
    'BASED_INTEGER',
    'EXTENDED_DIGIT',
    'APOSTROPHE'
] + [
    'ABS', 'ACCESS', 'ACROSS', 'AFTER', 'ALIAS', 'ALL', 'AND', 'ARCHITECTURE',
    'ARRAY', 'ASSERT', 'ATTRIBUTE', 'BEGIN', 'BLOCK', 'BODY', 'BREAK', 'BUFFER',
    'BUS', 'CASE', 'COMPONENT', 'CONFIGURATION', 'CONSTANT', 'DISCONNECT', 'DOWNTO',
    'END', 'ENTITY', 'ELSE', 'ELSIF', 'EXIT', 'FILE', 'FOR', 'FUNCTION', 'GENERATE',
    'GENERIC', 'GROUP', 'GUARDED', 'IF', 'IMPURE', 'INERTIAL', 'INOUT', 'IN', 'IS',
    'LABEL', 'LIBRARY', 'LIMIT', 'LINKAGE', 'LITERAL', 'LOOP', 'MAP', 'MOD', 'NAND',
    'NATURE', 'NEW', 'NEXT', 'NOISE', 'NOR', 'NOT', 'NULL_', 'OF', 'ON', 'OPEN', 'OR',
    'OTHERS', 'OUT', 'PACKAGE', 'PORT', 'POSTPONED', 'PROCESS', 'PROCEDURE',
    'PROCEDURAL', 'PURE', 'QUANTITY', 'RANGE', 'REVERSE_RANGE', 'REJECT', 'REM',
    'RECORD', 'REFERENCE', 'REGISTER', 'REPORT', 'RETURN', 'ROL', 'ROR', 'SELECT',
    'SEVERITY', 'SHARED', 'SIGNAL', 'SLA', 'SLL', 'SPECTRUM', 'SRA', 'SRL', 'SUBNATURE',
    'SUBTYPE', 'TERMINAL', 'THEN', 'THROUGH', 'TOLERANCE', 'TO',  'TRANSPORT', 'TYPE',
    'UNAFFECTED', 'UNITS', 'UNTIL', 'USE', 'VARIABLE', 'WAIT', 'WITH', 'WHEN', 'WHILE',
    'XNOR', 'XOR'
]

# Define the regular expressions for the tokens
t_BASE_LITERAL = r'(\d+)[#](\w+)(\.\w+)?[#]([eE][+\-]?\d+)?'
t_BIT_STRING_LITERAL_BINARY = r'B"([01_]+)"'
t_BIT_STRING_LITERAL_OCTAL = r'O"([0-7_]+)"'
t_BIT_STRING_LITERAL_HEX = r'X"([0-9A-F_]+)"'
t_REAL_LITERAL = r'(\d+)\.(\d+)([eE][+\-]?\d+)?'
t_BASIC_IDENTIFIER = r'[A-Z]([A-Z0-9_]*[A-Z0-9])*'
t_EXTENDED_IDENTIFIER = r'\\([\w&\'()+,./:;<=| \[\]@#-]+)\\'
t_COMMENT = r'--[^\n]*'
t_TAB = r'\t+'
#t_SPACE = r' +'
t_NEWLINE = r'\n'
t_CR = r'\r'
t_CHARACTER_LITERAL = r"'.'"
t_STRING_LITERAL = r'"([^"\n\r]|"")*"'
t_OTHER_SPECIAL_CHARACTER = r'[!$%@?^`{}~ \u00A4\u00A6\u00A7\u00A9\u00AB\u00AC\u00AD\u00AE\u00B0\u00B1\u00B5\u00B6\u00B7\u2116\u00BB\u0400-\u045E]'
t_DOUBLESTAR = r'\*\*'
t_ASSIGN = r'=='
t_LE = r'<='
t_GE = r'>='
t_ARROW = r'=>'
t_NEQ = r'/='
t_VARASGN = r':='
t_BOX = r'<>'
t_DBLQUOTE = r'"'
t_SEMI = r';'
t_COMMA = r','
t_AMPERSAND = r'&'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
t_MUL = r'\*'
t_DIV = r'/'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LOWERTHAN = r'<'
t_GREATERTHAN = r'>'
t_EQ = r'='
t_BAR = r'\|'
t_DOT = r'\.'
t_BACKSLASH = r'\\'
t_EXPONENT = r'[eE][+\-]?\d+'
t_HEXDIGIT = r'[A-F]'
t_INTEGER = r'\d+(_?\d+)*'
t_DIGIT = r'\d'
t_BASED_INTEGER = r'[0-9A-Z](_?[0-9A-Z])*'
t_EXTENDED_DIGIT = r'[0-9A-Z]'
t_APOSTROPHE = r"'"


# Ignored characters
t_ignore = ' \t\r'

# Define a rule for newlines (which is ignored)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule for keywords (case-insensitive)
def t_KEYWORD(t):
    r'(?i)ABS|ACCESS|ACROSS|AFTER|ALIAS|ALL|AND|ARCHITECTURE|ARRAY|ASSERT|ATTRIBUTE|BEGIN|BLOCK|BODY|BREAK|BUFFER|BUS|CASE|COMPONENT|CONFIGURATION|CONSTANT|DISCONNECT|DOWNTO|END|ENTITY|ELSE|ELSIF|EXIT|FILE|FOR|FUNCTION|GENERATE|GENERIC|GROUP|GUARDED|IF|IMPURE|INERTIAL|INOUT|IN|IS|LABEL|LIBRARY|LIMIT|LINKAGE|LITERAL|LOOP|MAP|MOD|NAND|NATURE|NEW|NEXT|NOISE|NOR|NOT|NULL_|OF|ON|OPEN|OR|OTHERS|OUT|PACKAGE|PORT|POSTPONED|PROCESS|PROCEDURE|PROCEDURAL|PURE|QUANTITY|RANGE|REVERSE_RANGE|REJECT|REM|RECORD|REFERENCE|REGISTER|REPORT|RETURN|ROL|ROR|SELECT|SEVERITY|SHARED|SIGNAL|SLA|SLL|SPECTRUM|SRA|SRL|SUBNATURE|SUBTYPE|TERMINAL|THEN|THROUGH|TOLERANCE|TO|TRANSPORT|TYPE|UNAFFECTED|UNITS|UNTIL|USE|VARIABLE|WAIT|WITH|WHEN|WHILE|XNOR|XOR'
    t.type = t.value.upper()
    return t

# Define an error rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
-- This is a comment
A123 32#3A.B3#E-4
B"1010_1011"
O"12_3456"
X"AB_CD_EF"
42.0E+3
BASIC_IDENTIFIER
\\Extended_Identifier\\

-- This is a comment
abs ACCESS AcRoSs After alias All and Architecture
array ASSERT ATTRIBUTE BEGIN BLOCK BODY BREAK BUFFER
bus case component CONFIGURATION CONSTANT DISCONNECT
downto END entity ELSE elsif EXIT file FOR function
generate GENERIC group GUARDED if impure IN inertial
inout is LABEL library LIMIT linkage literal loop MAP
MOD nand NATURE new NEXT noise NOR not NULL_ of on OPEN
or OTHERS out PACKAGE port POSTPONED process PROCEDURE
PROCEDURAL pure QUANTITY range REVERSE_RANGE reject REM
record REFERENCE register REPORT return ROL ROR select
SEVERITY shared SIGNAL SLA SLL spectrum SRA SRL subnature
subtype TERMINAL then THROUGH to TOLERANCE TRANSPORT type
UNAFFECTED units UNTIL use VARIABLE wait WITH when WHILE
xnor XOR
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
