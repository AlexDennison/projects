from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import Movie
from . forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movielist' : movie
    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movie = Movie.objects.get(id = movie_id)                   #To get details of a particular id
    return render(request,'detail.html',{'movies' :movie})

def add_movie(request):
    if request.method == 'POST':                               #Fetching data from HTML FORM
        name = request.POST.get('name',)
        image = request.FILES['image']
        overview = request.POST.get('overview',)
        year = request.POST.get('year',)
        genre = request.POST.get('genre',)
        rating = request.POST.get('rating',)
        movie = Movie(name =name,image=image,overview = overview,year=year,genre= genre,rating=rating)      #Adding fetched data to database
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie = Movie.objects.get(id = id)
    form = MovieForm(request.POST or None, request.FILES,instance = movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method =='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
    

