import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import pke
from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

stopwords = stopwords.words('english')


def get_embeddings():
	embedding = {}
	f = open('./textrank/glove.6B.100d.txt', encoding='utf-8')
	for line in f:
		values = line.split()
		word = values[0]
		coefs = np.asarray(values[1:], dtype='float32')
		embedding[word] = coefs
	f.close()
	return embedding


class TextRank:
	def __init__(self):
		self.embeddings = get_embeddings()
		self.sentence_vectors = None
		self.keyword_vectors = None
		self.sentence_keyword_similarity = None


	def get_sentences(self, text):
		sentences = []
		for s in text:
			sentences.append(sent_tokenize(s))
		sentences = [y for x in sentences for y in x]
		return sentences


	def preprocess(self, text):
		clean_sentences = pd.Series(text).str.replace('[^a-zA-Z]', ' ')
		clean_sentences = [s.lower() for s in clean_sentences]
		for i, j in enumerate(clean_sentences):
			clean_sentences[i] = ' '.join([k for k in j.split() if k not in stopwords])
		return clean_sentences


	def sent_to_vectors(self, sentences):
		self.sentence_vectors = []
		for i in sentences:
			if len(i) != 0:
				v = sum([self.embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
			else:
				v = np.zeros((100,))
			self.sentence_vectors.append(v)


	def keyword_to_vectors(self, keywords):
		self.keyword_vectors = []
		for keyword in keywords:
			if len(keyword.split()) > 1:
				v = sum([self.embeddings.get(w, np.zeros((100,))) for w in keyword.split()])/(len(keyword.split())+0.001)
			else:
				v = self.embeddings.get(keyword, np.zeros(100,))
			self.keyword_vectors.append(v)


	def sent_keyword_similarity(self, sent_vec, keyword_vec):
		self.sentence_keyword_similarity = np.zeros([len(sent_vec), 1])
		for i in range(len(sent_vec)):
			temp = 0
			for j in range(len(keyword_vec)):
				temp += cosine_similarity(sent_vec[i].reshape(1, 100), keyword_vec[j].reshape(1, 100))[0][0]
			self.sentence_keyword_similarity[i] = temp / len(keyword_vec)


	def similarity_matrix(self, n, vectors, keyword_embeddings):
		sim_mat = np.zeros([n, n])

		for i in range(n):
			for j in range(n):
				if i != j:
					sim_mat[i][j] = cosine_similarity(vectors[i].reshape(1, 100), vectors[j].reshape(1, 100))[0][0]
					sim_mat[i][j] += (self.sentence_keyword_similarity[i] + self.sentence_keyword_similarity[j]) / 2
		return sim_mat


	def get_summary(self, matrix, sentences):
		nx_graph = nx.from_numpy_array(matrix)
		scores = nx.pagerank(nx_graph)
		sentence_ranks = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
		extracted_sentences = []
		for i in range(10):
			extracted_sentences.append(sentence_ranks[i][1])
		return '\n'.join(extracted_sentences)
