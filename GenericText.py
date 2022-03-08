from TypeLister import TypeLister
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
import time

'''
GenericText prende come argomento il testo da anallizzare.
lo pulisce automaticamente con tutte le procedure necessarie.
poi il metodo guess_the_type ritorna il tipo indovinato.
'''

################################################################
#															   #
# E' CONSIGLIATO INGRANDIRE IL TERMINALE PRIMA DELL'ESECUZIONE #
#															   #
################################################################

class GenericText:
	def __init__(self,filename):
		try:
			with open(filename,'r') as f:
				self.text = f.readlines()
		except:
			print(f'{filename} non esiste')
			exit()

		self.cleantext()

	def cleantext(self):

		# stemmer = PorterStemmer()
		stemmer = SnowballStemmer('italian',ignore_stopwords = True)
		stop_words = set(stopwords.words('italian'))

		flag = 0
		for line in self.text:

			#CLEAN FROM CHARACTERS
			for chara in ",.‘’”“0123456789:;#()[]}{_-!?/&%$£\\/\"|":
				line = line.replace(chara,"")
			#volevo che gli apici diventassero spazi, cosi non si creano parole strane
			line = line.replace("'"," ")
			self.text[flag] = line

			# MAKE IT LOWER
			self.text[flag] = line.lower()

			# TOKENIZE 
			self.text[flag] = word_tokenize(self.text[flag])

			# STOP WORDS
			filtered_words = []
			for word in self.text[flag]:
				if word not in stop_words:
					filtered_words.append(word)
			self.text[flag] = filtered_words

			# STEEMMMMEEEEEER
			# a mio parere questa libreria ha un dubbio funzionamento
			stemmed_words = []
			for word in self.text[flag]:
				stemmed_words.append(stemmer.stem(word))
			self.text[flag] = stemmed_words

			#next line
			flag+=1

		# in the end, put it into a single list
		joined_list = []
		for line in self.text:
			joined_list += line
		self.text = joined_list

		## incerto se sia giusto considerare una sola volta le parole in questo caso
		## comunque, lo faccio
		
		unic_list = []
		for word in self.text:
			if word not in unic_list:
				unic_list.append(word)
		self.text = unic_list
		
	def guess_the_type(self):
		types = TypeLister().getTypes()
		delta = { x:0  for x in types}
		for key in types:
			delta[key] = 0
			#relative delta den
			den = len(types[key])
			for word_type in types[key]:
				for word_text in self.text:
					if word_text == word_type:
						
						delta[key] += 1/den

		maximum = 0
		# trova il delta maggiore !!
		for key in delta:
			if delta[key] > maximum:
				maximum = delta[key]
				guessed_type = key

		return guessed_type

	
	def debug_text(self):
		return self.text

### NON ESPLICITAMENTE RICHIESTO DALLA CONSEGNA
LABEL = "\n\
..######...##.....##.########..######...######.....########.##.....##.########....########.##....##.########..########\n\
.##....##..##.....##.##.......##....##.##....##.......##....##.....##.##.............##.....##..##..##.....##.##......\n\
.##........##.....##.##.......##.......##.............##....##.....##.##.............##......####...##.....##.##......\n\
.##...####.##.....##.######....######...######........##....#########.######.........##.......##....########..######..\n\
.##....##..##.....##.##.............##.......##.......##....##.....##.##.............##.......##....##........##......\n\
.##....##..##.....##.##.......##....##.##....##.......##....##.....##.##.............##.......##....##........##......\n\
..######....#######..########..######...######........##....##.....##.########.......##.......##....##........########\n\
"

if __name__ == '__main__':

	## HEADER PRINTER
	for line in LABEL:
		print(line,end = "")
		if line == '\n':
			time.sleep(0.5)
	print()

	filename = input('File da analizzare --> ')
	gt = GenericText(filename)
	print(f"Il genere del testo è {gt.guess_the_type()}")



