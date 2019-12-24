def lc_remove(text): 
	return ' '.join(word for word in text.split() if len(word)>3)