######################################################
# Attempting to make a VHDL paser using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

import ply.yacc as yacc
from vhdl_lexer import tokens

start =  'design_file'

def p_abstract_literal(p):
    '''
    abstract_literal : INTEGER
        | REAL_LITERAL
        | BASE_LITERAL
    '''

def p_access_type_definition(p):
    '''
    access_type_definition : ACCESS subtype_indication
    '''

def p_across_aspect(p):
    '''
    across_aspect : identifier_list tolerance_aspect_a1mark warp0_a1mark ACROSS
    '''

def p_actual_designator(p):
    '''
    actual_designator : expression
        | OPEN
    '''

def p_actual_parameter_part(p):
    '''
    actual_parameter_part : association_list
    '''

def p_actual_part(p):
    '''
    actual_part : name LPAREN actual_designator RPAREN
        | actual_designator
    '''

def p_adding_operator(p):
    '''
    adding_operator : PLUS
        | MINUS
        | AMPERSAND
    '''

def p_aggregate(p):
    '''
    aggregate : LPAREN element_association warp1_a1star RPAREN
    '''

def p_alias_declaration(p):
    '''
    alias_declaration : ALIAS alias_designator warp2_a1mark IS name signature_a1mark SEMI
    '''

def p_alias_designator(p):
    '''
    alias_designator : identifier
        | CHARACTER_LITERAL
        | STRING_LITERAL
    '''

def p_alias_indication(p):
    '''
    alias_indication : subnature_indication
        | subtype_indication
    '''

def p_allocator(p):
    '''
    allocator : NEW warp3_a1branch
    '''

def p_architecture_body(p):
    '''
    architecture_body : ARCHITECTURE identifier OF identifier IS architecture_declarative_part BEGIN architecture_statement_part END ARCHITECTURE_a1mark identifier_a1mark SEMI
    '''

def p_architecture_declarative_part(p):
    '''
    architecture_declarative_part : block_declarative_item_a1star
    '''

def p_architecture_statement(p):
    '''
    architecture_statement : block_statement
        | process_statement
        | label_colon_a1mark concurrent_procedure_call_statement
        | label_colon_a1mark concurrent_assertion_statement
        | label_colon_a1mark POSTPONED_a1mark concurrent_signal_assignment_statement
        | component_instantiation_statement
        | generate_statement
        | concurrent_break_statement
        | simultaneous_statement
    '''

def p_architecture_statement_part(p):
    '''
    architecture_statement_part : architecture_statement_a1star
    '''

def p_array_nature_definition(p):
    '''
    array_nature_definition : unconstrained_nature_definition
        | constrained_nature_definition
    '''

def p_array_type_definition(p):
    '''
    array_type_definition : unconstrained_array_definition
        | constrained_array_definition
    '''

def p_assertion(p):
    '''
    assertion : ASSERT condition warp4_a1mark warp5_a1mark
    '''

def p_assertion_statement(p):
    '''
    assertion_statement : label_colon_a1mark assertion SEMI
    '''

def p_association_element(p):
    '''
    association_element : warp6_a1mark actual_part
    '''

def p_association_list(p):
    '''
    association_list : association_element warp7_a1star
    '''

def p_attribute_declaration(p):
    '''
    attribute_declaration : ATTRIBUTE label_colon name SEMI
    '''

def p_attribute_designator(p):
    '''
    attribute_designator : identifier
        | RANGE
        | REVERSE_RANGE
        | ACROSS
        | THROUGH
        | REFERENCE
        | TOLERANCE
    '''

def p_attribute_specification(p):
    '''
    attribute_specification : ATTRIBUTE attribute_designator OF entity_specification IS expression SEMI
    '''

def p_base_unit_declaration(p):
    '''
    base_unit_declaration : identifier SEMI
    '''

def p_binding_indication(p):
    '''
    binding_indication : warp8_a1mark generic_map_aspect_a1mark port_map_aspect_a1mark
    '''

def p_block_configuration(p):
    '''
    block_configuration : FOR block_specification use_clause_a1star configuration_item_a1star END FOR SEMI
    '''

def p_block_declarative_item(p):
    '''
    block_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | signal_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | component_declaration
        | attribute_declaration
        | attribute_specification
        | configuration_specification
        | disconnection_specification
        | step_limit_specification
        | use_clause
        | group_template_declaration
        | group_declaration
        | nature_declaration
        | subnature_declaration
        | quantity_declaration
        | terminal_declaration
    '''

def p_block_declarative_part(p):
    '''
    block_declarative_part : block_declarative_item_a1star
    '''

def p_block_header(p):
    '''
    block_header : warp10_a1mark warp12_a1mark
    '''

def p_block_specification(p):
    '''
    block_specification : identifier warp13_a1mark
        | name
    '''

def p_block_statement(p):
    '''
    block_statement : label_colon BLOCK warp14_a1mark IS_a1mark block_header block_declarative_part BEGIN block_statement_part END BLOCK identifier_a1mark SEMI
    '''

def p_block_statement_part(p):
    '''
    block_statement_part : architecture_statement_a1star
    '''

def p_branch_quantity_declaration(p):
    '''
    branch_quantity_declaration : QUANTITY across_aspect_a1mark through_aspect_a1mark terminal_aspect SEMI
    '''

def p_break_element(p):
    '''
    break_element : break_selector_clause_a1mark name ARROW expression
    '''

def p_break_list(p):
    '''
    break_list : break_element warp15_a1star
    '''

def p_break_selector_clause(p):
    '''
    break_selector_clause : FOR name USE
    '''

def p_break_statement(p):
    '''
    break_statement : label_colon_a1mark BREAK break_list_a1mark warp16_a1mark SEMI
    '''

def p_case_statement(p):
    '''
    case_statement : label_colon_a1mark CASE expression IS case_statement_alternative_a1plus END CASE identifier_a1mark SEMI
    '''

def p_case_statement_alternative(p):
    '''
    case_statement_alternative : WHEN choices ARROW sequence_of_statements
    '''

def p_choice(p):
    '''
    choice : identifier
        | discrete_range
        | simple_expression
        | OTHERS
    '''

def p_choices(p):
    '''
    choices : choice warp17_a1star
    '''

def p_component_configuration(p):
    '''
    component_configuration : FOR component_specification warp18_a1mark block_configuration_a1mark END FOR SEMI
    '''

def p_component_declaration(p):
    '''
    component_declaration : COMPONENT identifier IS_a1mark generic_clause_a1mark port_clause_a1mark END COMPONENT identifier_a1mark SEMI
    '''

def p_component_instantiation_statement(p):
    '''
    component_instantiation_statement : label_colon instantiated_unit generic_map_aspect_a1mark port_map_aspect_a1mark SEMI
    '''

def p_component_specification(p):
    '''
    component_specification : instantiation_list COLON name
    '''

def p_composite_nature_definition(p):
    '''
    composite_nature_definition : array_nature_definition
        | record_nature_definition
    '''

def p_composite_type_definition(p):
    '''
    composite_type_definition : array_type_definition
        | record_type_definition
    '''

def p_concurrent_assertion_statement(p):
    '''
    concurrent_assertion_statement : label_colon_a1mark POSTPONED_a1mark assertion SEMI
    '''

def p_concurrent_break_statement(p):
    '''
    concurrent_break_statement : label_colon_a1mark BREAK break_list_a1mark sensitivity_clause_a1mark warp19_a1mark SEMI
    '''

def p_concurrent_procedure_call_statement(p):
    '''
    concurrent_procedure_call_statement : label_colon_a1mark POSTPONED_a1mark procedure_call SEMI
    '''

def p_concurrent_signal_assignment_statement(p):
    '''
    concurrent_signal_assignment_statement : label_colon_a1mark POSTPONED_a1mark warp20_a1branch
    '''

def p_condition(p):
    '''
    condition : expression
    '''

def p_condition_clause(p):
    '''
    condition_clause : UNTIL condition
    '''

def p_conditional_signal_assignment(p):
    '''
    conditional_signal_assignment : target LE opts conditional_waveforms SEMI
    '''

def p_conditional_waveforms(p):
    '''
    conditional_waveforms : waveform warp22_a1mark
    '''

def p_configuration_declaration(p):
    '''
    configuration_declaration : CONFIGURATION identifier OF name IS configuration_declarative_part block_configuration END CONFIGURATION_a1mark identifier_a1mark SEMI
    '''

def p_configuration_declarative_item(p):
    '''
    configuration_declarative_item : use_clause
        | attribute_specification
        | group_declaration
    '''

def p_configuration_declarative_part(p):
    '''
    configuration_declarative_part : configuration_declarative_item_a1star
    '''

def p_configuration_item(p):
    '''
    configuration_item : block_configuration
        | component_configuration
    '''

def p_configuration_specification(p):
    '''
    configuration_specification : FOR component_specification binding_indication SEMI
    '''

def p_constant_declaration(p):
    '''
    constant_declaration : CONSTANT identifier_list COLON subtype_indication warp23_a1mark SEMI
    '''

def p_constrained_array_definition(p):
    '''
    constrained_array_definition : ARRAY index_constraint OF subtype_indication
    '''

def p_constrained_nature_definition(p):
    '''
    constrained_nature_definition : ARRAY index_constraint OF subnature_indication
    '''

def p_constraint(p):
    '''
    constraint : range_constraint
        | index_constraint
    '''

def p_context_clause(p):
    '''
    context_clause : context_item_a1star
    '''

def p_context_item(p):
    '''
    context_item : library_clause
        | use_clause
    '''

def p_delay_mechanism(p):
    '''
    delay_mechanism : TRANSPORT
        | warp24_a1mark INERTIAL
    '''

def p_design_file(p):
    '''
    design_file : design_unit_a1star
    '''

def p_design_unit(p):
    '''
    design_unit : context_clause library_unit
    '''

def p_designator(p):
    '''
    designator : identifier
        | STRING_LITERAL
    '''

def p_direction(p):
    '''
    direction : TO
        | DOWNTO
    '''

def p_disconnection_specification(p):
    '''
    disconnection_specification : DISCONNECT guarded_signal_specification AFTER expression SEMI
    '''

def p_discrete_range(p):
    '''
    discrete_range : range_decl
        | subtype_indication
    '''

def p_element_association(p):
    '''
    element_association : warp25_a1mark expression
    '''

def p_element_declaration(p):
    '''
    element_declaration : identifier_list COLON element_subtype_definition SEMI
    '''

def p_element_subnature_definition(p):
    '''
    element_subnature_definition : subnature_indication
    '''

def p_element_subtype_definition(p):
    '''
    element_subtype_definition : subtype_indication
    '''

def p_entity_aspect(p):
    '''
    entity_aspect : ENTITY name warp26_a1mark
        | CONFIGURATION name
        | OPEN
    '''

def p_entity_class(p):
    '''
    entity_class : ENTITY
        | ARCHITECTURE
        | CONFIGURATION
        | PROCEDURE
        | FUNCTION
        | PACKAGE
        | TYPE
        | SUBTYPE
        | CONSTANT
        | SIGNAL
        | VARIABLE
        | COMPONENT
        | LABEL
        | LITERAL
        | UNITS
        | GROUP
        | FILE
        | NATURE
        | SUBNATURE
        | QUANTITY
        | TERMINAL
    '''

def p_entity_class_entry(p):
    '''
    entity_class_entry : entity_class BOX_a1mark
    '''

def p_entity_class_entry_list(p):
    '''
    entity_class_entry_list : entity_class_entry warp27_a1star
    '''

def p_entity_declaration(p):
    '''
    entity_declaration : ENTITY identifier IS entity_header entity_declarative_part warp28_a1mark END ENTITY_a1mark identifier_a1mark SEMI
    '''

def p_entity_declarative_item(p):
    '''
    entity_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | signal_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | attribute_declaration
        | attribute_specification
        | disconnection_specification
        | step_limit_specification
        | use_clause
        | group_template_declaration
        | group_declaration
        | nature_declaration
        | subnature_declaration
        | quantity_declaration
        | terminal_declaration
    '''

def p_entity_declarative_part(p):
    '''
    entity_declarative_part : entity_declarative_item_a1star
    '''

def p_entity_designator(p):
    '''
    entity_designator : entity_tag signature_a1mark
    '''

def p_entity_header(p):
    '''
    entity_header : generic_clause_a1mark port_clause_a1mark
    '''

def p_entity_name_list(p):
    '''
    entity_name_list : entity_designator warp29_a1star
        | OTHERS
        | ALL
    '''

def p_entity_specification(p):
    '''
    entity_specification : entity_name_list COLON entity_class
    '''

def p_entity_statement(p):
    '''
    entity_statement : concurrent_assertion_statement
        | process_statement
        | concurrent_procedure_call_statement
    '''

def p_entity_statement_part(p):
    '''
    entity_statement_part : entity_statement_a1star
    '''

def p_entity_tag(p):
    '''
    entity_tag : identifier
        | CHARACTER_LITERAL
        | STRING_LITERAL
    '''

def p_enumeration_literal(p):
    '''
    enumeration_literal : identifier
        | CHARACTER_LITERAL
    '''

def p_enumeration_type_definition(p):
    '''
    enumeration_type_definition : LPAREN enumeration_literal warp30_a1star RPAREN
    '''

def p_exit_statement(p):
    '''
    exit_statement : label_colon_a1mark EXIT identifier_a1mark warp31_a1mark SEMI
    '''

def p_expression(p):
    '''
    expression : relation warp32_a1star
    '''

def p_factor(p):
    '''
    factor : primary warp33_a1mark
        | ABS primary
        | NOT primary
    '''

def p_file_declaration(p):
    '''
    file_declaration : FILE identifier_list COLON subtype_indication file_open_information_a1mark SEMI
    '''

def p_file_logical_name(p):
    '''
    file_logical_name : expression
    '''

def p_file_open_information(p):
    '''
    file_open_information : warp34_a1mark IS file_logical_name
    '''

def p_file_type_definition(p):
    '''
    file_type_definition : FILE OF subtype_indication
    '''

def p_formal_parameter_list(p):
    '''
    formal_parameter_list : interface_list
    '''

def p_formal_part(p):
    '''
    formal_part : identifier
        | identifier LPAREN explicit_range RPAREN
    '''

def p_free_quantity_declaration(p):
    '''
    free_quantity_declaration : QUANTITY identifier_list COLON subtype_indication warp35_a1mark SEMI
    '''

def p_generate_statement(p):
    '''
    generate_statement : label_colon generation_scheme GENERATE warp36_a1mark architecture_statement_a1star END GENERATE identifier_a1mark SEMI
    '''

def p_generation_scheme(p):
    '''
    generation_scheme : FOR parameter_specification
        | IF condition
    '''

def p_generic_clause(p):
    '''
    generic_clause : GENERIC LPAREN generic_list RPAREN SEMI
    '''

def p_generic_list(p):
    '''
    generic_list : interface_constant_declaration warp37_a1star
    '''

def p_generic_map_aspect(p):
    '''
    generic_map_aspect : GENERIC MAP LPAREN association_list RPAREN
    '''

def p_group_constituent(p):
    '''
    group_constituent : name
        | CHARACTER_LITERAL
    '''

def p_group_constituent_list(p):
    '''
    group_constituent_list : group_constituent warp38_a1star
    '''

def p_group_declaration(p):
    '''
    group_declaration : GROUP label_colon name LPAREN group_constituent_list RPAREN SEMI
    '''

def p_group_template_declaration(p):
    '''
    group_template_declaration : GROUP identifier IS LPAREN entity_class_entry_list RPAREN SEMI
    '''

def p_guarded_signal_specification(p):
    '''
    guarded_signal_specification : signal_list COLON name
    '''

def p_identifier(p):
    '''
    identifier : BASIC_IDENTIFIER
        | EXTENDED_IDENTIFIER
    '''

def p_identifier_list(p):
    '''
    identifier_list : identifier warp39_a1star
    '''

def p_if_statement(p):
    '''
    if_statement : label_colon_a1mark IF condition THEN sequence_of_statements warp40_a1star warp41_a1mark END IF identifier_a1mark SEMI
    '''

def p_index_constraint(p):
    '''
    index_constraint : LPAREN discrete_range warp42_a1star RPAREN
    '''

def p_index_specification(p):
    '''
    index_specification : discrete_range
        | expression
    '''

def p_index_subtype_definition(p):
    '''
    index_subtype_definition : name RANGE BOX
    '''

def p_instantiated_unit(p):
    '''
    instantiated_unit : COMPONENT_a1mark name
        | ENTITY name warp43_a1mark
        | CONFIGURATION name
    '''

def p_instantiation_list(p):
    '''
    instantiation_list : identifier warp44_a1star
        | OTHERS
        | ALL
    '''

def p_interface_constant_declaration(p):
    '''
    interface_constant_declaration : CONSTANT_a1mark identifier_list COLON IN_a1mark subtype_indication warp45_a1mark
    '''

def p_interface_declaration(p):
    '''
    interface_declaration : interface_constant_declaration
        | interface_signal_declaration
        | interface_variable_declaration
        | interface_file_declaration
        | interface_terminal_declaration
        | interface_quantity_declaration
    '''

def p_interface_element(p):
    '''
    interface_element : interface_declaration
    '''

def p_interface_file_declaration(p):
    '''
    interface_file_declaration : FILE identifier_list COLON subtype_indication
    '''

def p_interface_signal_list(p):
    '''
    interface_signal_list : interface_signal_declaration warp46_a1star
    '''

def p_interface_port_list(p):
    '''
    interface_port_list : interface_port_declaration warp47_a1star
    '''

def p_interface_list(p):
    '''
    interface_list : interface_element warp48_a1star
    '''

def p_interface_quantity_declaration(p):
    '''
    interface_quantity_declaration : QUANTITY identifier_list COLON warp49_a1mark subtype_indication warp50_a1mark
    '''

def p_interface_port_declaration(p):
    '''
    interface_port_declaration : identifier_list COLON signal_mode_a1mark subtype_indication BUS_a1mark warp51_a1mark
    '''

def p_interface_signal_declaration(p):
    '''
    interface_signal_declaration : SIGNAL identifier_list COLON signal_mode_a1mark subtype_indication BUS_a1mark warp52_a1mark
    '''

def p_interface_terminal_declaration(p):
    '''
    interface_terminal_declaration : TERMINAL identifier_list COLON subnature_indication
    '''

def p_interface_variable_declaration(p):
    '''
    interface_variable_declaration : VARIABLE_a1mark identifier_list COLON signal_mode_a1mark subtype_indication warp53_a1mark
    '''

def p_iteration_scheme(p):
    '''
    iteration_scheme : WHILE condition
        | FOR parameter_specification
    '''

def p_label_colon(p):
    '''
    label_colon : identifier COLON
    '''

def p_library_clause(p):
    '''
    library_clause : LIBRARY logical_name_list SEMI
    '''

def p_library_unit(p):
    '''
    library_unit : secondary_unit
        | primary_unit
    '''

def p_literal(p):
    '''
    literal : NULL_
        | BIT_STRING_LITERAL
        | STRING_LITERAL
        | enumeration_literal
        | numeric_literal
    '''

def p_logical_name(p):
    '''
    logical_name : identifier
    '''

def p_logical_name_list(p):
    '''
    logical_name_list : logical_name warp54_a1star
    '''

def p_logical_operator(p):
    '''
    logical_operator : AND
        | OR
        | NAND
        | NOR
        | XOR
        | XNOR
    '''

def p_loop_statement(p):
    '''
    loop_statement : label_colon_a1mark iteration_scheme_a1mark LOOP sequence_of_statements END LOOP identifier_a1mark SEMI
    '''

def p_signal_mode(p):
    '''
    signal_mode : IN
        | OUT
        | INOUT
        | BUFFER
        | LINKAGE
    '''

def p_multiplying_operator(p):
    '''
    multiplying_operator : MUL
        | DIV
        | MOD
        | REM
    '''

def p_name(p):
    '''
    name : warp55_a1branch name_part_a1star
    '''

def p_name_part(p):
    '''
    name_part : selected_name_part
        | function_call_or_indexed_name_part
        | slice_name_part
        | attribute_name_part
    '''

def p_selected_name(p):
    '''
    selected_name : identifier warp56_a1star
    '''

def p_selected_name_part(p):
    '''
    selected_name_part : warp57_a1plus
    '''

def p_function_call_or_indexed_name_part(p):
    '''
    function_call_or_indexed_name_part : LPAREN actual_parameter_part RPAREN
    '''

def p_slice_name_part(p):
    '''
    slice_name_part : LPAREN discrete_range RPAREN
    '''

def p_attribute_name_part(p):
    '''
    attribute_name_part : signature_a1mark APOSTROPHE attribute_designator warp58_a1mark
    '''

def p_nature_declaration(p):
    '''
    nature_declaration : NATURE identifier IS nature_definition SEMI
    '''

def p_nature_definition(p):
    '''
    nature_definition : scalar_nature_definition
        | composite_nature_definition
    '''

def p_nature_element_declaration(p):
    '''
    nature_element_declaration : identifier_list COLON element_subnature_definition
    '''

def p_next_statement(p):
    '''
    next_statement : label_colon_a1mark NEXT identifier_a1mark warp59_a1mark SEMI
    '''

def p_numeric_literal(p):
    '''
    numeric_literal : abstract_literal
        | physical_literal
    '''

def p_object_declaration(p):
    '''
    object_declaration : constant_declaration
        | signal_declaration
        | variable_declaration
        | file_declaration
        | terminal_declaration
        | quantity_declaration
    '''

def p_opts(p):
    '''
    opts : GUARDED_a1mark delay_mechanism_a1mark
    '''

def p_package_body(p):
    '''
    package_body : PACKAGE BODY identifier IS package_body_declarative_part END warp60_a1mark identifier_a1mark SEMI
    '''

def p_package_body_declarative_item(p):
    '''
    package_body_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | use_clause
        | group_template_declaration
        | group_declaration
    '''

def p_package_body_declarative_part(p):
    '''
    package_body_declarative_part : package_body_declarative_item_a1star
    '''

def p_package_declaration(p):
    '''
    package_declaration : PACKAGE identifier IS package_declarative_part END PACKAGE_a1mark identifier_a1mark SEMI
    '''

def p_package_declarative_item(p):
    '''
    package_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | signal_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | component_declaration
        | attribute_declaration
        | attribute_specification
        | disconnection_specification
        | use_clause
        | group_template_declaration
        | group_declaration
        | nature_declaration
        | subnature_declaration
        | terminal_declaration
    '''

def p_package_declarative_part(p):
    '''
    package_declarative_part : package_declarative_item_a1star
    '''

def p_parameter_specification(p):
    '''
    parameter_specification : identifier IN discrete_range
    '''

def p_physical_literal(p):
    '''
    physical_literal : abstract_literal identifier
    '''

def p_physical_type_definition(p):
    '''
    physical_type_definition : range_constraint UNITS base_unit_declaration secondary_unit_declaration_a1star END UNITS identifier_a1mark
    '''

def p_port_clause(p):
    '''
    port_clause : PORT LPAREN port_list RPAREN SEMI
    '''

def p_port_list(p):
    '''
    port_list : interface_port_list
    '''

def p_port_map_aspect(p):
    '''
    port_map_aspect : PORT MAP LPAREN association_list RPAREN
    '''

def p_primary(p):
    '''
    primary : literal
        | qualified_expression
        | LPAREN expression RPAREN
        | allocator
        | aggregate
        | name
    '''

def p_primary_unit(p):
    '''
    primary_unit : entity_declaration
        | configuration_declaration
        | package_declaration
    '''

def p_procedural_declarative_item(p):
    '''
    procedural_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | variable_declaration
        | alias_declaration
        | attribute_declaration
        | attribute_specification
        | use_clause
        | group_template_declaration
        | group_declaration
    '''

def p_procedural_declarative_part(p):
    '''
    procedural_declarative_part : procedural_declarative_item_a1star
    '''

def p_procedural_statement_part(p):
    '''
    procedural_statement_part : sequential_statement_a1star
    '''

def p_procedure_call(p):
    '''
    procedure_call : selected_name warp61_a1mark
    '''

def p_procedure_call_statement(p):
    '''
    procedure_call_statement : label_colon_a1mark procedure_call SEMI
    '''

def p_process_declarative_item(p):
    '''
    process_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | attribute_declaration
        | attribute_specification
        | use_clause
        | group_template_declaration
        | group_declaration
    '''

def p_process_declarative_part(p):
    '''
    process_declarative_part : process_declarative_item_a1star
    '''

def p_process_statement(p):
    '''
    process_statement : label_colon_a1mark POSTPONED_a1mark PROCESS warp62_a1mark IS_a1mark process_declarative_part BEGIN process_statement_part END POSTPONED_a1mark PROCESS identifier_a1mark SEMI
    '''

def p_process_statement_part(p):
    '''
    process_statement_part : sequential_statement_a1star
    '''

def p_qualified_expression(p):
    '''
    qualified_expression : subtype_indication APOSTROPHE warp63_a1branch
    '''

def p_quantity_declaration(p):
    '''
    quantity_declaration : free_quantity_declaration
        | branch_quantity_declaration
        | source_quantity_declaration
    '''

def p_quantity_list(p):
    '''
    quantity_list : name warp64_a1star
        | OTHERS
        | ALL
    '''

def p_quantity_specification(p):
    '''
    quantity_specification : quantity_list COLON name
    '''

def p_range_decl(p):
    '''
    range_decl : explicit_range
        | name
    '''

def p_explicit_range(p):
    '''
    explicit_range : simple_expression warp65_a1mark
    '''

def p_range_constraint(p):
    '''
    range_constraint : RANGE range_decl
    '''

def p_record_nature_definition(p):
    '''
    record_nature_definition : RECORD nature_element_declaration_a1plus END RECORD identifier_a1mark
    '''

def p_record_type_definition(p):
    '''
    record_type_definition : RECORD element_declaration_a1plus END RECORD identifier_a1mark
    '''

def p_relation(p):
    '''
    relation : shift_expression warp66_a1mark
    '''

def p_relational_operator(p):
    '''
    relational_operator : EQ
        | NEQ
        | LOWERTHAN
        | LE
        | GREATERTHAN
        | GE
    '''

def p_report_statement(p):
    '''
    report_statement : label_colon_a1mark REPORT expression warp67_a1mark SEMI
    '''

def p_return_statement(p):
    '''
    return_statement : label_colon_a1mark RETURN expression_a1mark SEMI
    '''

def p_scalar_nature_definition(p):
    '''
    scalar_nature_definition : name ACROSS name THROUGH name REFERENCE
    '''

def p_scalar_type_definition(p):
    '''
    scalar_type_definition : physical_type_definition
        | enumeration_type_definition
        | range_constraint
    '''

def p_secondary_unit(p):
    '''
    secondary_unit : architecture_body
        | package_body
    '''

def p_secondary_unit_declaration(p):
    '''
    secondary_unit_declaration : identifier EQ physical_literal SEMI
    '''

def p_selected_signal_assignment(p):
    '''
    selected_signal_assignment : WITH expression SELECT target LE opts selected_waveforms SEMI
    '''

def p_selected_waveforms(p):
    '''
    selected_waveforms : waveform WHEN choices warp68_a1star
    '''

def p_sensitivity_clause(p):
    '''
    sensitivity_clause : ON sensitivity_list
    '''

def p_sensitivity_list(p):
    '''
    sensitivity_list : name warp69_a1star
    '''

def p_sequence_of_statements(p):
    '''
    sequence_of_statements : sequential_statement_a1star
    '''

def p_sequential_statement(p):
    '''
    sequential_statement : wait_statement
        | assertion_statement
        | report_statement
        | signal_assignment_statement
        | variable_assignment_statement
        | if_statement
        | case_statement
        | loop_statement
        | next_statement
        | exit_statement
        | return_statement
        | label_colon_a1mark NULL_ SEMI
        | break_statement
        | procedure_call_statement
    '''

def p_shift_expression(p):
    '''
    shift_expression : simple_expression warp70_a1mark
    '''

def p_shift_operator(p):
    '''
    shift_operator : SLL
        | SRL
        | SLA
        | SRA
        | ROL
        | ROR
    '''

def p_signal_assignment_statement(p):
    '''
    signal_assignment_statement : label_colon_a1mark target LE delay_mechanism_a1mark waveform SEMI
    '''

def p_signal_declaration(p):
    '''
    signal_declaration : SIGNAL identifier_list COLON subtype_indication signal_kind_a1mark warp71_a1mark SEMI
    '''

def p_signal_kind(p):
    '''
    signal_kind : REGISTER
        | BUS
    '''

def p_signal_list(p):
    '''
    signal_list : name warp72_a1star
        | OTHERS
        | ALL
    '''

def p_signature(p):
    '''
    signature : LBRACKET warp74_a1mark warp75_a1mark RBRACKET
    '''

def p_simple_expression(p):
    '''
    simple_expression : warp76_a1mark term warp77_a1star
    '''

def p_simple_simultaneous_statement(p):
    '''
    simple_simultaneous_statement : label_colon_a1mark simple_expression ASSIGN simple_expression tolerance_aspect_a1mark SEMI
    '''

def p_simultaneous_alternative(p):
    '''
    simultaneous_alternative : WHEN choices ARROW simultaneous_statement_part
    '''

def p_simultaneous_case_statement(p):
    '''
    simultaneous_case_statement : label_colon_a1mark CASE expression USE simultaneous_alternative_a1plus END CASE identifier_a1mark SEMI
    '''

def p_simultaneous_if_statement(p):
    '''
    simultaneous_if_statement : label_colon_a1mark IF condition USE simultaneous_statement_part warp78_a1star warp79_a1mark END USE identifier_a1mark SEMI
    '''

def p_simultaneous_procedural_statement(p):
    '''
    simultaneous_procedural_statement : label_colon_a1mark PROCEDURAL IS_a1mark procedural_declarative_part BEGIN procedural_statement_part END PROCEDURAL identifier_a1mark SEMI
    '''

def p_simultaneous_statement(p):
    '''
    simultaneous_statement : simple_simultaneous_statement
        | simultaneous_if_statement
        | simultaneous_case_statement
        | simultaneous_procedural_statement
        | label_colon_a1mark NULL_ SEMI
    '''

def p_simultaneous_statement_part(p):
    '''
    simultaneous_statement_part : simultaneous_statement_a1star
    '''

def p_source_aspect(p):
    '''
    source_aspect : SPECTRUM simple_expression COMMA simple_expression
        | NOISE simple_expression
    '''

def p_source_quantity_declaration(p):
    '''
    source_quantity_declaration : QUANTITY identifier_list COLON subtype_indication source_aspect SEMI
    '''

def p_step_limit_specification(p):
    '''
    step_limit_specification : LIMIT quantity_specification WITH expression SEMI
    '''

def p_subnature_declaration(p):
    '''
    subnature_declaration : SUBNATURE identifier IS subnature_indication SEMI
    '''

def p_subnature_indication(p):
    '''
    subnature_indication : name index_constraint_a1mark warp80_a1mark
    '''

def p_subprogram_body(p):
    '''
    subprogram_body : subprogram_specification IS subprogram_declarative_part BEGIN subprogram_statement_part END subprogram_kind_a1mark designator_a1mark SEMI
    '''

def p_subprogram_declaration(p):
    '''
    subprogram_declaration : subprogram_specification SEMI
    '''

def p_subprogram_declarative_item(p):
    '''
    subprogram_declarative_item : subprogram_declaration
        | subprogram_body
        | type_declaration
        | subtype_declaration
        | constant_declaration
        | variable_declaration
        | file_declaration
        | alias_declaration
        | attribute_declaration
        | attribute_specification
        | use_clause
        | group_template_declaration
        | group_declaration
    '''

def p_subprogram_declarative_part(p):
    '''
    subprogram_declarative_part : subprogram_declarative_item_a1star
    '''

def p_subprogram_kind(p):
    '''
    subprogram_kind : PROCEDURE
        | FUNCTION
    '''

def p_subprogram_specification(p):
    '''
    subprogram_specification : procedure_specification
        | function_specification
    '''

def p_procedure_specification(p):
    '''
    procedure_specification : PROCEDURE designator warp81_a1mark
    '''

def p_function_specification(p):
    '''
    function_specification : warp82_a1mark FUNCTION designator warp83_a1mark RETURN subtype_indication
    '''

def p_subprogram_statement_part(p):
    '''
    subprogram_statement_part : sequential_statement_a1star
    '''

def p_subtype_declaration(p):
    '''
    subtype_declaration : SUBTYPE identifier IS subtype_indication SEMI
    '''

def p_subtype_indication(p):
    '''
    subtype_indication : selected_name selected_name_a1mark constraint_a1mark tolerance_aspect_a1mark
    '''

def p_suffix(p):
    '''
    suffix : identifier
        | CHARACTER_LITERAL
        | STRING_LITERAL
        | ALL
    '''

def p_target(p):
    '''
    target : name
        | aggregate
    '''

def p_term(p):
    '''
    term : factor warp84_a1star
    '''

def p_terminal_aspect(p):
    '''
    terminal_aspect : name warp85_a1mark
    '''

def p_terminal_declaration(p):
    '''
    terminal_declaration : TERMINAL identifier_list COLON subnature_indication SEMI
    '''

def p_through_aspect(p):
    '''
    through_aspect : identifier_list tolerance_aspect_a1mark warp86_a1mark THROUGH
    '''

def p_timeout_clause(p):
    '''
    timeout_clause : FOR expression
    '''

def p_tolerance_aspect(p):
    '''
    tolerance_aspect : TOLERANCE expression
    '''

def p_type_declaration(p):
    '''
    type_declaration : TYPE identifier warp87_a1mark SEMI
    '''

def p_type_definition(p):
    '''
    type_definition : scalar_type_definition
        | composite_type_definition
        | access_type_definition
        | file_type_definition
    '''

def p_unconstrained_array_definition(p):
    '''
    unconstrained_array_definition : ARRAY LPAREN index_subtype_definition warp88_a1star RPAREN OF subtype_indication
    '''

def p_unconstrained_nature_definition(p):
    '''
    unconstrained_nature_definition : ARRAY LPAREN index_subtype_definition warp89_a1star RPAREN OF subnature_indication
    '''

def p_use_clause(p):
    '''
    use_clause : USE selected_name warp90_a1star SEMI
    '''

def p_variable_assignment_statement(p):
    '''
    variable_assignment_statement : label_colon_a1mark target VARASGN expression SEMI
    '''

def p_variable_declaration(p):
    '''
    variable_declaration : SHARED_a1mark VARIABLE identifier_list COLON subtype_indication warp91_a1mark SEMI
    '''

def p_wait_statement(p):
    '''
    wait_statement : label_colon_a1mark WAIT sensitivity_clause_a1mark condition_clause_a1mark timeout_clause_a1mark SEMI
    '''

def p_waveform(p):
    '''
    waveform : waveform_element warp92_a1star
        | UNAFFECTED
    '''

def p_waveform_element(p):
    '''
    waveform_element : expression warp93_a1mark
    '''

def p_BIT_STRING_LITERAL(p):
    '''
    BIT_STRING_LITERAL : BIT_STRING_LITERAL_BINARY
        | BIT_STRING_LITERAL_OCTAL
        | BIT_STRING_LITERAL_HEX
    '''

def p_tolerance_aspect_a1mark(p):
    '''
    tolerance_aspect_a1mark : tolerance_aspect
        | empty
    '''

def p_warp0_a1mark(p):
    '''
    warp0_a1mark : VARASGN expression
        | empty
    '''

def p_warp1_a1star(p):
    '''
    warp1_a1star : COMMA element_association warp1_a1star
        | COMMA element_association
        | empty
    '''

def p_warp2_a1mark(p):
    '''
    warp2_a1mark : COLON alias_indication
        | empty
    '''

def p_signature_a1mark(p):
    '''
    signature_a1mark : signature
        | empty
    '''

def p_warp3_a1branch(p):
    '''
    warp3_a1branch : qualified_expression 
        |  subtype_indication
    '''

def p_ARCHITECTURE_a1mark(p):
    '''
    ARCHITECTURE_a1mark : ARCHITECTURE
        | empty
    '''

def p_identifier_a1mark(p):
    '''
    identifier_a1mark : identifier
        | empty
    '''

def p_block_declarative_item_a1star(p):
    '''
    block_declarative_item_a1star : block_declarative_item block_declarative_item_a1star
        | block_declarative_item
        | empty
    '''

def p_label_colon_a1mark(p):
    '''
    label_colon_a1mark : label_colon
        | empty
    '''

def p_POSTPONED_a1mark(p):
    '''
    POSTPONED_a1mark : POSTPONED
        | empty
    '''

def p_architecture_statement_a1star(p):
    '''
    architecture_statement_a1star : architecture_statement architecture_statement_a1star
        | architecture_statement
        | empty
    '''

def p_warp4_a1mark(p):
    '''
    warp4_a1mark : REPORT expression
        | empty
    '''

def p_warp5_a1mark(p):
    '''
    warp5_a1mark : SEVERITY expression
        | empty
    '''

def p_warp6_a1mark(p):
    '''
    warp6_a1mark : formal_part ARROW
        | empty
    '''

def p_warp7_a1star(p):
    '''
    warp7_a1star : COMMA association_element warp7_a1star
        | COMMA association_element
        | empty
    '''

def p_warp8_a1mark(p):
    '''
    warp8_a1mark : USE entity_aspect
        | empty
    '''

def p_generic_map_aspect_a1mark(p):
    '''
    generic_map_aspect_a1mark : generic_map_aspect
        | empty
    '''

def p_port_map_aspect_a1mark(p):
    '''
    port_map_aspect_a1mark : port_map_aspect
        | empty
    '''

def p_use_clause_a1star(p):
    '''
    use_clause_a1star : use_clause use_clause_a1star
        | use_clause
        | empty
    '''

def p_configuration_item_a1star(p):
    '''
    configuration_item_a1star : configuration_item configuration_item_a1star
        | configuration_item
        | empty
    '''

def p_warp9_a1mark(p):
    '''
    warp9_a1mark : generic_map_aspect SEMI
        | empty
    '''

def p_warp10_a1mark(p):
    '''
    warp10_a1mark : generic_clause warp9_a1mark
        | empty
    '''

def p_warp11_a1mark(p):
    '''
    warp11_a1mark : port_map_aspect SEMI
        | empty
    '''

def p_warp12_a1mark(p):
    '''
    warp12_a1mark : port_clause warp11_a1mark
        | empty
    '''

def p_warp13_a1mark(p):
    '''
    warp13_a1mark : LPAREN index_specification RPAREN
        | empty
    '''

def p_warp14_a1mark(p):
    '''
    warp14_a1mark : LPAREN expression RPAREN
        | empty
    '''

def p_IS_a1mark(p):
    '''
    IS_a1mark : IS
        | empty
    '''

def p_across_aspect_a1mark(p):
    '''
    across_aspect_a1mark : across_aspect
        | empty
    '''

def p_through_aspect_a1mark(p):
    '''
    through_aspect_a1mark : through_aspect
        | empty
    '''

def p_break_selector_clause_a1mark(p):
    '''
    break_selector_clause_a1mark : break_selector_clause
        | empty
    '''

def p_warp15_a1star(p):
    '''
    warp15_a1star : COMMA break_element warp15_a1star
        | COMMA break_element
        | empty
    '''

def p_break_list_a1mark(p):
    '''
    break_list_a1mark : break_list
        | empty
    '''

def p_warp16_a1mark(p):
    '''
    warp16_a1mark : WHEN condition
        | empty
    '''

def p_case_statement_alternative_a1plus(p):
    '''
    case_statement_alternative_a1plus : case_statement_alternative case_statement_alternative_a1plus
        | case_statement_alternative
    '''

def p_warp17_a1star(p):
    '''
    warp17_a1star : BAR choice warp17_a1star
        | BAR choice
        | empty
    '''

def p_warp18_a1mark(p):
    '''
    warp18_a1mark : binding_indication SEMI
        | empty
    '''

def p_block_configuration_a1mark(p):
    '''
    block_configuration_a1mark : block_configuration
        | empty
    '''

def p_generic_clause_a1mark(p):
    '''
    generic_clause_a1mark : generic_clause
        | empty
    '''

def p_port_clause_a1mark(p):
    '''
    port_clause_a1mark : port_clause
        | empty
    '''

def p_sensitivity_clause_a1mark(p):
    '''
    sensitivity_clause_a1mark : sensitivity_clause
        | empty
    '''

def p_warp19_a1mark(p):
    '''
    warp19_a1mark : WHEN condition
        | empty
    '''

def p_warp20_a1branch(p):
    '''
    warp20_a1branch : conditional_signal_assignment 
        |  selected_signal_assignment
    '''

def p_warp21_a1mark(p):
    '''
    warp21_a1mark : ELSE conditional_waveforms
        | empty
    '''

def p_warp22_a1mark(p):
    '''
    warp22_a1mark : WHEN condition warp21_a1mark
        | empty
    '''

def p_CONFIGURATION_a1mark(p):
    '''
    CONFIGURATION_a1mark : CONFIGURATION
        | empty
    '''

def p_configuration_declarative_item_a1star(p):
    '''
    configuration_declarative_item_a1star : configuration_declarative_item configuration_declarative_item_a1star
        | configuration_declarative_item
        | empty
    '''

def p_warp23_a1mark(p):
    '''
    warp23_a1mark : VARASGN expression
        | empty
    '''

def p_context_item_a1star(p):
    '''
    context_item_a1star : context_item context_item_a1star
        | context_item
        | empty
    '''

def p_warp24_a1mark(p):
    '''
    warp24_a1mark : REJECT expression
        | empty
    '''

def p_design_unit_a1star(p):
    '''
    design_unit_a1star : design_unit design_unit_a1star
        | design_unit
        | empty
    '''

def p_warp25_a1mark(p):
    '''
    warp25_a1mark : choices ARROW
        | empty
    '''

def p_warp26_a1mark(p):
    '''
    warp26_a1mark : LPAREN identifier RPAREN
        | empty
    '''

def p_BOX_a1mark(p):
    '''
    BOX_a1mark : BOX
        | empty
    '''

def p_warp27_a1star(p):
    '''
    warp27_a1star : COMMA entity_class_entry warp27_a1star
        | COMMA entity_class_entry
        | empty
    '''

def p_warp28_a1mark(p):
    '''
    warp28_a1mark : BEGIN entity_statement_part
        | empty
    '''

def p_ENTITY_a1mark(p):
    '''
    ENTITY_a1mark : ENTITY
        | empty
    '''

def p_entity_declarative_item_a1star(p):
    '''
    entity_declarative_item_a1star : entity_declarative_item entity_declarative_item_a1star
        | entity_declarative_item
        | empty
    '''

def p_warp29_a1star(p):
    '''
    warp29_a1star : COMMA entity_designator warp29_a1star
        | COMMA entity_designator
        | empty
    '''

def p_entity_statement_a1star(p):
    '''
    entity_statement_a1star : entity_statement entity_statement_a1star
        | entity_statement
        | empty
    '''

def p_warp30_a1star(p):
    '''
    warp30_a1star : COMMA enumeration_literal warp30_a1star
        | COMMA enumeration_literal
        | empty
    '''

def p_warp31_a1mark(p):
    '''
    warp31_a1mark : WHEN condition
        | empty
    '''

def p_warp32_a1star(p):
    '''
    warp32_a1star : logical_operator relation warp32_a1star
        | logical_operator relation
        | empty
    '''

def p_warp33_a1mark(p):
    '''
    warp33_a1mark : DOUBLESTAR primary
        | empty
    '''

def p_file_open_information_a1mark(p):
    '''
    file_open_information_a1mark : file_open_information
        | empty
    '''

def p_warp34_a1mark(p):
    '''
    warp34_a1mark : OPEN expression
        | empty
    '''

def p_warp35_a1mark(p):
    '''
    warp35_a1mark : VARASGN expression
        | empty
    '''

def p_warp36_a1mark(p):
    '''
    warp36_a1mark : block_declarative_item_a1star BEGIN
        | empty
    '''

def p_warp37_a1star(p):
    '''
    warp37_a1star : SEMI interface_constant_declaration warp37_a1star
        | SEMI interface_constant_declaration
        | empty
    '''

def p_warp38_a1star(p):
    '''
    warp38_a1star : COMMA group_constituent warp38_a1star
        | COMMA group_constituent
        | empty
    '''

def p_warp39_a1star(p):
    '''
    warp39_a1star : COMMA identifier warp39_a1star
        | COMMA identifier
        | empty
    '''

def p_warp40_a1star(p):
    '''
    warp40_a1star : ELSIF condition THEN sequence_of_statements warp40_a1star
        | ELSIF condition THEN sequence_of_statements
        | empty
    '''

def p_warp41_a1mark(p):
    '''
    warp41_a1mark : ELSE sequence_of_statements
        | empty
    '''

def p_warp42_a1star(p):
    '''
    warp42_a1star : COMMA discrete_range warp42_a1star
        | COMMA discrete_range
        | empty
    '''

def p_COMPONENT_a1mark(p):
    '''
    COMPONENT_a1mark : COMPONENT
        | empty
    '''

def p_warp43_a1mark(p):
    '''
    warp43_a1mark : LPAREN identifier RPAREN
        | empty
    '''

def p_warp44_a1star(p):
    '''
    warp44_a1star : COMMA identifier warp44_a1star
        | COMMA identifier
        | empty
    '''

def p_CONSTANT_a1mark(p):
    '''
    CONSTANT_a1mark : CONSTANT
        | empty
    '''

def p_IN_a1mark(p):
    '''
    IN_a1mark : IN
        | empty
    '''

def p_warp45_a1mark(p):
    '''
    warp45_a1mark : VARASGN expression
        | empty
    '''

def p_warp46_a1star(p):
    '''
    warp46_a1star : SEMI interface_signal_declaration warp46_a1star
        | SEMI interface_signal_declaration
        | empty
    '''

def p_warp47_a1star(p):
    '''
    warp47_a1star : SEMI interface_port_declaration warp47_a1star
        | SEMI interface_port_declaration
        | empty
    '''

def p_warp48_a1star(p):
    '''
    warp48_a1star : SEMI interface_element warp48_a1star
        | SEMI interface_element
        | empty
    '''

def p_warp49_a1mark(p):
    '''
    warp49_a1mark : warp94_a1branch
        | empty
    '''

def p_warp50_a1mark(p):
    '''
    warp50_a1mark : VARASGN expression
        | empty
    '''

def p_signal_mode_a1mark(p):
    '''
    signal_mode_a1mark : signal_mode
        | empty
    '''

def p_BUS_a1mark(p):
    '''
    BUS_a1mark : BUS
        | empty
    '''

def p_warp51_a1mark(p):
    '''
    warp51_a1mark : VARASGN expression
        | empty
    '''

def p_warp52_a1mark(p):
    '''
    warp52_a1mark : VARASGN expression
        | empty
    '''

def p_VARIABLE_a1mark(p):
    '''
    VARIABLE_a1mark : VARIABLE
        | empty
    '''

def p_warp53_a1mark(p):
    '''
    warp53_a1mark : VARASGN expression
        | empty
    '''

def p_warp54_a1star(p):
    '''
    warp54_a1star : COMMA logical_name warp54_a1star
        | COMMA logical_name
        | empty
    '''

def p_iteration_scheme_a1mark(p):
    '''
    iteration_scheme_a1mark : iteration_scheme
        | empty
    '''

def p_name_part_a1star(p):
    '''
    name_part_a1star : name_part name_part_a1star
        | name_part
        | empty
    '''

def p_warp55_a1branch(p):
    '''
    warp55_a1branch : identifier 
        |  STRING_LITERAL
    '''

def p_warp56_a1star(p):
    '''
    warp56_a1star : DOT suffix warp56_a1star
        | DOT suffix
        | empty
    '''

def p_warp57_a1plus(p):
    '''
    warp57_a1plus : DOT suffix warp57_a1plus
        | DOT suffix
    '''

def p_warp58_a1mark(p):
    '''
    warp58_a1mark : LPAREN expression RPAREN
        | empty
    '''

def p_warp59_a1mark(p):
    '''
    warp59_a1mark : WHEN condition
        | empty
    '''

def p_GUARDED_a1mark(p):
    '''
    GUARDED_a1mark : GUARDED
        | empty
    '''

def p_delay_mechanism_a1mark(p):
    '''
    delay_mechanism_a1mark : delay_mechanism
        | empty
    '''

def p_warp60_a1mark(p):
    '''
    warp60_a1mark : PACKAGE BODY
        | empty
    '''

def p_package_body_declarative_item_a1star(p):
    '''
    package_body_declarative_item_a1star : package_body_declarative_item package_body_declarative_item_a1star
        | package_body_declarative_item
        | empty
    '''

def p_PACKAGE_a1mark(p):
    '''
    PACKAGE_a1mark : PACKAGE
        | empty
    '''

def p_package_declarative_item_a1star(p):
    '''
    package_declarative_item_a1star : package_declarative_item package_declarative_item_a1star
        | package_declarative_item
        | empty
    '''

def p_secondary_unit_declaration_a1star(p):
    '''
    secondary_unit_declaration_a1star : secondary_unit_declaration secondary_unit_declaration_a1star
        | secondary_unit_declaration
        | empty
    '''

def p_procedural_declarative_item_a1star(p):
    '''
    procedural_declarative_item_a1star : procedural_declarative_item procedural_declarative_item_a1star
        | procedural_declarative_item
        | empty
    '''

def p_sequential_statement_a1star(p):
    '''
    sequential_statement_a1star : sequential_statement sequential_statement_a1star
        | sequential_statement
        | empty
    '''

def p_warp61_a1mark(p):
    '''
    warp61_a1mark : LPAREN actual_parameter_part RPAREN
        | empty
    '''

def p_process_declarative_item_a1star(p):
    '''
    process_declarative_item_a1star : process_declarative_item process_declarative_item_a1star
        | process_declarative_item
        | empty
    '''

def p_warp62_a1mark(p):
    '''
    warp62_a1mark : LPAREN sensitivity_list RPAREN
        | empty
    '''

def p_warp63_a1branch(p):
    '''
    warp63_a1branch : aggregate 
        |  LPAREN expression RPAREN
    '''

def p_warp64_a1star(p):
    '''
    warp64_a1star : COMMA name warp64_a1star
        | COMMA name
        | empty
    '''

def p_warp65_a1mark(p):
    '''
    warp65_a1mark : direction simple_expression
        | empty
    '''

def p_nature_element_declaration_a1plus(p):
    '''
    nature_element_declaration_a1plus : nature_element_declaration nature_element_declaration_a1plus
        | nature_element_declaration
    '''

def p_element_declaration_a1plus(p):
    '''
    element_declaration_a1plus : element_declaration element_declaration_a1plus
        | element_declaration
    '''

def p_warp66_a1mark(p):
    '''
    warp66_a1mark : relational_operator shift_expression
        | empty
    '''

def p_warp67_a1mark(p):
    '''
    warp67_a1mark : SEVERITY expression
        | empty
    '''

def p_expression_a1mark(p):
    '''
    expression_a1mark : expression
        | empty
    '''

def p_warp68_a1star(p):
    '''
    warp68_a1star : COMMA waveform WHEN choices warp68_a1star
        | COMMA waveform WHEN choices
        | empty
    '''

def p_warp69_a1star(p):
    '''
    warp69_a1star : COMMA name warp69_a1star
        | COMMA name
        | empty
    '''

def p_warp70_a1mark(p):
    '''
    warp70_a1mark : shift_operator simple_expression
        | empty
    '''

def p_signal_kind_a1mark(p):
    '''
    signal_kind_a1mark : signal_kind
        | empty
    '''

def p_warp71_a1mark(p):
    '''
    warp71_a1mark : VARASGN expression
        | empty
    '''

def p_warp72_a1star(p):
    '''
    warp72_a1star : COMMA name warp72_a1star
        | COMMA name
        | empty
    '''

def p_warp73_a1star(p):
    '''
    warp73_a1star : COMMA name warp73_a1star
        | COMMA name
        | empty
    '''

def p_warp74_a1mark(p):
    '''
    warp74_a1mark : name warp73_a1star
        | empty
    '''

def p_warp75_a1mark(p):
    '''
    warp75_a1mark : RETURN name
        | empty
    '''

def p_warp76_a1mark(p):
    '''
    warp76_a1mark : warp95_a1branch
        | empty
    '''

def p_warp77_a1star(p):
    '''
    warp77_a1star : adding_operator term warp77_a1star
        | adding_operator term
        | empty
    '''

def p_simultaneous_alternative_a1plus(p):
    '''
    simultaneous_alternative_a1plus : simultaneous_alternative simultaneous_alternative_a1plus
        | simultaneous_alternative
    '''

def p_warp78_a1star(p):
    '''
    warp78_a1star : ELSIF condition USE simultaneous_statement_part warp78_a1star
        | ELSIF condition USE simultaneous_statement_part
        | empty
    '''

def p_warp79_a1mark(p):
    '''
    warp79_a1mark : ELSE simultaneous_statement_part
        | empty
    '''

def p_simultaneous_statement_a1star(p):
    '''
    simultaneous_statement_a1star : simultaneous_statement simultaneous_statement_a1star
        | simultaneous_statement
        | empty
    '''

def p_index_constraint_a1mark(p):
    '''
    index_constraint_a1mark : index_constraint
        | empty
    '''

def p_warp80_a1mark(p):
    '''
    warp80_a1mark : TOLERANCE expression ACROSS expression THROUGH
        | empty
    '''

def p_subprogram_kind_a1mark(p):
    '''
    subprogram_kind_a1mark : subprogram_kind
        | empty
    '''

def p_designator_a1mark(p):
    '''
    designator_a1mark : designator
        | empty
    '''

def p_subprogram_declarative_item_a1star(p):
    '''
    subprogram_declarative_item_a1star : subprogram_declarative_item subprogram_declarative_item_a1star
        | subprogram_declarative_item
        | empty
    '''

def p_warp81_a1mark(p):
    '''
    warp81_a1mark : LPAREN formal_parameter_list RPAREN
        | empty
    '''

def p_warp82_a1mark(p):
    '''
    warp82_a1mark : warp96_a1branch
        | empty
    '''

def p_warp83_a1mark(p):
    '''
    warp83_a1mark : LPAREN formal_parameter_list RPAREN
        | empty
    '''

def p_selected_name_a1mark(p):
    '''
    selected_name_a1mark : selected_name
        | empty
    '''

def p_constraint_a1mark(p):
    '''
    constraint_a1mark : constraint
        | empty
    '''

def p_warp84_a1star(p):
    '''
    warp84_a1star : multiplying_operator factor warp84_a1star
        | multiplying_operator factor
        | empty
    '''

def p_warp85_a1mark(p):
    '''
    warp85_a1mark : TO name
        | empty
    '''

def p_warp86_a1mark(p):
    '''
    warp86_a1mark : VARASGN expression
        | empty
    '''

def p_warp87_a1mark(p):
    '''
    warp87_a1mark : IS type_definition
        | empty
    '''

def p_warp88_a1star(p):
    '''
    warp88_a1star : COMMA index_subtype_definition warp88_a1star
        | COMMA index_subtype_definition
        | empty
    '''

def p_warp89_a1star(p):
    '''
    warp89_a1star : COMMA index_subtype_definition warp89_a1star
        | COMMA index_subtype_definition
        | empty
    '''

def p_warp90_a1star(p):
    '''
    warp90_a1star : COMMA selected_name warp90_a1star
        | COMMA selected_name
        | empty
    '''

def p_SHARED_a1mark(p):
    '''
    SHARED_a1mark : SHARED
        | empty
    '''

def p_warp91_a1mark(p):
    '''
    warp91_a1mark : VARASGN expression
        | empty
    '''

def p_condition_clause_a1mark(p):
    '''
    condition_clause_a1mark : condition_clause
        | empty
    '''

def p_timeout_clause_a1mark(p):
    '''
    timeout_clause_a1mark : timeout_clause
        | empty
    '''

def p_warp92_a1star(p):
    '''
    warp92_a1star : COMMA waveform_element warp92_a1star
        | COMMA waveform_element
        | empty
    '''

def p_warp93_a1mark(p):
    '''
    warp93_a1mark : AFTER expression
        | empty
    '''

def p_warp94_a1branch(p):
    '''
    warp94_a1branch : IN 
        |  OUT
    '''

def p_warp95_a1branch(p):
    '''
    warp95_a1branch : PLUS 
        |  MINUS
    '''

def p_warp96_a1branch(p):
    '''
    warp96_a1branch : PURE 
        |  IMPURE
    '''

# Define the empty rule to handle the zero occurrences case
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
import ply.yacc as yacc
parser = yacc.yacc()


