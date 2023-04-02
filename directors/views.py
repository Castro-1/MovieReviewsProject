from django.shortcuts import render
from .models import Directors
# Create your views here.
def directors(request):
    directors = Directors.objects.all()
    return render(request, 'directors.html', {"directors": directors})