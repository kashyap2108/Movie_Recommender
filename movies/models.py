from django.db import models

# Create your models here.

class Movie(models.Model):
	movie_id = models.IntegerField()
	imdb_id = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
	release_year = models.IntegerField()
	director = models.CharField(max_length=200)
	avg_rating = models.FloatField()

	def __str__(self):
		return self.title


class Genre(models.Model):
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	genre = models.CharField(max_length=20)


	def __str__(self):
		return self.genre

class Cast(models.Model):
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	actors = models.CharField(max_length=50)

	def __str__(self):
		return self.actors
