

## PLY

### Overview

PLY (Python Lex-Yacc) is a tool for creating parsers and compilers in Python. It consists of two main components:

1. Lex (Lexical Analyzer):
   - Breaks down input text into tokens (smallest meaningful units)
   - You define token rules using regular expressions
   - Example: Identifying numbers, keywords, operators in a programming language

2. Yacc (Yet Another Compiler Compiler):
   - Takes tokens from Lex and applies grammar rules
   - You define grammar rules to describe the structure of your language
   - Helps build a parse tree or perform actions based on the input

Key Features:
- Pure Python implementation
- No separate code generation step
- Uses Python docstrings for specifying rules
- Provides error handling and debugging capabilities

Basic Usage:
1. Define tokens in your lexer
2. Write grammar rules in your parser
3. Use lex.lex() to create a lexer
4. Use yacc.yacc() to create a parser
5. Parse input with your created parser

PLY is useful for:
- Creating domain-specific languages
- Building interpreters or compilers
- Parsing configuration files or data formats

While PLY requires some understanding of parsing concepts, it's designed to be more accessible than traditional compiler construction tools, making it a good choice for Python developers needing parsing capabilities.

Would you like me to expand on any specific part of PLY or provide a simple example?

### Yacc Tut



Tutorial: Creating an Arithmetic Expression Parser with yacc.py

1. Setup
First, make sure you have PLY installed:

```
pip install ply
```

2. Create the Lexer (calc_lexer.py)
Before we use yacc, we need to define our tokens. Create a file named `calc_lexer.py`:

```python
import ply.lex as lex

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
```

3. Create the Parser (calc_parser.py)
Now, let's create our parser using yacc. Create a file named `calc_parser.py`:

```python
import ply.yacc as yacc
from calc_lexer import tokens

# Grammar rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test it out
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
```

4. Explanation of the Parser Code

- We import the tokens from our lexer.
- Each function defines a grammar rule. The docstring specifies the rule, and the function body defines what to do when the rule is matched.
- The p_expression_* functions handle addition and subtraction.
- The p_term_* functions handle multiplication and division.
- The p_factor_* functions handle numbers and parenthesized expressions.
- We use left recursion to establish operator precedence (multiplication/division before addition/subtraction).
- The p_error function is called when there's a syntax error.
- We create the parser with yacc.yacc().
- The while loop at the end allows us to interactively test our parser.

5. Running the Parser
Run the `calc_parser.py` file:

```
python calc_parser.py
```

You can now enter arithmetic expressions:

```
calc > 2 + 3
5
calc > 2 * (3 + 4)
14
calc > 10 / (2 + 3)
2.0
```

6. Additional Features
You can extend this parser to handle more operations, variables, or even functions. For example, to add exponentiation:

```python
# Add '^' to the token list in calc_lexer.py
tokens = (..., 'POWER', ...)

# Add this rule in calc_lexer.py
t_POWER   = r'\^'

# Add this rule in calc_parser.py
def p_factor_power(p):
    'factor : factor POWER factor'
    p[0] = p[1] ** p[3]
```

Remember to adjust your precedence rules accordingly.

This tutorial provides a basic introduction to using yacc.py. You can build upon this example to create more complex parsers for various applications, such as programming languages, configuration files, or domain-specific languages.





## Pseduocode

```
# Initialize the lexer and parser
function init_lexer():
    lexer = create_lexer()
    return lexer

function init_parser():
    parser = create_parser()
    return parser

# Tokenize the input string
function tokenize(input_str):
    tokens = lexer.tokenize(input_str)
    return tokens

# Shift a token onto the stack
function shift(token):
    stack.push(token)
    input.remove(token)

function reduction_rule_applies():
    # Factor <- NUMBER
    if stack.top_is(NUMBER):
        return "p_factor_num"
    
    # Term <- Factor
    elif stack.top_is(factor):
        return "p_term_factor"
    
    # Expression <- Term
    elif stack.top_is(term):
        return "p_expression_term"
        
    # Expression <- Expression PLUS Term
    elif stack.top_is(expression, PLUS, term):
        return "p_expression_plus"
        
    # Expression <- Expression MINUS Term
    elif stack.top_is(expression, MINUS, term):
        return "p_expression_minus"
        
    # Factor <- LPAREN Expression RPAREN
    elif stack.top_is(LPAREN, expression, RPAREN):
        return "p_factor_expr"
        
    # Term <- Term TIMES Factor
    elif stack.top_is(term, TIMES, factor):
        return "p_term_times"
        
    # Term <- Term DIVIDE Factor
    elif stack.top_is(term, DIVIDE, factor):
        return "p_term_div"
        
    # No applicable reduction rule
    else:
        return False  
        
# Helper function to check the top 
#   elements of the stack
function stack.top_is(elements):
    for i from 0 to length(elements)-1:
        if stack[-1 - i] is not elements[length(elements)-1 - i]:
            return False
    return True
    
# Apply a reduction rule
function reduce(rule):
  
    if rule == "p_factor_num":
        # factor <- NUMBER
        factor = stack.pop()
        stack.push(create_factor(factor))
        
    elif rule == "p_term_factor":
        # term <- factor
        term = stack.pop()
        stack.push(create_term(term))
        
    elif rule == "p_expression_term":
        # expression <- term
        expression = stack.pop()
        stack.push(create_expression(expression))
        
    elif rule == "p_expression_plus":
        # expression <- expression PLUS term
        term = stack.pop()
        plus = stack.pop()
        expression = stack.pop()
        stack.push(create_expression(expression, plus, term))
        
    elif rule == "p_expression_minus":
        # expression <- expression MINUS term
        term = stack.pop()
        minus = stack.pop()
        expression = stack.pop()
        stack.push(create_expression(expression, minus, term))
        
    elif rule == "p_factor_expr":
        # factor <- LPAREN expression RPAREN
        rparen = stack.pop()
        expression = stack.pop()
        lparen = stack.pop()
        stack.push(create_factor(expression))
        
    elif rule == "p_term_times":
        # term <- term TIMES factor
        factor = stack.pop()
        times = stack.pop()
        term = stack.pop()
        stack.push(create_term(term, times, factor))
        
    elif rule == "p_term_div":
        # term <- term DIVIDE factor
        factor = stack.pop()
        divide = stack.pop()
        term = stack.pop()
        stack.push(create_term(term, divide, factor))

# Get the current state of the stack
function get_stack():
    return stack

# Get the current input string
function get_input():
    return input

# Fully parse the input string
function parse(input_str):
    tokens = tokenize(input_str)
    
    while tokens is not empty:
        token = tokens[0]
        shift(token) #Shift a token onto the stack.
        tokens.remove(token)
        
        while(1):
            rule = get_applicable_rule()
            if (!rule)  
               break;
            reduce(rule)
            
    return stack.top()

# Example usage
lexer = init_lexer()
parser = init_parser()

input_str = "2 + 3 * (4 - 1)"
result = parse(input_str)
print(result)  # Expected output: 11

```



## ANTL 2 PLY

Adapting certain constructs from ANTLR's VHDL grammar to Python PLY, which does not support all the syntax features, may require creative adjustments. Here are some key points and examples of how to handle unsupported syntax:

1. **Optional Elements (`?`)**: In PLY, optional elements can be managed by checking the length of the production (`p`) list and handling missing elements with conditions.
2. **Kleene Star (`\*`) and Plus (`+`)**: Use recursive productions or Python list constructs to handle these.
3. **Action Code**: Inline actions in ANTLR (like `{...}`) need to be placed inside the PLY parser functions.
4. **Labeling Rules**: ANTLR's labeled alternatives are not directly supported. Use more specific rules instead.

Here's an example with workarounds:

### Original ANTLR Grammar Example

```
antlrCopy codeacross_aspect
    : identifier_list (tolerance_aspect)? (VARASGN expression)? ACROSS
```

### PLY Workaround

In PLY, optional elements can be handled by checking the length of the production list:

```
pythonCopy codedef p_across_aspect(p):
    '''
    across_aspect : identifier_list ACROSS
                  | identifier_list tolerance_aspect ACROSS
                  | identifier_list VARASGN expression ACROSS
                  | identifier_list tolerance_aspect VARASGN expression ACROSS
    '''
    if len(p) == 3:
        p[0] = ("across_aspect", p[1], None, None)
    elif len(p) == 4:
        if p[2] == "ACROSS":
            p[0] = ("across_aspect", p[1], None, None)
        else:
            p[0] = ("across_aspect", p[1], p[2], None)
    elif len(p) == 5:
        p[0] = ("across_aspect", p[1], None, (p[3], p[4]))
    else:
        p[0] = ("across_aspect", p[1], p[2], (p[4], p[5]))
```

### Handling Repetition (`*` and `+`)

For repetition constructs, use recursion or loop constructs:

```
pythonCopy codedef p_association_list(p):
    '''
    association_list : association_element
                     | association_list COMMA association_element
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]
```

### Handling Optional Elements

For optional elements, explicitly check their presence:

```
pythonCopy codedef p_attribute_specification(p):
    '''
    attribute_specification : ATTRIBUTE attribute_designator OF entity_specification IS expression SEMI
    '''
    p[0] = ("attribute_specification", p[2], p[4], p[6])

def p_entity_specification(p):
    '''
    entity_specification : entity_name_list COLON entity_class
    '''
    p[0] = ("entity_specification", p[1], p[3])

def p_entity_name_list(p):
    '''
    entity_name_list : entity_designator
                     | entity_name_list COMMA entity_designator
                     | OTHERS
                     | ALL
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]
```

### Handling Inline Actions

Inline actions from ANTLR should be converted into corresponding Python code inside the PLY functions:

```
pythonCopy codedef p_expression(p):
    '''
    expression : relation
               | expression logical_operator relation
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ("logical_expr", p[1], p[2], p[3])
```

By restructuring the grammar rules and carefully handling optional and repeating elements, you can adapt most ANTLR VHDL grammar rules to PLY syntax. If you need further assistance with specific rules, feel free to ask!

## END

