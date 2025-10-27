import ply.lex as lex

reserved = {
    'while': 'WHILE'
}

tokens = [
    'ID', 'NUMBER', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'OPERATOR'
] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_OPERATOR = r'==|!=|<|>|<=|>='
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
