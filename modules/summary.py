import os
from preprocess import Preprocessor
from keyphrase import Keyphrase
from textrank.textrank import TextRank
from shortest import Graph


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
			contents += pp.read_text(file_path + file)

		# Combining paragraphs generate one large doc content
		complete_content = pp.clean(contents)

		# Pronoun resolution for effective keyphrase extraction
		resolved_content = pp.resolve_pronoun(complete_content)
		
		# Tokenize the consolidated data into sentences
		sentences = pp.get_sentences(resolved_content)

		# Maintain the original sentences of the documents for extraction
		original_sentences = pp.get_sentences(complete_content)
		if len(original_sentences) < len(sentences):
			sentences = sentences[:len(original_sentences)]
		
		# Extraction of keyphrases
		self.keywords = kp.get_keyphrases(resolved_content)

		# Create a vector for the sentences
		tr.sent_to_vectors(sentences)
		
		# Create a vector for the keywords
		tr.keyword_to_vectors(self.keywords)

		# Get averaged sentence to keyword similarity
		tr.sent_keyword_similarity(tr.sentence_vectors, tr.keyword_vectors)

		# Create a similarity matrix i.e. graph for textrank
		matrix = tr.similarity_matrix(len(sentences), tr.sentence_vectors, tr.keyword_vectors)

		# Using Shortest Path to reduce by extracting sentences with proper flow
		g = Graph(len(matrix))
		g.graph = matrix
		sentence_index = g.dijkstra(0, len(matrix) - 1)
		extracted_sentences = [sentences[i] for i in sentence_index]

		# Recompute similarity matrix for reduced sentences
		tr.sent_to_vectors(extracted_sentences)
		matrix = tr.similarity_matrix(len(extracted_sentences), tr.sentence_vectors, tr.keyword_vectors)

		# Create summary based on sentence scores after TextRank iterations
		sentences_used = [original_sentences[i] for i in sentence_index]
		self.summary = tr.get_summary(matrix, sentences_used)
		
		# View Summary
		return self.summary

read_path = 'PATH_TO_INPUT_DOCS'
write_path = 'PATH_TO_OUTPUT_SUMMARY'

for directory in os.listdir(read_path):
	path = read_path + directory + '/'
	print('Generating for: ' + path)
	os.mkdir(write_path + directory)
	write_file = write_path + directory + '/generated_summary.txt'

	summ = Summary()
	generated_summary = summ.summarize(path)
	with open(write_file, 'w') as fd:
		fd.write(generated_summary)
