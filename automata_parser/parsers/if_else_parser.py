import ply.yacc as yacc
from automata_parser.lexers.if_else_lexer import tokens

def p_statement_if_else(p):
    'statement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE'
    p[0] = ('if-else', p[3], p[6], p[10])

def p_statement_if(p):
    'statement : IF LPAREN condition RPAREN LBRACE statement RBRACE'
    p[0] = ('if', p[3], p[6])

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

parser = yacc.yacc(tabmodule='_if_else_parsetab', errorlog=yacc.NullLogger())
