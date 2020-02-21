import collections
import sys
import re

def tokenize(stream):
	Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

	tokenSpec = [
		# Arithmetic operators 		('OPERATOR',	r'(?<!--[\+\-\^\*/%])[\+\-]|[\^\*/%!]'),<br /-->
		# Function identifiers 		('FUNCTIONID',	r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()'),
		# Variable identifiers 		('VARIABLEID',	r'[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()'),
		# Any numeric value (decimal or floating point) 		('NUMBER',		r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'),
		# Left brace 		('LBRACE',		r'[(]'),
		# Right brace 		('RBRACE',		r'[)]'),
		# Assignment operator 		('ASSIGN',		r':='),
		# Line endings 		('NEWLINE',		r'\n'),
		# Skip over spaces and tabs 		('SKIP',			r'[ \t]'),
	]

	tokenRegex = '|'.join('(?P<%s>%s)' % pair for pair in tokenSpec)
	keywords = {
		'+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIV',
		'^': 'EXP', '%': 'MOD', '!': 'FAC'
	}

	nextToken = re.compile(tokenRegex).match

	# Setup the line start and current position ... 	pos = lineStart = 0

	# ... as well as the current line. 	line = 1

	# Fetch the first token ... 	token = nextToken(stream)

	# ... and start the processing. 	while token is not None:
		# Fetch the token type ... 		typ = token.lastgroup

		# ... and increment line counter if it is a newline. 		if typ == 'NEWLINE':
			lineStart = pos
			line += 1
		elif typ != 'SKIP':
			# Fetch the token value ... 			value = token.group(typ)

			# ... and handle keywords. 			if typ == 'OPERATOR' and value in keywords.keys():
				typ = keywords[value]

			yield Token(typ, value, line, token.start() - lineStart)

		pos = token.end()
		token = nextToken(stream, pos)
	if pos != len(stream):
		raise TokenizerException('Unexpected character %r on line %d' % (stream[pos], line))

def main(argv):
	form = argv[0]

	# Do something with this data. 	if form is not None:
		for token in tokenize(form):
			print token
	else:
		print 'Invalid parameters.\n'
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])
