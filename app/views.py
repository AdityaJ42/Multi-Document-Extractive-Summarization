from django.shortcuts import render, redirect
from .models import Files
from summarizer.settings import BASE_DIR
import os
from modules.summary import Summary


def summary(request):
	if request.method == 'GET':
		return render(request, 'index.html', {})
	elif request.method == 'POST':
		for i in request.FILES.getlist('files'):
			f = Files()
			f.file = i
			f.save()

		read_path = BASE_DIR + '/media/files/'
		write_path = BASE_DIR + '/generated_summary/'

		summ = Summary()
		generated_summary = summ.summarize(read_path)

		write_file = write_path + '/generated_summary.txt'
		with open(write_file, 'w') as fd:
			fd.write(generated_summary)

		return render(request, 'summary.html', {'summary': generated_summary})


def delete_files(request):
	for files in os.listdir(BASE_DIR + '/media/files/'):
		os.remove(BASE_DIR + '/media/files/' + files)
	os.remove(BASE_DIR + '/generated_summary/generated_summary.txt')
	return redirect(summary)
