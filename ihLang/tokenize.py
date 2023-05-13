import re

# Define the regular expressions for tokens
token_patterns = [
    (r'print', 'PRINT'),  # Print keyword
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Variable identifiers
    (r'\d+', 'NUMBER'),  # Numbers
    (r'\+', 'PLUS'),  # Addition operator
    (r'-', 'MINUS'),  # Subtraction operator
    (r'\*', 'MULTIPLY'),  # Multiplication operator
    (r'/', 'DIVIDE'),  # Division operator
    (r'=', 'ASSIGN'),  # Assignment operator
    (r';', 'SEMICOLON'),  # Semicolon
    (r'\s+', 'SKIP'),  # Skip whitespace
]


def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None

        # Try to match the token patterns
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                if token_type != 'SKIP':
                    tokens.append((value, token_type))
                break

        if not match:
            raise Exception('Invalid token at position ' + str(position))

        position = match.end()

    return tokens
