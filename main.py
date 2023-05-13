from ihLang.tokenize import tokenize
from ihLang.parsing import parse_program
from ihLang.semanticAnalysis import perform_semantic_analysis
from ihLang.bashCodeGeneration import generate_bash_code


# Example ihLang code
ihlang_code = '''
z = 1;
x = 10 + 11 + 11 * 10;
a = z * x + 100;
print x;
'''

# Compile and execute the ihLang code
try:
    tokens = tokenize(ihlang_code)
    print(tokens)
    ast = parse_program(tokens)
    print(ast)
    perform_semantic_analysis(ast)
    bash_code = generate_bash_code(ast)
    print("Generated Bash code:")
    print(bash_code)
except Exception as e:
    print("Semantic Error:", str(e))
