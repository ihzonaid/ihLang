def parse_program(tokens):
    statements = parse_statement_list(tokens)  # line
    return statements


def parse_statement_list(tokens):
    statements = []

    while tokens:
        statement = parse_statement(tokens)
        statements.append(statement)

        if tokens and tokens[0][1] == 'SEMICOLON':
            tokens.pop(0)  # Consume the semicolon token

    return statements


def parse_statement(tokens):
    if tokens[0][1] == 'PRINT':
        tokens.pop(0)  # Consume the 'print' token
        expression = parse_expression(tokens)
        return {'type': 'print', 'expression': expression}
    else:
        identifier_token = tokens.pop(0)
        if identifier_token[1] != 'IDENTIFIER':
            raise SyntaxError('Invalid statement')
        assign_token = tokens.pop(0)
        if assign_token[1] != 'ASSIGN':
            raise SyntaxError('Invalid statement')
        expression = parse_expression(tokens)
        return {'type': 'assignment', 'identifier': identifier_token[0], 'expression': expression}


def parse_expression(tokens):
    term = parse_term(tokens)

    if tokens and tokens[0][1] == 'PLUS':
        tokens.pop(0)  # Consume the '+' token
        expression = parse_expression(tokens)
        return {'type': 'binary_operation', 'operator': '+', 'left': term, 'right': expression}
    elif tokens and tokens[0][1] == 'MINUS':
        tokens.pop(0)  # Consume the '-' token
        expression = parse_expression(tokens)
        return {'type': 'binary_operation', 'operator': '-', 'left': term, 'right': expression}
    else:
        return term


def parse_term(tokens):
    factor = parse_factor(tokens)

    if tokens and (tokens[0][1] == 'MULTIPLY' or tokens[0][1] == 'DIVIDE'):
        operator_token = tokens.pop(0)
        factor2 = parse_factor(tokens)
        factor = {'type': 'binary_operation',
                  'operator': operator_token[0], 'left': factor, 'right': factor2}

    return factor


def parse_factor(tokens):
    token = tokens.pop(0)

    if token[1] == 'NUMBER':
        return {'type': 'number', 'value': int(token[0])}
    elif token[1] == 'IDENTIFIER':
        return {'type': 'identifier', 'name': token[0]}
    else:
        raise SyntaxError('Invalid factor')
