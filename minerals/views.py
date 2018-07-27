#views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Minerals

def index(request):
	minerals = Mineral.objects.all()
	return render(request, 'minerals/index.html', {'minerals': minerals})
	
def detail(request, pk):
	mineral = get_object_or_404(Mineral, pk=pk)
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})