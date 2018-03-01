Question=raw_input ("Enter in any number of words, spearated by a comma. ")

lower=Question.lower()
words=lower.split(',')
numOfWords=len(words)

if(numOfWords%2 == 1):

	if("llama" or "Llama" in words):
		print(' '.join(words))

elif((numOfWords%2 == 1) or ((words[0]%2 == 1) and (words[1]%2 == 1) and (words[2]%2 == 1) and (words[3]%2 == 1) and (words[4]%2 == 1))):
	print("That is add...O_O")
