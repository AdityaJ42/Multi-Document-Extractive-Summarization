import os

read_path = '5'
write_path = 'task_5_sum'


for i in sorted(os.listdir(read_path)):
	parts = i.split('.')
	dir_name, author = parts[0], parts[4]

	if dir_name.lower() + 't' not in os.listdir(write_path):
		os.mkdir(write_path + '/' + dir_name.lower() + 't')
	
	if author == 'A':
		with open(read_path + '/' + i, 'r') as fd:
			content = fd.read().strip()
		with open(write_path + '/' + dir_name.lower() + 't/summary.txt', 'a') as fd:
			fd.write(content + ' ')
