# ihLang Compiler

The ihLang Compiler is a simple language compiler that converts ihLang code into Bash script code. It supports `basic variable assignment` and `calculation operations`.

## Features

- Assign values to variables using the syntax: `variable = value`
- Assign calculated values to variables using expressions: `variable = calculated value`
- Perform calculations with a combination of variables and numbers: `y = x + 10`
- Carry out calculations between variables: `z = x + y`
- Print variables or numbers using the `print` function: `print x`

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository:

```shell
  git clone https://github.com/ihzonaid/ihLang.git
```

2. Change into the project directory:

```shell
cd ihLang
```

## Usage

1. Create a new ihLang code file with the extension .ih. For example, example.ih.

2. Write your ihLang code in the file using the supported syntax.

3. Run the ihLang compiler to generate the corresponding Bash code:

```shell
python ihLangC.py demo.ih
```

```shell
python ihLangC.py example.ih -o example.bash
```

This command will generate the example.bash file containing the translated Bash code.

## Examples

Example 1: Variable Assignment and Calculation
ihLang code (example.ih):

```plaintext
x = 10;
y = x + 5;
z = x + y;
print z;
```

Bash code (`example.bash`):

```bash
x=10
y=$((x + 5))
z=$((x + y))
echo $z
```

Example 2: Printing a Number
ihLang code (example.ih):

```plaintext
print 42;
```

Bash code (example.bash):

```bash
echo 42
```

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License.

### Important Link

- [Presentation Canva Link](https://www.canva.com/design/DAFi8nXNANo/u5CtZuVODs-9Ge3oHEr6kw/edit?utm_content=DAFi8nXNANo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- [Written Blog](https://abrasive-boat-cf1.notion.site/Simple-Compiler-design-with-code-for-IhLang-fff96c28197646cd97e16bd9782ce0d5)
