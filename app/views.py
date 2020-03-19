from django.shortcuts import render


def home(request):
	return render(request, 'index.html', {})


def summary(request):
	if request.method == 'GET':
		return render(request, 'upload.html', {})
	elif request.method == 'POST':
		return render(request, 'summary.html', {})
