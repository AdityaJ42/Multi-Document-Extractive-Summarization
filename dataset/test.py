import os
from nltk.tokenize import sent_tokenize, word_tokenize

path = './task_5_sum/'
counts = {}
print(len(os.listdir(path)))
for directory in sorted(os.listdir(path)):
	file_path = path + directory + '/'
	for file in os.listdir(file_path):
		with open(file_path + file, 'r') as fd:
			content = fd.read()
			if len(sent_tokenize(content.strip())) in counts:
				counts[len(sent_tokenize(content.strip()))] += 1
			else:
				counts[len(sent_tokenize(content.strip()))] = 1
for i in sorted(counts):
	print('Summ Len: {}\nCount: {}\n'.format(i, counts[i]))
