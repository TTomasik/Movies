from django.contrib import admin
from rest_movies.models import Person, Movie, Role


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'year', 'Actors')

    def Actors(self, movie):
        return ", ".join([str(t) for t in movie.actors.all()])


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'person', 'movie')

    # def Toppings(self, pizza):
    #     return ", ".join([t.name for t in pizza.toppings.all()])