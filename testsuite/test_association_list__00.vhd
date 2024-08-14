
-- association_list    
--    U1 : ENTITY work.module1 PORT MAP (
        clk      => clk,
        rst      => rst,
        data_in  => input1,
        data_out => internal_signal1
--    );


association_list
    : association_element (COMMA association_element)*
    ;
	
association_element
    : (formal_part ARROW)? actual_part
    ;
	
formal_part
    : identifier
    | identifier LPAREN explicit_range RPAREN
    ;

identifier
    : BASIC_IDENTIFIER
    | EXTENDED_IDENTIFIER
    ;
	
	
actual_part
    : name LPAREN actual_designator RPAREN
    | actual_designator
    ;

actual_designator
    : expression
    | OPEN
    ;
	
	
expression
    : relation (: logical_operator relation)*
    ;

relation
    : shift_expression (: relational_operator shift_expression)?
    ;

shift_expression
    : simple_expression (: shift_operator simple_expression)?
    ;
		

simple_expression
    : (PLUS | MINUS)? term (: adding_operator term)*
    ;
	
term
    : factor (: multiplying_operator factor)*
    ;
	
	
factor
    : primary (: DOUBLESTAR primary)?
    | ABS primary
    | NOT primary
    ;
	
primary
    : literal
    | qualified_expression
    | LPAREN expression RPAREN
    | allocator
    | aggregate
    | name
    ;
	
name
    : (identifier | STRING_LITERAL) (name_part)*
    ;
	
	
	