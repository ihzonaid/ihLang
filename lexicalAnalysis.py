import re
# Define regular expressions for tokens
token_patterns = [
    ('INT', r'\d+'),  # Integer literal
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifier
    ('PLUS', r'\+'),  # Plus operator
    ('MULTIPLY', r'\*'),  # Multiply operator
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('ASSIGN', r'='),  # Assignment operator
    ('SEMICOLON', r';'),  # Semicolon
    ('EQUALS', r'=='),  # Equals sign
    ('WHITESPACE', r'\s+'),  # Whitespace
]


def tokenize(program):
    tokens = []
    while program:
        match = None
        for token_name, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(program)
            if match:
                token_value = match.group(0)
                if token_name != 'WHITESPACE':  # Skip whitespace tokens
                    tokens.append((token_name, token_value))
                program = program[len(token_value):]
                break
        if not match:
            program = program[1:]  # Skip unrecognized characters
    return tokens


# Example usage
program = "x = 10 + 5;"
tokens = tokenize(program)
print(tokens)
