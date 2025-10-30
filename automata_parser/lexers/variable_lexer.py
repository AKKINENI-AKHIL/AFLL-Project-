import ply.lex as lex

tokens = (
    'ID',
    'NUMBER',
    'EQUALS',
    'STRING',
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_EQUALS = r'='
t_STRING = r'\".*?\"'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
