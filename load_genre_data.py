import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE","movie_rs.settings")

import django
django.setup()

from movies.models import Movie,Genre

def save_movie_from_row(movie_row):
	#print(movie_row[0],type(movie_row[1]))
	genre_obj = Genre()
	title = str(movie_row[0])
	print(title)
	genre_obj.movie = Movie.objects.get(title=title)
	genre_obj.genre = str(movie_row[1])
	genre_obj.save()



	


if __name__ == "__main__":

	if len(sys.argv) == 2:

		print ("Reading from file " + str(sys.argv[1]))
		movies_df = pd.read_csv(sys.argv[1])
		movies_df.apply(save_movie_from_row,axis=1)
		print ("There are {} genres ".format(Genre.objects.count()))

	else:
		print ("Please , provide Wine file path")