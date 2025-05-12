
while(<>) {
s/\bbased_literal\b/BASE_LITERAL/g;
s/\bextended_identifier\b/EXTENDED_IDENTIFIER/g;
s/\bcharacter_literal\b/CHARACTER_LITERAL/g;
s/\bstring_literal\b/STRING_LITERAL/g;
s/\bexponent\b/EXPONENT/g;
s/\bbasic_identifier\b/BASIC_IDENTIFIER/g;
s/\bextended_digit\b/EXTENDED_DIGIT/g;
S/\bbased_integer\b/BASED_INTEGER/g;
print $_;
}


BIT_STRING_LITERAL_BINARYbit_string_literal
BIT_STRING_LITERAL_OCTALbit_string_literal
BIT_STRING_LITERAL_HEXbit_string_literal
REAL_LITERALreal_literal (part of abstract_literal)
INTEGERinteger (part of abstract_literal)