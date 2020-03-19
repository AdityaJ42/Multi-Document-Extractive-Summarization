import re
import os

source_path = './docs/'
dest_path = './prepared/'


def get_text(fp):
	with open(fp, 'r') as fp:
		ip = fp.read()
	pattern = re.compile(r"<TEXT>(.*)</TEXT>",re.DOTALL)
	matches = pattern.search(ip)
	return matches.group(1)

for i in os.listdir(source_path):
	path = source_path + i + '/'
	for j in sorted(os.listdir(path)):
		temp = path + j + '/'
		temp2 = path.replace(source_path, dest_path)
		if j not in os.listdir(temp2):
			os.mkdir(temp2 + j)
		for k in os.listdir(temp):
			file_path = temp + k
			text = get_text(file_path)
			write_path = file_path.replace(source_path, dest_path)
			fd = open(write_path, 'w')
			fd.write(text)
			fd.close()