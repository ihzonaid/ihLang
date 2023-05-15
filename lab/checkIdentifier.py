import re

identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'


def isIdentifier(word):
    return True if re.match(identifier_pattern, test_word) else False