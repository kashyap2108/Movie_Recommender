import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE","movie_rs.settings")

import django
django.setup()

from movies.models import Movie

def save_movie_from_row(movie_row):
	#print(movie_row[0],type(movie_row[1]))
	movie = Movie()
	movie.movie_id = movie_row[0]
	movie.imdb_id = str(movie_row[1])
	movie.title = str(movie_row[2])
	movie.director = str(movie_row[3])
	movie.release_year = movie_row[4]
	movie.avg_rating = movie_row[5]
	print(movie.title)
	movie.save()


if __name__ == "__main__":

	if len(sys.argv) == 2:

		print ("Reading from file " + str(sys.argv[1]))
		movies_df = pd.read_csv(sys.argv[1])
		movies_df.apply(save_movie_from_row,axis=1)
		print ("There are {} movies ".format(Movie.objects.count()))

	else:
		print ("Please , provide Wine file path")