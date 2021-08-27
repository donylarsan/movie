from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import Movieform
from .models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    # return HttpResponse("this is movie no %s" % movie_id)
    return render(request, "details.html", {'movie': movie})


def addmov(request):
    if request.method == "POST":
        nam = request.POST.get('name', )
        des = request.POST.get('desc', )
        yer = request.POST.get('year', )
        imag = request.FILES['img']
        movie = Movie(name=nam, desc=des, year=yer, img=imag)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
