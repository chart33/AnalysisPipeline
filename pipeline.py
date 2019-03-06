# the purpose of this code is to extract text from a pdf,
# clean it of stopwords and trivial symbols, and prepare a
# frequency counter for all resulting tokens that may be
# used to further identify key terms and phrases

import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import collections
import sys
 

filename = sys.argv[1]

def GetTokens(filename):
	print("tokenizing filename %s" % filename)
	text=textract.process('test.pdf', method='tesseract', language='eng')
	sentences=word_tokenize(text.decode('utf-8'))
	punctuations = ['(',')',';',':','[',']',',','.','-','!']
	stop_words = stopwords.words('english')

	keywords = [word for word in sentences if not word in stop_words and not word in punctuations]
	token_frequency = collections.Counter(keywords)

	return token_frequency


tokens = GetTokens(filename)

print tokens
