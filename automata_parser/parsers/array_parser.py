import ply.yacc as yacc
from automata_parser.lexers.array_lexer import tokens

def p_statement_array(p):
    'statement : ID EQUALS LBRACKET elements RBRACKET'
    p[0] = ('array', p[1], p[4])

def p_elements(p):
    'elements : elements COMMA NUMBER'
    p[0] = p[1] + [p[3]]

def p_elements_single(p):
    'elements : NUMBER'
    p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(tabmodule='_array_parsetab', errorlog=yacc.NullLogger())
