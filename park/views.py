from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal
from django.db.models import Q


def index(request):
    return render(request, 'park/home.html',
           {'all_animal':Animal.objects.all().count(),
            'mammal_num':Animal.objects.filter(class_name="Mammal").count(),
            'reptile_num':Animal.objects.filter(class_name="Reptile").count(),
            'bird_num':Animal.objects.filter(class_name="Bird").count(),
            'fish_num':Animal.objects.filter(class_name="Fish").count(),
            'amphibian_num':Animal.objects.filter(class_name="Amphibian").count()})

def animal_list(request, class_name):
    all_class = ["All","Mammal","Reptile","Bird","Fish","Amphibian"]
    if(class_name == 'All'):
        animal_list = Animal.objects.order_by('thai_name')
    elif(class_name in ('Mammal','Reptile','Bird','Fish','Amphibian')):
        animal_list = Animal.objects.filter(class_name=class_name).order_by('thai_name')
    else:
        raise Http404("Question does not exist")
    return render(request, 'park/animal_list.html',{'lists':animal_list,'all_class':all_class,'class_now':class_name})

def animal_data(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'park/animal_data.html',{'animal':animal})

def search(request):
    animal_list = []
    word = ""
    if(request.GET.get('word')):
        word = request.GET.get('word')
        animal_list = Animal.objects.filter(
            Q(thai_name__icontains=word) |
            Q(name__icontains=word,) |
            Q(class_name__icontains=word,) |
            Q(order__icontains=word,) |
            Q(family__icontains=word,) |
            Q(info__icontains=word,) |
            Q(habitat__icontains=word)
        )
        for animal in animal_list:
            print(animal.name)
    return render(request, 'park/search.html',{'word':word, 'lists':animal_list})