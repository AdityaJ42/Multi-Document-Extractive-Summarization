import pke
from nltk.corpus import stopwords
stoplist = stopwords.words('english')

class Keyphrase:
	def __init__(self):
		pass


	def get_keyphrases(self, content):
		extractor = pke.unsupervised.YAKE()
		extractor.load_document(input=content, language='en', normalization=None)
		extractor.candidate_selection(n=2, stoplist=stoplist)
		extractor.candidate_weighting(window=1, stoplist=stoplist, use_stems=False)
		keyphrases = extractor.get_n_best(n=5, threshold=1)
		all_keyphrase = [k[0] for k in keyphrases]
		return all_keyphrase
