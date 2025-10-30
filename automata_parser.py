
import re

def check_if_else(code):
    """
    Checks the syntax of an if-else statement.
    Valid syntax: if (condition) { body } else { body }
    """
    # Simplified regex for demonstration
    pattern = re.compile(r'^if\s*\([^)]+\)\s*\{[^}]*\}\s*else\s*\{[^}]*\}$')
    return pattern.match(code) is not None

def check_for_loop(code):
    """
    Checks the syntax of a for loop.
    Valid syntax: for (initialization; condition; increment) { body }
    """
    pattern = re.compile(r'^for\s*\([^;]+;[^;]+;[^)]+\)\s*\{[^}]*\}$')
    return pattern.match(code) is not None

def check_while_loop(code):
    """
    Checks the syntax of a while loop.
    Valid syntax: while (condition) { body }
    """
    pattern = re.compile(r'^while\s*\([^)]+\)\s*\{[^}]*\}$')
    return pattern.match(code) is not None

def check_array_declaration(code):
    """
    Checks the syntax of an array declaration.
    Valid syntax: type[] arrayName = {value1, value2, ...};
    """
    pattern = re.compile(r'^\w+\[\]\s+\w+\s*=\s*\{[^}]*\};$')
    return pattern.match(code) is not None

def check_variable_declaration(code):
    """
    Checks the syntax of a variable declaration.
    Valid syntax: type variableName = value;
    """
    pattern = re.compile(r'^\w+\s+\w+\s*=\s*\S[^;]*;$')
    return pattern.match(code) is not None

if __name__ == '__main__':
    # Test cases
    test_cases = {
        'if-else': [
            ('if (x > 0) { x = 1; } else { x = -1; }', True),
            ('if(x>0){x=1;}else{x=-1;}', True),
            ('if (x > 0) { x = 1; }', False),
            ('if (x > 0) else { x = -1; }', False),
        ],
        'for-loop': [
            ('for (int i = 0; i < 10; i++) { sum += i; }', True),
            ('for(int i=0;i<10;i++){sum+=i;}', True),
            ('for (int i = 0; i < 10) { sum += i; }', False),
            ('for (i < 10; i++) { sum += i; }', False),
        ],
        'while-loop': [
            ('while (x < 10) { x++; }', True),
            ('while(x<10){x++;}', True),
            ('while { x++; }', False),
            ('while (x < 10) x++;', False),
        ],
        'array-declaration': [
            ('int[] arr = {1, 2, 3};', True),
            ('string[] names = {"a", "b"};', True),
            ('int arr = {1, 2, 3};', False),
            ('int[] arr = 1, 2, 3;', False),
        ],
        'variable-declaration': [
            ('int x = 5;', True),
            ('string name = "test";', True),
            ('int x = ;', False),
            ('int x 5;', False),
        ]
    }

    for construct, cases in test_cases.items():
        print(f'--- Testing {construct} ---')
        for code, expected in cases:
            checker_func = {
                'if-else': check_if_else,
                'for-loop': check_for_loop,
                'while-loop': check_while_loop,
                'array-declaration': check_array_declaration,
                'variable-declaration': check_variable_declaration
            }[construct]

            result = checker_func(code)
            status = 'Pass' if result == expected else 'Fail'
            print(f'Code: "{code}"\nExpected: {expected}, Got: {result} -> {status}\n')
