#views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Mineral

def index(request):
	''' Returns a list of all the minerals in the database. '''
	minerals = Mineral.objects.all()
	return render(request, 'minerals/index.html', {'minerals': minerals})
	
def detail(request, pk):
	''' Returns a detailed view of a single mineral. '''
	mineral = get_object_or_404(Mineral, pk=pk)
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})