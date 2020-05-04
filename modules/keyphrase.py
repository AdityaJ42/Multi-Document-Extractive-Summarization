import pke
from nltk.corpus import stopwords
stoplist = stopwords.words('english')

class Keyphrase:
	def __init__(self, regenerate):
		self.top_percent = 0.6 if not regenerate else 0.33


	def get_keyphrases(self, content):
		pos = {'NOUN', 'PROPN', 'ADJ'}
		extractor = pke.unsupervised.TextRank()
		extractor.load_document(input=content, language='en', normalization=None)
		extractor.candidate_weighting(window=3, pos=pos, top_percent=self.top_percent)
		keyphrases = extractor.get_n_best(n=3)
		all_keyphrase = [k[0] for k in keyphrases]
		return all_keyphrase
