from django.shortcuts import render, redirect
from .models import People


# Create your views here.
def index(request):
    people = People.objects.all()
    return render(request, 'index.html', {'pessoas': people})


def create(request):
    r_name = request.POST.get('name')
    People.objects.create(name=r_name)
    people = People.objects.all()
    return render(request, 'index.html', {'pessoas': people})


def edit(request, id):
    people = People.objects.get(id=id)
    return render(request, 'update.html', {'pessoas': people})


def update(request, id):
    r_name = request.POST.get('name')
    people = People.objects.get(id=id)
    people.name = r_name
    people.save()
    return redirect(index)


def destroy(request, id):
    people = People.objects.get(id=id)
    people.delete()
    return redirect(index)
