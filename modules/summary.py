import os
from preprocess import Preprocessor
from keyphrase import Keyphrase
from textrank.textrank import TextRank


class Summary:
	def __init__(self, regenerate=False):
		self.keywords = None
		self.summary = None
		self.regenerate = regenerate

	def summarize(self, file_path):
		pp = Preprocessor()
		tr = TextRank()
		kp = Keyphrase()
		contents = ""

		# Read the single/multiple documents uploaded by user
		for file in os.listdir(file_path):
			if file.split('.')[1] == 'txt':
				contents += pp.read_text(file_path + file)
			elif file.split('.')[1] == 'docx':
				contents += pp.read_docx(file_path + file)

		# Combining paragraphs generate one large doc content
		complete_content = pp.clean(contents)

		# Pronoun resolution for effective keyphrase extraction
		resolved_content = pp.resolve_pronoun(complete_content)

		# Extraction of keyphrases
		self.keywords = kp.get_keyphrases(resolved_content)

		# Tokenize the consolidated data into sentences
		sentences = pp.get_sentences(resolved_content)

		# Tokenize the original document data into sentences
		# original_sentences = pp.get_sentences(complete_content)
		
		# Create a copy of the resolved sentences for displaying results
		original_sentences = sentences.copy()

		# Create a vector for the sentences and keywords
		sentence_vectors = tr.sent_to_vectors(sentences)
		keyword_vectors = tr.keyword_to_vectors(self.keywords)

		# Create a similarity matrix i.e. graph for textrank
		matrix = tr.similarity_matrix(len(sentences), sentence_vectors, keyword_vectors)

		# Create summary based on sentence scores after TextRank iterations
		self.summary = tr.get_summary(matrix, original_sentences)
		
		# View Summary
		return self.summary
