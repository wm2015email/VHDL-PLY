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
    'EXTENDED_IDENTIFIER',
    'CHARACTER_LITERAL',
    'STRING_LITERAL',
    'BASIC_IDENTIFIER',
    'COMMENT',
    'WHITESPACE',
    'NEWLINE',
    'CR',
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

def get_colpos(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    

def get_rowpos(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return line_start + 1

# Order of Token matching is as follows:
#   1. Def's in order they are defined
#   2. after all def's are matched then string rules are matched
#      except string matches give preceedence to the longest string first.

def t_cr(t):
    r'[\r]+'
    pass

def t_COMMENT(t):
    r'--[^\n]*'
    # pass means skip this token
    pass

# Define a rule for newlines (which is ignored)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CHARACTER_LITERAL(t):
    r"'.'"
    return t

def t_STRING_LITERAL(t):
    r'"([^"\n\r]|"")*"'
    return t

def t_whitespace(t):
    r'[ \t]+'
    pass

    
## Define a rule for keywords (case-insensitive)
#def t_KEYWORD(t):
#    r'(?i)ABS|ACCESS|ACROSS|AFTER|ALIAS|ALL|AND|ARCHITECTURE|ARRAY|ASSERT|ATTRIBUTE|BEGIN|BLOCK|BODY|BREAK|BUFFER|BUS|CASE|COMPONENT|CONFIGURATION|CONSTANT|DISCONNECT|DOWNTO|END|ENTITY|ELSE|ELSIF|EXIT|FILE|FOR|FUNCTION|GENERATE|GENERIC|GROUP|GUARDED|IF|IMPURE|INERTIAL|INOUT|IN|IS|LABEL|LIBRARY|LIMIT|LINKAGE|LITERAL|LOOP|MAP|MOD|NAND|NATURE|NEW|NEXT|NOISE|NOR|NOT|NULL_|OF|ON|OPEN|OR|OTHERS|OUT|PACKAGE|PORT|POSTPONED|PROCESS|PROCEDURE|PROCEDURAL|PURE|QUANTITY|RANGE|REVERSE_RANGE|REJECT|REM|RECORD|REFERENCE|REGISTER|REPORT|RETURN|ROL|ROR|SELECT|SEVERITY|SHARED|SIGNAL|SLA|SLL|SPECTRUM|SRA|SRL|SUBNATURE|SUBTYPE|TERMINAL|THEN|THROUGH|TOLERANCE|TO|TRANSPORT|TYPE|UNAFFECTED|UNITS|UNTIL|USE|VARIABLE|WAIT|WITH|WHEN|WHILE|XNOR|XOR'
#    # This reassigns type from KEYWORD to the Matched value. 
#    t.type = t.value.upper()
#    t.lineno = t.lexer.lineno
#    t.lexpos = t.lexer.lexpos
#    return t


# Define the regular expressions for the tokens
def t_BASE_LITERAL(t):
    r'(\d+)[#](\w+)(\.\w+)?[#]([eE][+\-]?\d+)?'
    return t

def t_BIT_STRING_LITERAL_BINARY(t):
    r'B"([01_]+)"'
    return t

def t_BIT_STRING_LITERAL_OCTAL(t):
    r'O"([0-7_]+)"'
    return t

def t_BIT_STRING_LITERAL_HEX(t):
    r'X"([0-9A-F_]+)"'
    return t

def t_REAL_LITERAL(t):
    r'(\d+)\.(\d+)([eE][+\-]?\d+)?'
    return t

def t_EXTENDED_IDENTIFIER(t):
    r'\\([\w&\'()+,./:;<=| \[\]@#-]+)\\'
    return t


def t_EXPONENT(t):
    r'[eE][+\-]?\d+'
    return t

#def t_HEXDIGIT(t):
#    r'[A-F]'
#    return t

#def t_INTEGER(t):
#    r'\d+(_?\d+)*'
#    return t

#def t_DIGIT(t):
#    r'\d'
#    return t

#def t_BASED_INTEGER(t):
#    r'[0-9A-Z](_?[0-9A-Z])*'
#    return t

#def t_EXTENDED_DIGIT(t):
#    r'[0-9A-Z]'
#    return t

#def t_BASIC_IDENTIFIER(t):
#    r'[A-Z]([A-Z0-9_]*[A-Z0-9])*'
#    return t

# Define keywords as a global variable
keywords = {
    "ABS", "ACCESS", "ACROSS", "AFTER", "ALIAS", "ALL", "AND", "ARCHITECTURE", "ARRAY", "ASSERT", "ATTRIBUTE",
    "BEGIN", "BLOCK", "BODY", "BREAK", "BUFFER", "BUS", "CASE", "COMPONENT", "CONFIGURATION", "CONSTANT",
    "DISCONNECT", "DOWNTO", "END", "ENTITY", "ELSE", "ELSIF", "EXIT", "FILE", "FOR", "FUNCTION", "GENERATE",
    "GENERIC", "GROUP", "GUARDED", "IF", "IMPURE", "INERTIAL", "INOUT", "IN", "IS", "LABEL", "LIBRARY", "LIMIT",
    "LINKAGE", "LITERAL", "LOOP", "MAP", "MOD", "NAND", "NATURE", "NEW", "NEXT", "NOISE", "NOR", "NOT", "NULL",
    "OF", "ON", "OPEN", "OR", "OTHERS", "OUT", "PACKAGE", "PORT", "POSTPONED", "PROCESS", "PROCEDURE", 
    "PROCEDURAL", "PURE", "QUANTITY", "RANGE", "REVERSE_RANGE", "REJECT", "REM", "RECORD", "REFERENCE", 
    "REGISTER", "REPORT", "RETURN", "ROL", "ROR", "SELECT", "SEVERITY", "SHARED", "SIGNAL", "SLA", "SLL", 
    "SPECTRUM", "SRA", "SRL", "SUBNATURE", "SUBTYPE", "TERMINAL", "THEN", "THROUGH", "TOLERANCE", "TO", 
    "TRANSPORT", "TYPE", "UNAFFECTED", "UNITS", "UNTIL", "USE", "VARIABLE", "WAIT", "WITH", "WHEN", "WHILE", 
    "XNOR", "XOR"
}

# Define a rule for BASIC_IDENTIFIER and KEYWORDS combined
def t_BASIC_IDENTIFIER(t):
    r'\w+'
    if t.value.upper() in keywords:
        t.type = t.value.upper()  # Use the keyword as the token type
    return t



#t_BASE_LITERAL              = r'(\d+)[#](\w+)(\.\w+)?[#]([eE][+\-]?\d+)?'
#t_BIT_STRING_LITERAL_BINARY = r'B"([01_]+)"'
#t_BIT_STRING_LITERAL_OCTAL  = r'O"([0-7_]+)"'
#t_BIT_STRING_LITERAL_HEX    = r'X"([0-9A-F_]+)"'
#t_REAL_LITERAL              = r'(\d+)\.(\d+)([eE][+\-]?\d+)?'
#t_EXTENDED_IDENTIFIER       = r'\\([\w&\'()+,./:;<=| \[\]@#-]+)\\'
#t_CHARACTER_LITERAL         = r"'.'"
#t_STRING_LITERAL            = r'"([^"\n\r]|"")*"'
#t_EXPONENT                  = r'[eE][+\-]?\d+'
t_HEXDIGIT                  = r'[A-F]'
t_INTEGER                   = r'\d+(_?\d+)*'
t_DIGIT                     = r'\d'
t_BASED_INTEGER             = r'[0-9A-Z](_?[0-9A-Z])*'
t_EXTENDED_DIGIT            = r'[0-9A-Z]'
#t_BASIC_IDENTIFIER          = r'([A-Z0-9_])'



#t_COMMENT     = r'--[^\n]*'

t_DOUBLESTAR  = r'\*\*'
t_ASSIGN      = r'=='
t_LE          = r'<='
t_GE          = r'>='
t_ARROW       = r'=>'
t_NEQ         = r'/='
t_VARASGN     = r':='
t_BOX         = r'<>'
t_DBLQUOTE    = r'"'
t_SEMI        = r';'
t_COMMA       = r','
t_AMPERSAND   = r'&'
t_LPAREN      = r'\('
t_RPAREN      = r'\)'
t_LBRACKET    = r'\['
t_RBRACKET    = r'\]'
t_COLON       = r':'
t_MUL         = r'\*'
t_DIV         = r'/'
t_PLUS        = r'\+'
t_MINUS       = r'-'
t_LOWERTHAN   = r'<'
t_GREATERTHAN = r'>'
t_EQ          = r'='
t_BAR         = r'\|'
t_DOT         = r'\.'
t_BACKSLASH   = r'\\'
t_APOSTROPHE  = r"'"

    
#def t_TAB(t):
#    r'\t+'
#    pass
#    
#def t_SPACE(t):
#    r' +'
#    pass
#    
#def t_CR(t):
#    r'\r'
#    pass
    
#t_TAB = r'\t+'
#t_SPACE = r' +'
#t_NEWLINE = r'\n'
#t_CR = r'\r'
t_OTHER_SPECIAL_CHARACTER = r'[!$%@?^`{}~ \u00A4\u00A6\u00A7\u00A9\u00AB\u00AC\u00AD\u00AE\u00B0\u00B1\u00B5\u00B6\u00B7\u2116\u00BB\u0400-\u045E]'

# Ignored characters
#t_ignore = ' \t\r'



# Define an error rule
def t_error(t):
    # Note: lexer error shouldn't happen...
    colpos = get_colpos(t.lexer.lexdata, t)
    t.lexer.skip(1)
    print(f"LEXER ERROR: lineno:{t.lineno:<4} colpos:{colpos:<4} value:{t.value}")
    #print(f"Illegal lexer character '{t.value[0]}'")
    exit(-1)

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
    colpos = get_colpos(data, tok)
    print(f"TOKEN: lineno:{tok.lineno:<4} colpos:{colpos:<4} type:{tok.type:<30} value:{tok.value}")
    
