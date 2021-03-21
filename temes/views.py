from django.shortcuts import render
from temes.models import Category, Exercici


# Create your views here.

def temes(request):
    categories = Category.objects.all()
    return render(request, 'temes/temes.html', {"categories": categories})


def exercicis(request, id):
    exercicis = Exercici.objects.all().filter(category_id=id)
    return render(request, 'temes/exercicis.html', {"exercicis": exercicis})


def show_exercici(request, pk):
    show_exercici = Exercici.objects.get(pk=pk)
    return render(request, 'temes/exercici_gran.html',
                  {"show_exercici": show_exercici})
