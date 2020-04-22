from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Movie, Genre

### CRUD
#from .models import Movie

#Movie.objects.all()
#Movie.objects.filter(release_year=1994)
#Movie.objects.get(id=1)

#def index(request):
#   movies = Movie.objects.all()
#   return render(request, 'views/index.html', { 'movies': movies } )

# def index(request):
#     my_dict = {"insert_me": "I am from views.py"}
#     movies = Movie.objects.all()
#     return render(request,'views/index.html',context=movies)

def index(request):
       return render(request, 'views/index.html')

"""
    read all: Movie.objects.all()
    get by id: Movie.objects.get(id=1)
    filter: Movie.objects.filter(in_stock=0)
"""

def catalog(request):
    movies = Movie.objects.all() # read the movies tables
    #titles = ', '.join([m.title for m in movies])
    #return HttpResponse(titles)
    return render(request, 'views/catalogtest.html', { 'title': 'FROM BACKED', 'movies': movies } )

def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'views/details.html', {'movie': movie})


    # in python we have two options
    
# {% %} logic like loops and conditional statements
# {{ }} render values 

# {% for movie in movies %}
#     th> {{ movie.x }} </th>

#     {% endfor %}