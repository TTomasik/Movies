from django.shortcuts import render
from rest_framework.views import APIView
from rest_movies.models import Movie, Person, Role
from django.http import HttpResponse, HttpResponseNotFound, Http404
from rest_movies.serializers import MovieSerializer, PersonSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MoviesList(APIView):

    def get(self, request, format=None):
        movie = Movie.objects.all()
        print(movie)
        serializer = MovieSerializer(movie, many=True, context={"request": request})
        return Response(serializer.data)

class PersonsList(APIView):

    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True, context={"request": request})
        return Response(serializer.data)

class PersonDetail(APIView):

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = PersonSerializer(detail, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        person_put = self.get_object(pk)
        serializer = PersonSerializer(person_put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class MovieDetail(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = MovieSerializer(detail, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        movie_put = self.get_object(pk)
        serializer = MovieSerializer(movie_put, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)




#GENERICS:
# from rest_framework import generics
#
# class PersonList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
# class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


