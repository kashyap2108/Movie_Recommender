import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE","movie_rs.settings")

import django
django.setup()

from movies.models import Movie,Cast

def save_movie_from_row(movie_row):
	#print(movie_row[0],type(movie_row[1]))
	try:
		cast_obj = Cast()
		id = movie_row[0]
		print(id)
		cast_obj.movie = Movie.objects.get(movie_id=id)
		cast_obj.actors = str(movie_row[1])
		cast_obj.save()
	except:
		pass



	


if __name__ == "__main__":

	if len(sys.argv) == 2:

		print ("Reading from file " + str(sys.argv[1]))
		movies_df = pd.read_csv(sys.argv[1])
		print (movies_df.head(3))

		movies_df.apply(save_movie_from_row,axis=1)
		print ("There are {} genres ".format(Cast.objects.count()))

	else:
		print ("Please , provide Wine file path")