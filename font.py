import pygame
import string

def size(text):
	biggest_len = 0
	for line in string.split(text, "\n"):
		if len(line) > biggest_len:
			biggest_len = len(line)
	return (12*biggest_len,(string.count(text, "\n") + 1)*16)

def render(font,text,color):
	thumbx = 0
	thumby = 0
	textsurf = pygame.Surface(size(text), pygame.SRCALPHA)
	for char in text:
		if char == "\n":
			thumbx = 0
			thumby += 16
			continue
		charpos = fontdict.get(str(char), (15,5))
		#print "%s:%s" % (str(char),charpos)
		position = (charpos[0]*12,charpos[1]*16, 12, 16)
		textsurf.blit(font,(thumbx, thumby),area=position)
		thumbx += 12
	textsurf.fill(color,special_flags=pygame.BLEND_RGBA_MULT)
	return textsurf

fontdict = {
			' ':(0,0),
			'!':(1,0),
			'"':(2,0),
			'#':(3,0),
			'$':(4,0),
			'%':(5,0),
			'&':(6,0),
			"'":(7,0),
			'(':(8,0),
			')':(9,0),
			'*':(10,0),
			'+':(11,0),
			',':(12,0),
			'-':(13,0),
			'.':(14,0),
			'/':(15,0),
			'0':(0,1),
			'1':(1,1),
			'2':(2,1),
			'3':(3,1),
			'4':(4,1),
			'5':(5,1),
			'6':(6,1),
			'7':(7,1),
			'8':(8,1),
			'9':(9,1),
			':':(10,1),
			';':(11,1),
			'<':(12,1),
			'=':(13,1),
			'>':(14,1),
			'?':(15,1),
			'@':(0,2),
			'A':(1,2),
			'B':(2,2),
			'C':(3,2),
			'D':(4,2),
			'E':(5,2),
			'F':(6,2),
			'G':(7,2),
			'H':(8,2),
			'I':(9,2),
			'J':(10,2),
			'K':(11,2),
			'L':(12,2),
			'M':(13,2),
			'N':(14,2),
			'O':(15,2),
			'P':(0,3),
			'Q':(1,3),
			'R':(2,3),
			'S':(3,3),
			'T':(4,3),
			'U':(5,3),
			'V':(6,3),
			'W':(7,3),
			'X':(8,3),
			'Y':(9,3),
			'Z':(10,3),
			'[':(11,3),
			'\\':(12,3),
			']':(13,3),
			'^':(14,3),
			'_':(15,3),
			'`':(0,4),
			'a':(1,4),
			'b':(2,4),
			'c':(3,4),
			'd':(4,4),
			'e':(5,4),
			'f':(6,4),
			'g':(7,4),
			'h':(8,4),
			'i':(9,4),
			'j':(10,4),
			'k':(11,4),
			'l':(12,4),
			'm':(13,4),
			'n':(14,4),
			'o':(15,4),
			'p':(0,5),
			'q':(1,5),
			'r':(2,5),
			's':(3,5),
			't':(4,5),
			'u':(5,5),
			'v':(6,5),
			'w':(7,5),
			'x':(8,5),
			'y':(9,5),
			'z':(10,5),
			'{':(11,5),
			'|':(12,5),
			'}':(13,5),
			'~':(14,5)}