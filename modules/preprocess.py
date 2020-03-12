import re
from nltk.corpus import stopwords
import spacy
import neuralcoref
from nltk.tokenize import sent_tokenize
stopwords = stopwords.words('english')


class Preprocessor:
	def __init__(self):
		pass


	def read_text(self, file):
		with open(file, 'r') as fd:
			contents = fd.read()
		return contents

	def read_docx(self, file):
		doc = docx.Document(file)
		text = []
		for para in doc.paragraphs:
			text.append(para.text)
		return '\n'.join(text)


	def clean(self, text):
		return text.strip().replace('\n', ' ')


	def resolve_pronoun(self, text):
		nlp = spacy.load('en')
		neuralcoref.add_to_pipe(nlp, greedyness=0.55)
		doc = nlp(text)

		if doc._.has_coref:
			resolved_text = doc._.coref_resolved

		return resolved_text


	def get_sentences(self, text):
		sentences = sent_tokenize(text)
		return sentences


	def remove_stopwords(self, sentences):
		for i, sent in enumerate(sentences):
			sentences[i] = re.sub(r'^[a-zA-Z0-9]+', ' ', sent.lower())
			sentences[i] = ' '.join([j for j in sent.split() if j not in stopwords])
		return sentences
