from TrainingSet import TrainingSet
files = ['ambiente','animali','fascismo','omosessuali','sport','terrorismo']

'''
TYPELISTER NON FA ALTRO CHE ISTANZIARE L'OGGETTO TRAININGSET

SUCCESSIVAMENTE IMPLEMENTA UN METODO CHE RITORNA UN DIZIONARIO {<tipologia> : <parole caratteristiche>, ...}
'''

class TypeLister:
	def __init__(self):
		mytexts = TrainingSet(files)

		self.types = {}
		for filename in files:
			self.types[filename] = mytexts.get_type_list(filename)

	def getTypes(self):
		return self.types