import ply.yacc as yacc
from automata_parser.lexers.while_loop_lexer import tokens

def p_statement_while(p):
    'statement : WHILE LPAREN condition RPAREN LBRACE statement RBRACE'
    p[0] = ('while', p[3], p[6])

def p_condition(p):
    'condition : ID OPERATOR expression'
    p[0] = (p[2], p[1], p[3])

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_statement_expr(p):
    'statement : ID'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(tabmodule='_while_loop_parsetab', errorlog=yacc.NullLogger())
