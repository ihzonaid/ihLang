# Define symbol table for variable tracking
symbol_table = {}

def analyze_semantics(parse_tree):
    def visit(node):
        if node['type'] == 'stmt':
            visit_stmt(node)
        elif node['type'] == 'expr':
            visit_expr(node)
        elif node['type'] == 'term':
            visit_term(node)
        elif node['type'] == 'factor':
            visit_factor(node)

    def visit_stmt(node):
        identifier = node['children'][0]['value']
        if identifier in symbol_table:
            raise SemanticError("Variable already declared: " + identifier)
        symbol_table[identifier] = 'int'  # Assume all variables are of type int
        visit(node['children'][2])

    def visit_expr(node):
        visit_term(node['children'][0])
        if len(node['children']) == 3:
            visit(node['children'][2])

    def visit_term(node):
        visit_factor(node['children'][0])
        if len(node['children']) == 3:
            visit(node['children'][2])

    def visit_factor(node):
        if node['children'][0]['type'] == 'ID':
            identifier = node['children'][0]['value']
            if identifier not in symbol_table:
                raise SemanticError("Variable not declared: " + identifier)
        visit(node['children'][0])

    # Start semantic analysis from the root of the parse tree
    visit(parse_tree)

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

analyze_semantics(parse_tree)
