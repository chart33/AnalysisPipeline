import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import collections
import sys
import os

directory = sys.argv[1]


def GetTokens(filename):
	print("tokenizing filename %s" % filename)
	text=textract.process(filename, method='tesseract', language='eng')
	sentences=word_tokenize(text.decode('utf-8'))
	filter_tokens = ['(',')',';',':','[',']',',','.','-','!','=','we','patient','care', 'patients']
	stop_words = stopwords.words('english')

	keywords = [word for word in sentences if not word in stop_words and not word in filter_tokens]
	token_frequency = collections.Counter(keywords)

	return token_frequency.most_common(10)

def IsPDF(filename):
	if (filename.find('.pdf',len(filename)-4, len(filename)) > 0):
		return True

	return False

def RunPipeline(directory):
	frequency_data = {}
	# iterate over files
	for filename in os.listdir(directory):
	# get tokens for each file and pack into frequency data
		if IsPDF(filename):
			full_name = directory+'/'+filename
			frequency_data[filename] = GetTokens(full_name)
		else:
			print ("%s is not a pdf." % filename)

	return frequency_data

print RunPipeline(directory)

