from django.shortcuts import render
from django.http import HttpResponse
from mister.models import Collector

def index(request):
	return render(request, 'index.html')

def collection(request):
	data=Collector.objects.all().order_by('-time_collected')
	return render(request, 'plantinfo.html', {'data': data,})

# def instance_detail(request, id):
# 	instance=Collector.objects.get(id=id)
# 	return render(request, 'instance_detail.html', {'instance': instance,})	
# 	pass