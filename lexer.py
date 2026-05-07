# ============================================================
#  Lexical Analyzer (Scanner)
#  Read source code from test.txt -> output tokens in terminal
# ============================================================

import os
import sys

# ── Token Categories ─────────────────────────────────────────
KEYWORDS = {
    'int', 'float', 'if', 'else', 'while', 'return',
    'void', 'char', 'bool', 'for', 'break', 'continue', 'string'
}

DELIMITERS = set('(){}[];,:')        # fixed: no duplicate, ] included

MULTI_OPS  = ['==', '!=', '<=', '>=']   # checked before single-char ops
SINGLE_OPS = set('+-*/=<>')


# ── Tokenizer ────────────────────────────────────────────────
def tokenize(source):
    tokens = []
    errors = []
    i      = 0
    line   = 1

    while i < len(source):
        c = source[i]

        # newline — track line number
        if c == '\n':
            line += 1
            i += 1
            continue

        # whitespace — skip
        if c in ' \t\r':
            i += 1
            continue

        # single-line comment  // ...
        if source[i:i+2] == '//':
            j = i + 2
            while j < len(source) and source[j] != '\n':
                j += 1
            tokens.append(('COMMENT', source[i:j], line))
            i = j
            continue

        # string literal  "..."
        if c == '"':
            j = i + 1
            while j < len(source) and source[j] != '"' and source[j] != '\n':
                j += 1
            if j < len(source) and source[j] == '"':
                tokens.append(('STRING', source[i:j+1], line))
                i = j + 1
            else:
                errors.append((line, f"Unterminated string: {source[i:i+15]}"))
                i = j
            continue

        # number — integer or float
        if c.isdigit():
            j = i
            while j < len(source) and source[j].isdigit():
                j += 1
            if (j < len(source) and source[j] == '.'
                    and j + 1 < len(source) and source[j+1].isdigit()):
                j += 1
                while j < len(source) and source[j].isdigit():
                    j += 1
            tokens.append(('NUMBER', source[i:j], line))
            i = j
            continue

        # keyword or identifier
        if c.isalpha() or c == '_':
            j = i
            while j < len(source) and (source[j].isalnum() or source[j] == '_'):
                j += 1
            word  = source[i:j]
            ttype = 'KEYWORD' if word in KEYWORDS else 'IDENTIFIER'
            tokens.append((ttype, word, line))
            i = j
            continue

        # multi-character operators  == != <= >=
        matched = False
        for op in MULTI_OPS:
            if source[i:i+2] == op:
                tokens.append(('OPERATOR', op, line))
                i += 2
                matched = True
                break
        if matched:
            continue

        # single-character operator  + - * / = < >
        if c in SINGLE_OPS:
            tokens.append(('OPERATOR', c, line))
            i += 1
            continue

        # delimiter  ( ) { } [ ] ; , :
        if c in DELIMITERS:
            tokens.append(('DELIMITER', c, line))
            i += 1
            continue

        # unrecognized character — report error, keep going
        errors.append((line, f"Unrecognized character: '{c}'"))
        i += 1

    return tokens, errors


# ── Main ─────────────────────────────────────────────────────
def main():
    filename = 'test.txt'

    if not os.path.exists(filename):
        print(f"ERROR: '{filename}' not found.")
        print("Place test.txt in the same folder as lexer.py and run again.")
        sys.exit(1)

    with open(filename, 'r') as f:
        source = f.read()

    tokens, errors = tokenize(source)

    print("========================================")
    print("       LEXICAL ANALYZER OUTPUT")
    print("========================================")

    for ttype, lexeme, lineno in tokens:
        print(f"<{ttype}, {lexeme}>")

    if errors:
        print()
        print("------------- ERRORS ---------------")
        for lineno, msg in errors:
            print(f"[ERROR] Line {lineno}: {msg}")

    print("========================================")
    print(f"  Total Tokens : {len(tokens)}")
    print(f"  Total Errors : {len(errors)}")
    print("========================================")


if __name__ == "__main__":
    main()