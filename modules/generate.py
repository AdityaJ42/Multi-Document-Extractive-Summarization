import os
from preprocess import Preprocessor
from textrank.textrank import TextRank


pp = Preprocessor()
tr = TextRank()

base_path = "/home/aditya/Desktop/BE Project/data/prepared/"
read_path = base_path + "Task 1 and 2/"
for folder in os.listdir(read_path):

	write_path = base_path + "summaries/" + folder + "/"
	os.mkdir(write_path)
	file_path = read_path + folder + '/'
	contents = ''

	for file in os.listdir(file_path):
		contents += pp.read_text(file_path + file)

	contents = pp.clean(contents)
	resolved_content = pp.resolve_pronoun(contents)
	keyphrases = tr.get_keyphrases(contents)
	sentences = pp.get_sentences(resolved_content)
	og_sentences = sentences
	sentences = pp.remove_stopwords(sentences)

	vecs = tr.sent_to_vectors(sentences)
	matrix = tr.similarity_matrix(sentences, vecs, keyphrases)
	summary = tr.summarize(matrix, og_sentences)
	
	write_data = [og_sentences[0]]
	for k, i in enumerate(summary.split('\n')):
		if i != og_sentences[0]:
			write_data.append(i)

	with open(write_path + 'summary.txt', 'w') as fd:
		fd.write('\n'.join(write_data))

#print("Original Length: {}".format(len(og_sentences)))
#print("Summary Length: {}".format(len(summary.split('\n'))))
