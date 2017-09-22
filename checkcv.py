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
		line = re.sub('(Topic\w*)|[0-9.,()*:-]', '', line)
		words = WhitespaceTokenizer().tokenize(line)
		#print(words[:10])
		print(line, palmetto.get_coherence(words[:10]))
