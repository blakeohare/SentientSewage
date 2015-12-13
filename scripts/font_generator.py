import pygame
import os

LOCATIONS = [
	'ABCDEFGHIJKLM',
	'NOPQRSTUVWXYZ',
	'abcdefghijklm',
	'nopqrstuvwxyz',
	'0123456789.?~',
	'{}<>()[],;:\'"',
	'\\|/-_+`!@#$%^',
	'&*='
]

widths = {
	'A': 8,
	'B': 8,
	'C': 8,
	'D': 8,
	'E':7,
	'F':7,
	'G':8,
	'H':8,
	'I': 5,
	'J':6,
	'K': 8,
	'L': 7,
	'M': 9,
	'N': 8,
	'O': 8,
	'P': 7,
	'Q': 8,
	'R': 8,
	'S': 8,
	'T': 9,
	'U': 8,
	'V': 9,
	'W': 9,
	'X': 8,
	'Y': 9,
	'Z': 8,
	'a': 7,
	'b': 7,
	'c': 7,
	'd': 7,
	'e': 7,
	'f': 7,
	'g': 7,
	'h': 7,
	'i': 4,
	'j': 6,
	'k': 7,
	'l': 4,
	'm': 9,
	'n': 7,
	'o': 7,
	'p': 7,
	'q': 7,
	'r': 7,
	's': 7,
	't': 6,
	'u': 7,
	'v': 7,
	'w': 9,
	'x': 7,
	'y': 7,
	'z': 7,
	'0': 7,
	'1': 7,
	'2': 7,
	'3': 7,
	'4': 8,
	'5': 7,
	'6': 7,
	'7': 7,
	'8': 7,
	'9': 7,
	'.': 3,
	'?': 7,
	'~': 9,
	'{': 7,
	'}': 7,
	'<': 8,
	'>': 8,
	'(': 5,
	')': 5,
	'[': 5,
	']': 5,
	',': 4,
	';': 4,
	':': 3,
	'\'': 3,
	'"': 5,
	'\\': 7,
	'|': 3,
	'/': 7,
	'-': 7,
	'_': 9,
	'+': 7,
	'`': 4,
	'!': 3,
	'@': 9,
	'#': 9,
	'$': 7,
	'%': 9,
	'^': 7,
	'&': 8,
	'*': 7,
	'=': 8,
}

characters = {
	'per': '.',
	'com': ',',
	'lt': '<',
	'gt': '>',
	'sla': '/',
	'que': '?',
	'quo': '"',
	'apo': "'",
	'col': ':',
	'sem': ';',
	'sqr1': '[',
	'sqr2': ']',
	'cur1': '{',
	'cur2': '}',
	'par1': '(',
	'par2': ')',
	'bsl': '\\',
	'pip': '|',
	'hyp': '-',
	'equ': '=',
	'plu': '+',
	'und': '_',
	'ban': '!',
	'til': '~',
	'at': '@',
	'hsh': '#',
	'dol': '$',
	'prc': '%',
	'car': '^',
	'amp': '&',
	'ast': '*',
	'bck': '`',
}

for letter in 'abcdefghijklmnopqrstuvwxyz':
	characters['u_' + letter] = letter.upper()
	characters['l_' + letter] = letter
for i in range(10):
	characters['n_' + str(i)] = str(i)


pygame.init()
pygame.display.set_mode((200, 200))

def find_location(c):
	y = 0
	for row in LOCATIONS:
		x = 0
		for col in row:
			if col == c:
				return (x, y)
			x += 1
		y += 1
	# crash if not found

template = pygame.image.load('font_template.png').convert()

output = []

for filename in characters.keys():
	c = characters[filename]
	col, row = find_location(c)
	x = col * 14 + 3
	y = row * 14 + 2
	surf = pygame.Surface((widths[c], 13))
	surf.blit(template, (-x, -y))
	pygame.image.save(surf, os.path.join('..', 'source', 'images', 'font', filename + '.png'))
	output.append(c + filename)

c = open(os.path.join('..', 'source', 'images', 'font', 'lookup.txt'), 'wt')
c.write('\n'.join(output))
c.close()

