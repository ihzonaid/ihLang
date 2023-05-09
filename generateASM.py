def generate_code(parse_tree):
    asm_code = ""

    def visit(node):
        nonlocal asm_code
        if node['type'] == 'stmt':
            asm_code += visit_stmt(node)
        elif node['type'] == 'expr':
            asm_code += visit_expr(node)
        elif node['type'] == 'term':
            asm_code += visit_term(node)
        elif node['type'] == 'factor':
            asm_code += visit_factor(node)

    def visit_stmt(node):
        nonlocal asm_code
        identifier = node['children'][0]['value']
        expr_code = visit(node['children'][2])
        if expr_code is not None:
            return f"STORE {expr_code} {identifier}\n"
        return ""

    def visit_expr(node):
        nonlocal asm_code
        term_code = visit(node['children'][0]['children'][0])
        if len(node['children']) == 3:
            expr_code = visit(node['children'][2])
            temp_var = generate_temp_var()
            asm_code += f"ADD {term_code} {expr_code} {temp_var}\n"
            return temp_var
        else:
            return term_code

    def visit_term(node):
        nonlocal asm_code
        factor_code = visit(node['children'][0])
        if len(node['children']) == 3:
            term_code = visit(node['children'][2])
            temp_var = generate_temp_var()
            asm_code += f"MUL {factor_code} {term_code} {temp_var}\n"
            return temp_var
        else:
            return factor_code

    def visit_factor(node):
        nonlocal asm_code
        if node['children'][0]['type'] == 'ID':
            identifier = node['children'][0]['value']
            return identifier
        elif node['children'][0]['type'] == 'INT':
            return node['children'][0]['value']

    def generate_temp_var():
        nonlocal asm_code
        # Generate a unique temporary variable name
        # This is just a placeholder implementation for demonstration purposes
        return "T" + str(generate_temp_var.counter)
    generate_temp_var.counter = 0

    # Start code generation from the root of the parse tree
    visit(parse_tree)

    return asm_code

# Example usage
parse_tree = {
    'type': 'stmt',
    'children': [
        {'type': 'ID', 'value': 'x'},
        {'type': 'ASSIGN'},
        {
            'type': 'expr',
            'children': [
                {
                    'type': 'term',
                    'children': [
                        {'type': 'factor', 'children': [{'type': 'ID', 'value': 'y'}]},
                        {'type': 'MULTIPLY'},
                        {'type': 'factor', 'children': [{'type': 'INT', 'value': '2'}]}
                    ]
                }
            ]
        },
        {'type': 'SEMICOLON'}
    ]
}

assembly_code = generate_code(parse_tree)
print(assembly_code)
