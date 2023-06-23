# Simple Compiler design with code for (IhLang)

একটি সিম্পল কম্পাইলার বানানোর আগে, আগে জেনে নিই Compiler কি, কি  কাজ করে , কিভাবে কাজ করে?

আমরা যদি C  প্রোগ্রামিং ল্যাঙ্গয়েজ এর Code দেখি,

```jsx
#include<stdio.h>

int main() {
	int x = 20;

	return x;
}

```

আমরা আগে থেকেই জানি কম্পিঊটার এই সব কোড কোন কিছুই সরাসরি বুজে না, 

এটাকে অনুবাধ করে মেশিন ভাষায় নিতে হয়, তবেই কম্পিউটার/ মেশিন বুজতে পারে।

এই অনুবাদ করার কাজটা যে করে থাকে তাকে কম্পাইলার বলে।

কিভাবে কম্পাইলার এই কাজটা করে?

```jsx
#include<stdio.h>

int main() {
	int x = 20;
	return x;
}

```

কম্পাইলার একটি পাইপলাইন প্রক্রিয়া। প্রথমে একটি স্ক্যানার ব্যবহার করে প্রোগ্রামের বিভিন্ন টোকেন (Token) নির্ধারণ করে। তারপর সিনট্যাক্স বিশ্লেষণ (Syntax Analysis) করা হয়। সিনট্যাক্স বিশ্লেষণ করা হয় যাতে  কোনও ত্রুটি না থাকে এবং প্রোগ্রামের স্ট্রাকচার সঠিক হয়। এরপর সেটি অনুবাধ করা হয় এবং সম্পর্কিত বাইনারি কোড বা মেশিন কোড তৈরি করা হয়।

সম্পর্কিত বাইনারি কোড  বা মেশিন কোড তৈরি করার পরে, কম্পাইলার একটি লিঙ্কার ব্যবহার করে একটি একক বাইনারি ফাইল তৈরি করে। এই ফাইলটি কম্পিউটারে লোড করা যায় এবং সেটি চালানো হয়।

কম্পাইলারের প্রক্রিয়াটি শুরু থেকে শেষ পর্যন্ত অনেকটা একটি পাইপলাইন প্রক্রিয়ার মতো। একটি স্টেপের পরে আরেকটি স্টেপ অনুসরণ করে এবং পর্যালোচনা করে।

## Clearly Define problem and goal

আমাদের goal হচ্ছে , আমরা একটা কম্পাইলার ডিজাইন করতে চাই। এটাকে আরো একটু সহজ ভাষায় বললে, আমরা চাই আমাদের নিজের একটা প্রোগ্রামিং ল্যাংগুয়েজ যা কম্পিঊটার বুজতে পারবে।

ধরি নতুন একটি সহজ এবং সাধারন ল্যাংগুয়েজ (Language) হলো ihLang. নিচে এই ভাষায় লিখিত একটা Demo প্রোগ্রাম দেওয়া হলো ,আমরা চাই এই ভাষায় লিখিত প্রোগাম যাতে মেশিন ভাষায় অনুবাদিত হয়। 

```jsx
x = 21;
y = 20;
z = x + y;
a = x * y;
b = z / y;
print x;
print 10;
```

অর্থাৎ 0 and 1 বা  বাইনারি কোড  বা মেশিন কোড এ পরিনয় হয়। বুঝার সুবিধার জন্য আমরা চাই আমাদের ভাষা যাতে Bash ভাষায় রুপান্তরিত হয়। 

আমরা আমাদের প্রবলেম define করতে পারলাম। 

### এখন প্রবলেম এর  সমাধান এ কিভাবে যাবো?

একটা ভাষাকে অন্য ভাষায় কম্পাইল করা সহজ কোন প্রবলেম না, এটা অনেক Complex একটা প্রবলেম, কিন্তু আমার উদ্দেশ্য থাকবে  যত সহজে কম্পাইলার overall কিভাবে কাজ করে উপস্থাপন করা যায়।

আমরা কিভাবে এই প্রবলেম এর সমাধান চিন্তা করতে পারি? আমি আপানাদের আমার সাথে এই প্রবলেম এর সমাধান কিভাবে চিন্তা করতে হয়, তা দেখানোর চেষ্টা করবো, আমার উদ্দেশ্য থাকবে কত সহজে এই কঠিন কম্পাইলার ডিজাইন জিনিসটা আপনাদের সামনে উপস্থাপন করা যায়, আমি একটা overall thought process দেখানোর ট্রাই করবো।
আমি এখানে শুধু কম্পাইলার ডিজাইনের কঠিন concept দিয়ে আপনাদের bore করতে চাই না।

আমি আবারও বলছি, আমাদের বড় প্রবলেম define করা শেষ। 

এই প্রবলেম টা সমাধান করার জন্য, এখন প্রথমে দেখতে হবে নতুন প্রোগ্রামিং ভাষার দিকে। যে সহজ এবং সিম্পল ভাষা ihLang কথা বলেছিলাম, এটার Syntax কেমন হবে, এটার কি কি ফিচার থাকবে? 

ihLang এ কি কি ফিচার থাকবে এটা ভালো করে বুজলে আমাদের প্রবলেমটা সমাধান করা সহজ হবে। তাহলে এখন ihLang এর ফিচার ডিফাইন করি

**ihLang এর ফিচারসমুহ**

- আমারা  variable এ দশমিক সংখ্যা (integer) রাখতে  পারবো।

```jsx
x = 20;
```

- variable এ দশমিক সংখ্যা (integer) নিজেদের মধ্যে যোগ, বিয়োগ, গুন, ভাগ , করে রাখতে পারবো।

```jsx
x = 20 + 30;
y = 40 - 20;
```

- variable গুলোর যোগ, বিয়োগ, গুন ভাগ করতে পারবো এবং অন্য variable এ save করতে পাড়বও।

```jsx
z = x + y;
```

- variable এর সাথে অন্য Integer যোগ, বিয়োগ, গুন ভাগ করে , অন্য variable এ রাখা যাবে।
- প্রতিটি লাইন “;” দিয়ে শেষ করতে হবে।
- আমরা কোন কিছু terminal এ প্রিন্ট করার জন্য print statement ব্যবহার করতে পাররো। syntax টা হবে
    - print এর পরে হয় variable অথবা কোন সখ্যা দিতে পারবো।
    
    ```jsx
    print x;
    print 10;
    ```
    

ihLang এ কি করতে পারবো না?

- আমরা বাকি সব কিছুই আমাদের প্রোগাম দিয়ে করতে পারবো না, যেমন loop, if condition, function , class.

এখন ihLang কোড এর কোন word কি বুজায়, এটা বুজতে হবে, যেমন 

- `x, y, words, z` এগুলো হচ্ছে variable or identifier.
- `=` হচ্ছে assignment operator
- `+ , - , * , /` হচ্ছে calculation operator.
- `print` একটা function or print statement.

code এর এই অংশগুলো আলাদা করে label করাকেই  বলে Tokenization।

কম্পাইলার automatic এইসব variable, operator আলাদা করতে পারবে না। এগুলোর আলাদাভাবে চেনানোর জন্য আমাদের regular expression লিখতে হবে, যাতে কম্পাইলার  বুঝতে পারে। নিচে কিছু প্যাটার্ন দেওয়া আছে, Tokenize করার জন্য

```jsx
token_patterns = [
    (r'print', 'PRINT'),  # Print keyword
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Variable identifiers
    (r'\d+', 'NUMBER'),  # Numbers
    (r'\+', 'PLUS'),  # Addition operator
    (r'-', 'MINUS'),  # Subtraction operator
    (r'\*', 'MULTIPLY'),  # Multiplication operator
    (r'/', 'DIVIDE'),  # Division operator
    (r'=', 'ASSIGN'),  # Assignment operator
    (r';', 'SEMICOLON'),  # Semicolon
    (r'\s+', 'SKIP'),  # Skip whitespace
]
```

যদি লিখিত প্রোগ্রামে কোন অংশ যদি কোন প্যাটার্নের সাথে না মিলে, তখন কম্পাইলার কোডকে Tokenize করতে পারবে না। তাই কোড ihLang এর ব্যবহৃত Token rule এর সাথে মিলতে হবে। যেমন, যদি আমাদের ihLang এ কিন্তু  @ এর কোন ব্যবহার নেই, তাই   এ  @  কোড এ থাকলে নিশ্চয় ভুল, কম্পাইলার এটা tokenize করতে পারবে না।

### Tokenization **(Lexical Analysis)**

Tokenization করার পরে, ihLang এর এই কোড,

```jsx
x = 30;
x = x + 20;
```

এমনভাবে প্রতিটি word বা অংশ  টুকেন এ পরিনত হবে।

```jsx
[
	('IDENTIFIER', 'x'),
	('ASSIGN', '='),
	('INT', '30'),
	('SEMICOLON', ';'), 
	('IDENTIFIER', 'y'),
	('ASSIGN', '='),
	('IDENTIFIER', 'x'), 
	('PLUS', '+'), 
	('INT', '20'), 
	('SEMICOLON', ';')
]
```

এভাবে Tokenization করার পরবর্তি খাপে, এই Tokens গুলোকে একটা একটা করে read করার পর, কম্পাইলের বুজতে হবে Syntactically কোন ভুল আছে কিনা?

এই Tokenization এই পরে কোনভাবে বলা সম্ভব যে , লিখিত ihLang কোড এর সব Syntax ঠিক আছে. কারন  আমরা দেখেছি আগের ধাপে Compiler শুধু প্রতিটি ওয়ার্ড কে আলাদা করে। সেখানে syntax checking ছিলো না যে, এই কোড আধৌ আমাদের ihLang এর যে Syntax আছে, তা ফলো করে কিনা। যেমনঃ

```jsx
x = 30; 
30 = x;
```

এই কোডকে কিন্তু Tokenize করা যাবে, কিন্তু এই কোড আমাদের ihLang এর নিয়ম (Syntax) ফলো করে না, এই কোড এর last line এ `30 = x` এইটা ihLang এর Syntax  এর সাথে মিলে না। আর কোড যদি এই syntax না মানে তাহলে কম্পাইলার কিন্তু এই প্রোগ্রাম কম্পাইল complete করতে পারবে না। 

তাই কম্পাইলেরকে দেখতে হবে যে লিখিত কোড  ihLang Rule মানে কিনা, তার জন্য ihLang এর কিছু Rule কম্পাইল বানানোর সময় কম্পাইলারকে  বলে দিতে হবে। আমরা আগেই দেখেছি ihLang এর ফিচার বা Rule বা নিয়মগুলো কেমন হবে। কিন্তু কম্পাইলারকে বুঝানোর জন্য CFG (context free grammar) or other grammar rule লিখতে হয়।

এবং এই গ্রামার বা নিয়ম দিয়েই পরে কম্পাইলার একটা একটা টুকেন পড়ে এবং  check করে যে, ihLang এর code এই রুল সব মানে কিনা, এবং AST(Abstract Syntax Tree) তৈরি করে, 

Code যদি Syntax  না মানে তাহলে কম্পাইলার  ভুল ধরতে পারে।

আর এই  ধাপটাকেই বলে Syntax Analysis Phase।

### CFG (Context Free Grammar)

ihLang এর CFG বা (Context Free Grammar) এমন  হবে। আগের বর্নিত নিয়ম গুলোই এখানে CFG এর মাধ্যমে দেখানো হয়েছে 

```jsx
<program> ::= <statement_list>

<statement_list> ::= <statement> <statement_list> | <statement>

<statement> ::= <assignment_statement> | <print_statement>

<assignment_statement> ::= <identifier> "=" <expression> ";"

<print_statement> ::= "print" <expression> ";"

<expression> ::= <term> | <term> <add_operator> <expression>

<term> ::= <factor> | <factor> <mul_operator> <term>

<factor> ::= <number> | <identifier>

<add_operator> ::= "+" | "-"

<mul_operator> ::= "*" | "/"

<identifier> ::= [a-zA-Z_][a-zA-Z0-9_]*

<number> ::= [0-9]+
```

সহজ করে কিছু গ্রামার নিয়ে বললে, 

- কোন Code এ কোন কিছু alphabet দিয়ে শুরু হলে তা আমরা variable বা identifier হিসেবে দেখবো।
- কোন variable or identifier এর পরে আমরা সবসময় দেখি `=` রয়েছে, এই এইটাই CFG এর এই লাইনে বলা হয়েছে।
    
    ```jsx
    <assignment_statement> ::= <identifier> "=" <expression> ";"
    ```
    
- বাক্যের শেষে সেমিকোলন থাকবে, এরকম কিছু grammar বা Rule এখানে লেখা হয়েছে।

এই ধাপে Syntax check করার পাশাপাশি, আগের ধাপে পাওয়া Token নিয়ে  একটা ট্রি তৈরি করা হয়।

কিন্তু প্রশ্ন  হচ্ছে, টুকেন থেকে আমরা AST তৈরি করলাম, কেন? আমরা কি এটাকে আরো জটিল করে দিলাম? কিন্তু বিষয়টা এমন না, এই টুকেন থেকে যখন AST বানানো হয়, তখন আমাদের ihLang এর rule অনুযায়ি কি কি সেস্টমেন্ট রয়েছে এবং কোন অপারেশন আগে হবে, কোন অপারেশন পরে হবে, কোন অপারেশন না করে আমরা অন্য অপারেশন করতে পারব না, এই সব কিছু এই AST এর মাধ্যমে রিপ্রেজেন্ট করা হয়।

পরবর্তি ধাপে মেশিন কোড বা অন্য কোন কোড এ রুপান্তর করার সময় , এই AST ট্টি ট্রাভার্স করেই আমরা অন্য কোড এ রুপান্তর করতে হয়।

কিন্তু মেশিন কোড জেনারেশনের  আগেই একটা প্রবলেম হচ্ছে, যেমনঃ 

```jsx
x = y + 10;
```

এই কোড এ দেখা যাচ্ছে, y এর সাথে ১০ যোগ করে x এ assign করা হচ্ছে, কিন্তু এখানে প্রবলেম হচ্ছে, কোড এ আগে কোথাও x নেই।

এই কোড টুকেনাইজ ত হবেই, এটা থেকে AST ও বানানো যাবে, কিছু এখানে error টা  না Lexical, না Syntactically, বরং এটা Semantically error.

তাই এই ধরনের Semantic error ধরার জন্য কম্পাইলারের Semantic Analysis করতে হয়। 

 

### Semantic Analysis Phase

এই ধাপে , কম্পাইলের Semantic error analysis করে, আমাদের ihLang এর ক্ষেত্রে Semantic Error গুলো হতে পারে এমন

```jsx
print x; // x is not initialized
x = 10 + y; // y is not initiazed
```

এই ভুল গুলোই আমরা এই Semantic analysis phase এ check করে থাকি। Semantic Analysis Phase কোড 

```jsx
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
```

আমরা এখানে variable initialized কিনা এখানে এটাই check করি।

এখন এই ধাপের পরে, আমরা বলতে পারি, আমাদের code এর AST, Syntactically and Semantically ঠিক আছে, আর কোন ধাপের যেকোন ভুল কম্পাইলার ভুল দেখলে কত নম্বর লাইলে ভুল হয়েছে, এবং কি ধরনের ভুল হয়েছে তা প্রিন্ট করে, কম্পাইলেশন অফ করে দিবে। 

এখন এর পরে আসে Code Generation

### Code Generation

কম্পাইলার এই ধাপে, আমি আগেই বলেছি, AST থেকে মেশিন ভাষায় বা  অন্য কোন ভাষায় রুপান্তর করে, এই খাপে, AST Tree Traverse করার মাধ্যমে, এই কোডকে অন্য ভাষার syntax অনুযায়ি ঐ ভাষায় translate করে।

এখানে ihLang এর কোড Bash এ রুপান্তরের কোড দেখানো হলো।

```jsx
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
```

Bravo, you made it last of the blog. hope you learned somethings from this.

## Canva Slide

[Compiler Design](https://www.canva.com/design/DAFi8nXNANo/u5CtZuVODs-9Ge3oHEr6kw/edit?analyticsCorrelationId=e9b707ec-281d-4de6-b7b4-7c14a8cd6a8e)

## Code

[https://github.com/ihzonaid/ihLang](https://github.com/ihzonaid/ihLang)