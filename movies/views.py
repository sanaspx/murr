from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies= Movie.objects.all()
        return render(request,"movies/movies.html", {"movies": movies})
class MovieDetailView(View):
    """Полное описание фильма"""
    def get(self,request,pk):
        movies= Movie.objects.get(id=pk)
        return render(request, "movies/movie_detail.html", {"movies": movies})


