from django.shortcuts import render, redirect
from .models import Files
from summarizer.settings import BASE_DIR
import os
from modules.summary import Summary
from docx import Document
from django.http import HttpResponse

def delete_all():
	for files in os.listdir(BASE_DIR + '/media/files/'):
		os.remove(BASE_DIR + '/media/files/' + files)
	os.remove(BASE_DIR + '/generated_summary/generated_summary.docx')


def create_summary(regenerate=False):
	if regenerate:
		os.remove(BASE_DIR + '/generated_summary/generated_summary.docx')

	read_path = BASE_DIR + '/media/files/'
	write_file = BASE_DIR + '/generated_summary/generated_summary.docx'

	summ = Summary(regenerate)
	generated_summary = summ.summarize(read_path)

	doc = Document()
	doc.add_paragraph(generated_summary)
	doc.save(write_file)

	return generated_summary


def summary(request):
	if request.method == 'GET':
		if os.listdir(BASE_DIR + '/media/files/'):
			delete_all()
		return render(request, 'index.html', {})

	elif request.method == 'POST':
		for i in request.FILES.getlist('files'):
			f = Files()
			f.file = i
			f.save()

		generated_summary = create_summary()
		return render(request, 'summary.html', {'summary': generated_summary})


def delete_files(request):
	delete_all()
	return redirect(summary)


def regenerate(request):
	generated_summary = create_summary(regenerate=True)
	return render(request, 'summary.html', {'summary': generated_summary})

def download(request):
	fp = BASE_DIR + '/generated_summary/generated_summary.docx'
	data = open(fp, "rb").read()

	response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
	response['Content-Disposition'] = 'attachment; filename=download.docx'
	response["Content-Encoding"] = "UTF-8"

	return response
