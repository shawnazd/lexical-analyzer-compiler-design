# 🔍 Lexical Analyzer — Compiler Design Assignment

A lexical analyzer (scanner) implemented in **Python** for a simplified programming language.  
This is the first stage of a compiler — it reads raw source code and converts it into a stream of meaningful **tokens**.

---

## 📁 Repository Structure

```
lexical-analyzer-compiler-design/
│
├── lexer.py                  # Main lexical analyzer source code
│
├── diagrams/
│   └── Transition Diagram.jpg   # FSM transition diagram for all tokens
│
├── test_cases/
│   ├── testcase1.png         # Output screenshot — Basic Declarations
│   ├── testcase2.png         # Output screenshot — Expressions with String & Operators
│   └── testcase3.png         # Output screenshot — All Tokens + Error Handling
│
└── README.md
```

---

## 📌 What is a Lexical Analyzer?

A **lexical analyzer** (also called a *scanner* or *tokenizer*) is the first phase of a compiler. It reads source code character by character and groups them into meaningful units called **tokens**.

Each token has:
- A **type** (e.g., `KEYWORD`, `IDENTIFIER`, `NUMBER`)
- A **lexeme** — the actual string from the source code

**Example:** For the input `int x = 10;`, the lexer produces:
```
<KEYWORD, int>
<IDENTIFIER, x>
<OPERATOR, =>
<NUMBER, 10>
<DELIMITER, ;>
```

---

## 🧩 Supported Token Types

| Token Type   | Examples                          | Rule / Pattern                                  |
|--------------|-----------------------------------|-------------------------------------------------|
| `KEYWORD`    | `int`, `float`, `if`, `while`     | Fixed reserved words                            |
| `IDENTIFIER` | `x`, `count`, `myVar`             | Letter/underscore followed by letters/digits    |
| `NUMBER`     | `0`, `42`, `3.14`                 | Integer or decimal literal                      |
| `STRING`     | `"hello"`                         | Characters enclosed in double quotes            |
| `OPERATOR`   | `+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=` | Arithmetic and comparison operators |
| `DELIMITER`  | `(`, `)`, `{`, `}`, `[`, `]`, `,`, `;`, `:` | Punctuation and grouping symbols |
| `COMMENT`    | `// this is a comment`            | From `//` to end of line                        |

> Whitespace (spaces, tabs, newlines) is **ignored** between tokens.

### Keywords Recognized
```
int  float  if  else  while  return  void  char  bool  for  break  continue  string
```

---

## 🔄 Transition Diagram

The finite state machine (FSM) used to recognize all tokens is documented in:

```
diagrams/Transition Diagram.jpg
```

The diagram covers all token types: keywords/identifiers, numbers (integer & float), strings, operators (single and multi-character), delimiters, and comments.

---

## ▶️ How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/shawnazd/lexical-analyzer-compiler-design.git
   cd lexical-analyzer-compiler-design
   ```

2. Create a file named `test.txt` in the same directory as `lexer.py` and write your source code inside it.

3. Run the lexer:
   ```bash
   python lexer.py
   ```

4. The tokenized output will be printed to the terminal.

---

## 🧪 Test Cases

### Test Case 1 — Basic Declarations

**Input (`test.txt`):**
```
int x = 10;
```

**Output:**

```

📸 Screenshot: `test_cases/testcase1.png`

---

### Test Case 2 — Expressions with String and Operators

**Input (`test.txt`):**
```
float y = 3.14;
if (y >= 3) return "hello";
```

**Output:**


📸 Screenshot: `test_cases/testcase2.png`

---

### Test Case 3 — All Tokens + Error Handling

**Input (`test.txt`):**
```
int x = 5;
string msg = "Hello World
y = x + 2 // this is a comment
$invalid = 10;
```

📸 Screenshot: `test_cases/testcase3.png`

---


## 👤 Author

**Shawnaz**  
GitHub: [@shawnazd](https://github.com/shawnazd)
