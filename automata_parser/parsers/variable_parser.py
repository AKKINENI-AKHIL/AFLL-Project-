import ply.yacc as yacc
from automata_parser.lexers.variable_lexer import tokens

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(tabmodule='_variable_parsetab', errorlog=yacc.NullLogger())
