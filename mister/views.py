from django.shortcuts import render
from django.http import HttpResponse
from mister.models import Collector

def index(request):
	data = Collector.objects.all()
	return render(request, 'index.html', {'data': data,})

# def collector_detail(request, slug):
# 	data = Collector.objects.get(slug=slug)
# 	return render(request, 'data/collector_detail.html', {'data': data,})