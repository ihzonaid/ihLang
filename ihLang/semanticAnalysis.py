def perform_semantic_analysis(ast):
    variable_table = {}

    for statement in ast:
        if statement['type'] == 'assignment':
            identifier = statement['identifier']
            expression = statement['expression']
            evaluate_expression(expression, variable_table)
            variable_table[identifier] = True
        elif statement['type'] == 'print':
            expression = statement['expression']
            evaluate_expression(expression, variable_table)

    # Check for uninitialized variables
    uninitialized_variables = [identifier for identifier,
                               initialized in variable_table.items() if not initialized]
    if uninitialized_variables:
        raise Exception(
            f"Uninitialized variables: {', '.join(uninitialized_variables)}")

    return ast


def evaluate_expression(expression, variable_table):
    if expression['type'] == 'number':
        return
    elif expression['type'] == 'identifier':
        identifier = expression['name']
        if identifier not in variable_table:
            raise Exception(f"Variable '{identifier}' is not initialized")
    elif expression['type'] == 'binary_operation':
        evaluate_expression(expression['left'], variable_table)
        evaluate_expression(expression['right'], variable_table)
