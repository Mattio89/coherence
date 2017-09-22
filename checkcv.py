import shlex
import nltk
from nltk.tokenize import WhitespaceTokenizer
from palmettopy.palmetto import Palmetto
import re
import string
import tkinter
palmetto = Palmetto()
from tkinter.filedialog import askopenfilename
filename = askopenfilename()

with open(filename,'r', encoding="utf8") as inFile:
	for line in inFile.readlines():
		#This regular expression removes any of the "noise" from a .txt file containing the generated topics. Only the words in the topic remain.
		line = re.sub('(Topic\w*)|[0-9.,()*:-]', '', line)
		#Called in the NLTK tokenizer to help navigate outputing the correct lines.
		words = WhitespaceTokenizer().tokenize(line)
		#Palmetto only takes the first 10 words in its webservice, so this limits the input and prints the coherence value
		print(line, palmetto.get_coherence(words[:10]))
		#I use the bash command 'python checkcv.py >> output.txt' to save the output.
