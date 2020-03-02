import re
from nltk.corpus import stopwords
import spacy
import neuralcoref
from nltk.tokenize import sent_tokenize


class Preprocessor:
	def __init__(self, path):
		pass


	def get_text(self, file):
		with open(file, 'r') as fd:
			contents = fd.read()
		return contents

	def get_text_from_docx(self, file):
		doc = docx.Document(file)
		text = []
		for para in doc.paragraphs:
			text.append(para.text)
		return '\n'.join(text)


	def get_sentences(self, text):
		sentences = []
		for s in text:
			sentences.append(sent_tokenize(s))
		sentences = [y for x in sentences for y in x]
		return sentences


	def remove_stopwords(self, sentences):
		for i, sent in enumerate(sentences):
			sentences[i] = ' '.join([i for i in sent.split() if i not in stopwords])
		return sentences


	def resolve_pronoun(self, text):
		nlp = spacy.load('en')
		neuralcoref.add_to_pipe(nlp, greedyness=0.55)
		doc = nlp(text)

		if doc._.has_coref:
			resolved_text = doc._.coref_resolved

		return resolved_text
