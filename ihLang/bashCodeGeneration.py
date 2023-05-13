def generate_bash_code(ast):
    bash_code = ""

    for statement in ast:
        if statement['type'] == 'assignment':
            bash_code += f"{statement['identifier']}={generate_expression_code(statement['expression'])}\n"
        elif statement['type'] == 'print':
            bash_code += f"echo {generate_expression_code(statement['expression'])}\n"

    return bash_code


def generate_expression_code(expression):
    if expression['type'] == 'number':
        return str(expression['value'])
    elif expression['type'] == 'identifier':
        return f"${{{expression['name']}}}"
    elif expression['type'] == 'binary_operation':
        left_code = generate_expression_code(expression['left'])
        right_code = generate_expression_code(expression['right'])
        operator = expression['operator']
        return f"(({left_code} {operator} {right_code}))"
