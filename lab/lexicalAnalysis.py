import re




x  = """
int x = 10;
"""

words = x.split()

tokens = []


keywords = ["int", "float", "if", "else"]







def isIdentifier(word):
    identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return True if re.match(identifier_pattern, word) else False



for word in words:
    if word == "+":
        tokens.append({"PLUS", "+"})
    elif word == "-":
        tokens.append({"MINUS", "-"})
    elif word == "*":
        tokens.append({"MUL", "*"})
    elif word == "-":
        tokens.append({"DIV", "/"})
    elif word in keywords:
        tokens.append({"KEYWORD", word})
    elif isIdentifier(word):
        tokens.append({"IDENTIFIER", word})


print(tokens)






