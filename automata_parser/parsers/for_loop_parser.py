import ply.yacc as yacc
from automata_parser.lexers.for_loop_lexer import tokens

def p_statement_for(p):
    'statement : FOR ID IN RANGE LPAREN NUMBER RPAREN LBRACE statement RBRACE'
    p[0] = ('for', p[2], p[6], p[9])

def p_statement_expr(p):
    'statement : ID'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(tabmodule='_for_loop_parsetab', errorlog=yacc.NullLogger())
