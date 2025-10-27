from automata_parser.lexers.if_else_lexer import lexer as if_else_lexer
from automata_parser.parsers.if_else_parser import parser as if_else_parser
from automata_parser.lexers.for_loop_lexer import lexer as for_loop_lexer
from automata_parser.parsers.for_loop_parser import parser as for_loop_parser
from automata_parser.lexers.while_loop_lexer import lexer as while_loop_lexer
from automata_parser.parsers.while_loop_parser import parser as while_loop_parser
from automata_parser.lexers.array_lexer import lexer as array_lexer
from automata_parser.parsers.array_parser import parser as array_parser
from automata_parser.lexers.variable_lexer import lexer as variable_lexer
from automata_parser.parsers.variable_parser import parser as variable_parser

def main():
    while True:
        try:
            s = input('Enter a statement: ')
        except EOFError:
            break
        if not s:
            continue

        if s.strip().startswith('if'):
            result = if_else_parser.parse(s, lexer=if_else_lexer)
            if result:
                print("✅ Valid IF condition")
            else:
                print("❌ Syntax error in IF construct")
        elif s.strip().startswith('for'):
            result = for_loop_parser.parse(s, lexer=for_loop_lexer)
            if result:
                print("✅ Valid FOR loop")
            else:
                print("❌ Syntax error in FOR construct")
        elif s.strip().startswith('while'):
            result = while_loop_parser.parse(s, lexer=while_loop_lexer)
            if result:
                print("✅ Valid WHILE loop")
            else:
                print("❌ Syntax error in WHILE construct")
        elif '[' in s and ']' in s:
            result = array_parser.parse(s, lexer=array_lexer)
            if result:
                print("✅ Valid ARRAY declaration")
            else:
                print("❌ Syntax error in ARRAY construct")
        elif '=' in s:
            result = variable_parser.parse(s, lexer=variable_lexer)
            if result:
                print("✅ Valid VARIABLE declaration")
            else:
                print("❌ Syntax error in VARIABLE declaration")
        else:
            print("❌ Unknown construct")

if __name__ == '__main__':
    main()
