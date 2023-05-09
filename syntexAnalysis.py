import graphviz
def parse(tokens):
    token_index = 0

    def match(token_name):
        nonlocal token_index
        if token_index < len(tokens) and tokens[token_index][0] == token_name:
            token_index += 1
        else:
            raise SyntaxError("Expected token: " + token_name)

    def stmt():
        match('IDENTIFIER')
        match('ASSIGN')
        expr_node = expr()  # Store the result of expr() in a variable
        match('SEMICOLON')

        stmt_node = {
            'type': 'stmt',
            'children': [
                {'type': 'ID', 'value': tokens[0][1]},
                {'type': 'ASSIGN'},
                expr_node,  # Add expr_node to children list
                {'type': 'SEMICOLON'}
            ]
        }
        return stmt_node

    def expr():
        node = {'type': 'expr', 'children': []}
        term_node = term()
        node['children'].append(term_node)

        if token_index < len(tokens) and tokens[token_index][0] == 'PLUS':
            match('PLUS')
            expr_node = expr()
            node['children'].append({'type': 'PLUS'})
            node['children'].append(expr_node)

        return node

    def term():
        node = {'type': 'term', 'children': []}
        factor_node = factor()
        node['children'].append(factor_node)

        if token_index < len(tokens) and tokens[token_index][0] == 'MULTIPLY':
            match('MULTIPLY')
            term_node = term()
            node['children'].append({'type': 'MULTIPLY'})
            node['children'].append(term_node)

        return node

    def factor():
        if token_index < len(tokens) and tokens[token_index][0] == 'LPAREN':
            match('LPAREN')
            expr_node = expr()
            match('RPAREN')
            return expr_node
        elif token_index < len(tokens) and tokens[token_index][0] in ['IDENTIFIER', 'INT']:
            token = tokens[token_index]
            match(token[0])
            if token[0] == 'IDENTIFIER':
                return {'type': 'factor', 'children': [{'type': token[0], 'value': token[1]}]}
            else:  # token[0] == 'INT'
                return {'type': 'factor', 'children': [{'type': token[0], 'value': int(token[1])}]}



    parse_tree = stmt()
    return parse_tree




import matplotlib.pyplot as plt

def visualize_parse_tree(parse_tree):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    def traverse(node, x, y, dx, dy):
        node_type = node['type']
        if node_type in ['stmt', 'expr', 'term', 'factor']:
            node_label = node_type
        else:
            node_label = f"{node_type}({node.get('value', '')})"

        ax.text(x, y, node_label, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

        children = node.get('children', [])
        num_children = len(children)

        if num_children > 0:
            dx /= num_children
            x -= dx * (num_children - 1) / 2
            y -= dy
            for child in children:
                traverse(child, x, y, dx, dy)
                x += dx
            x -= dx * (num_children - 1) / 2
            y += dy

            for child in children:
                ax.plot([x, x + dx], [y, y + dy], 'k-')
                x += dx

    traverse(parse_tree, 0, 0, 1, -1)

    plt.show()

# tokens = [('IDENTIFIER', 'x'), ('ASSIGN', '='), ('INT', '10'), ('PLUS', '+'), ('INT', '5'), ('SEMICOLON', ';')]
from lexicalAnalysis import tokenize

# program = "x = 10 + 5;"
program = "x = 10 + 5 * 5; y = x + 3; z = x + y;"
tokens = tokenize(program)
parse_tree = parse(tokens)
print(parse_tree)




