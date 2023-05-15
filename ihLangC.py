from ihLang.tokenize import tokenize
from ihLang.parsing import parse_program
from ihLang.semanticAnalysis import perform_semantic_analysis
from ihLang.bashCodeGeneration import generate_bash_code
import sys
import os


def process_ihlang_file(filename, output_filename):
    with open(filename, 'r') as file:
        ihlang_code = file.read()

    try:
        tokens = tokenize(ihlang_code)
        ast = parse_program(tokens)
        perform_semantic_analysis(ast)
        bash_code = generate_bash_code(ast)

        if output_filename is None:
            # Generate output filename if not provided
            base_filename = os.path.splitext(filename)[0]
            output_filename = base_filename + '.bash'

        with open(output_filename, 'w') as file:
            file.write(bash_code)

        print(f"Generated Bash code: {output_filename}")

    except Exception as e:
        print("Semantic Error:", str(e))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ihlang_compiler.py <ih_file> [-o <output_file>]")
        sys.exit(1)

    ih_filename = sys.argv[1]
    output_filename = None

    if len(sys.argv) >= 4 and sys.argv[2] == '-o':
        output_filename = sys.argv[3]

    process_ihlang_file(ih_filename, output_filename)
