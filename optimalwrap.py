from copy import deepcopy

input_text = input("Input text to be wrapped")

results = {}

def extractWords(words):
	words = words.split(" ")
	return [[{word:len(word)}] for word in words]

def score(words):
	if words is None:
		return None
	line_lengths = []
	for line in words:
		line_length = 0
		for word in line:
			for key, value in word.items():
				if len(line)>1:
					line_length+=1
				line_length+=value
		if len(line)>1:
			line_length-=1
		line_lengths.append(line_length)
	width = max(line_lengths)
	area = width*len(line_lengths)
	score_value = area - sum(line_lengths)
	return score_value

def returnline(text, n):
	if set(text[n]) == set(text[n-1]):
		return text
	old_line = text.pop(n)
	text[n-1] = text[n-1] + old_line
	return text

def returnfirstword(text,n):
	word = text[n].pop(0)
	text[n-1].append(word)
	if not text[n]:
		text.pop(n)
	return text

def wrap(text):
	for line in text:
		line_string = str()
		for word in line:
			for key, value in word.items():
				word_string = key + " "
				line_string+=word_string
		print(line_string)

def score_result(text):
	new_text = deepcopy(text)
	results[score(text)] = new_text

def optimize(text):
	if len(text) == 1:
		return
	if score(text) == 0:
		return
	for n in range(1,len(text)):
		text = returnfirstword(text,len(text)-1)
		if len(text) > 1:
			if score(text) not in results:
				score_result(text)
	optimize(text)

optimize(extractWords(input_text))

wrap(results[min(results)])