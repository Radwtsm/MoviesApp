from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from flix.serializers import MovieSerializer

from .models import Movie


@api_view(['GET'])
def getMovies(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
