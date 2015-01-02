EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats': 'mange', 'drinks': 'bois',\
        'likes': 'aime', 1: 'un',\
        '6.00':'6.00'}

def translateWord(word,dictionary):
	if word in dictionary:
		return dictionary[word]
	else:
		return word

def translate(sentences):
	translation = ""
	word = ""
	for c in sentences:
		if c != ' ':
			word = word + c
		else:
			translation = translation + ' ' +translateWord(word, EtoF)
			word = ""
	return translation[1:] + " " +translateWord(word, EtoF)

print translate('John eats bread')