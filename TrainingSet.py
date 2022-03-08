from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

'''
1.  TRAININGSET PRENDE UNA LISTA DI FILENAMES COME ARGOMENTO.
2.  PULISCE I TESTI (ITALIANI) PULENDO CARATTERI INUTILI, FACENDOLI MINUSCOLI, TOGLIENDO
	STOP WORDS E FACENDO STEMMING.

'''

class TrainingSet:

	def __init__(self,filename_list):
		self.texts = {}
		for filename in filename_list:
			with open(filename,'r') as f:
				self.texts[filename] = f.readlines()
		self.ready_to_work()

	# void, prepara i testi alla elaborazione
	def ready_to_work(self):

		#from libraries
		stemmer = SnowballStemmer('italian',ignore_stopwords = True)
		stop_words = set(stopwords.words('italian'))


		for filename in self.texts:
			flag = 0
			for line in self.texts[filename]:
				# x ogni riga(flag):

				#CLEAN FROM CHARACTERS
				for chara in ",.0123456789:;#()[]}{_-!?/&%$£\\/\"|":
					line = line.replace(chara,"")
				#volevo che gli apici diventassero spazi, cosi non si creano parole strane
				line = line.replace("'"," ")
				self.texts[filename][flag] = line

				# MAKE IT LOWER
				self.texts[filename][flag] = line.lower()

				# TOKENIZE 
				self.texts[filename][flag] = word_tokenize(self.texts[filename][flag])

				# STOP WORDS
				filtered_words = []
				for word in self.texts[filename][flag]:
					if word not in stop_words:
						filtered_words.append(word)
				self.texts[filename][flag] = filtered_words

				# STEEMMMMEEEEEER
				# a mio parere questa libreria funziona malissimo
				stemmed_words = []
				for word in self.texts[filename][flag]:
					stemmed_words.append(stemmer.stem(word))
				self.texts[filename][flag] = stemmed_words

				#next line
				flag+=1

	# restituisce lista che contiene ciascuna parola del file già elaborato e senza doppioni
	def get_type_list(self,types):
		for typename in self.texts:
			if types == typename:
				joined_list = []

				# joined_list = lista che contiene ciascuna parola
				for line in self.texts[typename]:
					joined_list += line

				# togliamo i doppioni
				unic_list = []
				for word in joined_list:
					if word not in unic_list:
						unic_list.append(word)

				return unic_list

	def getTexts(self):
		return self.texts


# DEBUG
if __name__ == '__main__':
	gt = TrainingSet(['ambiente.txt'])
	gt.tutto()
	print(gt.getTexts())
	texts = gt.getTexts()
	print(gt.get_type_list('ambiente.txt'))