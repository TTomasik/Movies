from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey('Person', related_name='movie_director')
    actors = models.ManyToManyField('Person', through='Role', blank=True, related_name='movie_actors')
    year = models.SmallIntegerField()

    def __str__(self):
        return self.title

class Role(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="Movie_person")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="Movie_movie")
    role = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.role