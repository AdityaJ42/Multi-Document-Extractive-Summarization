import os

read_path = 'ref_sum'
write_path = 'gen_sum'

def generate(d, author):
	for i in sorted(os.listdir(read_path)):
		parts = i.split('.')
		dir_n, a = parts[0], parts[4]
		if dir_n == d and a == author:
			with open(read_path + '/' + i, 'r') as fd:
				content = fd.read().strip()
			with open(write_path + '/' + dir_n.lower() + 't/summary.txt', 'a') as fd:
				fd.write(content + '.\n')


for i in sorted(os.listdir(read_path)):
	parts = i.split('.')
	dir_name, author = parts[0], parts[4]

	if dir_name.lower() + 't' not in os.listdir(write_path):
		os.mkdir(write_path + '/' + dir_name.lower() + 't')

count = 0
while True:
	temp = []
	all_auths = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	for i in sorted(os.listdir(write_path)):
		if not os.listdir(write_path + '/' + i):
			generate(i.upper().replace('T', ''), all_auths[count])
	
	for i in sorted(os.listdir(write_path)):
		if os.listdir(write_path + '/' + i):
			temp.append(1)

	if temp.count(1) == 50:
		break
	else:
		count += 1

for i in sorted(os.listdir(write_path)):
	file_path = write_path + '/' + i
	with open(file_path + '/summary.txt', 'r') as fd:
		content = [i for i in fd.read().split('\n') if i != '']
		count += 1
		print('File: {}\nSummary sentences length: {}\n'.format(file_path, len(content)))
