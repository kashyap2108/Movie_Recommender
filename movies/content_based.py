import sys,os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import linear_kernel , cosine_similarity
os.environ.setdefault("DJANGO_SETTINGS_MODULE","movie_rs.settings")

from .models import Movie,Genre,Cast

def content_based(movie):
	movies = Movie.objects.all()
	z=[]
	for m in movies:
		genres = Genre.objects.filter(movie=m)
		genre_list = ''
		for genre in genres:
			genre_list = genre_list + ' ' + str(genre)
		cast = Cast.objects.filter(movie=m)
		cast_list = ''
		for c in cast:
			cast_list = cast_list + ' ' + str(c)
		lopo = [m.movie_id,m.title,m.avg_rating,m.director,m.release_year,genre_list,cast_list]
		z.append(lopo)
	df = pd.DataFrame(data=z)
	df.columns = ['movie_id','title','avg_rating','director','Release_Year','genres','cast']
	df['soup'] = df['director'] + df ['genres'] + df['cast']
	print(df.head(2))
	# count = CountVectorizer(analyzer='word',ngram_range=(1,2),min_df=0,stop_words='english')
	# count_matrix = count.fit_transform(df['soup'])
	# cosine_sim = cosine_similarity(count_matrix,count_matrix)
	# cosine_sim.to_pickle('cosine_sim.pkl')
	df.to_pickle('cb_frame.pkl')
	# df = df.reset_index()
	# titles = df['title']
	# indices = pd.Series(df.index,index=df['title'])
	# idx = indices[movie_title]
	# sim_scores = list(enumerate(cosine_sim[idx]))
	# sim_scores = sorted(sim_scores,key=lambda x : x[1],reverse = True)
	# sim_scores = sim_scores[1:31]
	# movie_indices = [i[0] for i in sim_scores]
	# return titles.iloc[movie_indices][:10]

