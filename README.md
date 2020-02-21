# Lexical-analysis-using-Python
I was always very facinated of everything about compilers, interpreters, parsers and lexers. Now I was wondering how I could implement such things using Python. I decided to write a simple lexer for algebraic expressions that converts a sequence of characters into a sequence of tokens. Till now I just implemented such things using C or C++ and so I started the simplest way as I learned by reading the Dragon Book.
I created a simple enum type that allows me to create enums as used to from languages like C++ and Java. Then I implemented a Token class that holds all information about a token and enables me to easily print a token using the Python’s magic str method. Finally I added a Lexer class that processes character by character and returns the tokens.
that resulted to lexer.py file
But this code is very long and it took some time until it worked. Fortunately, I stumbled over Python’s Regex module documentation where I found a simple tokenizer based on regular expressions. So I wrote a new script that uses this technique to parse algebraic expressions. This resulted in a much smaller script:
that resulted in  tokenizer based on regular expressions implementation as 
tokenizerregex.py
