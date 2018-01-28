from django.shortcuts import render
from django.shortcuts import render , HttpResponseRedirect , redirect , HttpResponse , get_object_or_404
# Create your views here.
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import linear_kernel , cosine_similarity

from django.http import JsonResponse
from .models import Movie,Genre,Cast

def home(request):
	search_query = request.GET.get('search_box',None)
	if request.is_ajax():
		return autocomplete(request)
	if search_query != None:
		search_query = request.GET.get('search_box',None)
		print(search_query)
		movies_list = content_based(str(search_query))
		for k in movies_list:
			print(k[0],k[1],k[2])
		context = {'movies_list' : movies_list}
		return render(request,'content_based.html',context)
	movies_list = Movie.objects.all().order_by('-avg_rating')[:10]
	context = {'movies_list' : movies_list}
	return render(request,'home.html',context)


def movies_genre_wise(request,genre):
	print(genre,'hello')
	movies_list = Genre.objects.all().filter(genre=genre).order_by('-movie__avg_rating')[:10]
	print(movies_list)
	context = {'movies_list' : movies_list}
	return render(request,'genre_list.html',context)


def content_based(movie_title):
	# movies = Movie.objects.all()
	# z=[]
	# for m in movies:
	# 	genres = Genre.objects.filter(movie=m)
	# 	genre_list = ''
	# 	for genre in genres:
	# 		genre_list = genre_list + ' ' + str(genre)
	# 	cast = Cast.objects.filter(movie=m)
	# 	cast_list = ''
	# 	for c in cast:
	# 		cast_list = cast_list + ' ' + str(c)
	# 	lopo = [m.movie_id,m.title,m.avg_rating,m.director,genre_list,cast_list]
	# 	z.append(lopo)
	# df = pd.DataFrame(data=z)
	# df.columns = ['movie_id','title','avg_rating','director','genres','cast']
	# df['soup'] = df['director'] + df ['genres'] + df['cast']
	df = pd.read_pickle('cb_frame.pkl')
	#print(df.head(2))
	#print(df.columns)
	count = CountVectorizer(analyzer='word',ngram_range=(1,2),min_df=0,stop_words='english')
	count_matrix = count.fit_transform(df['soup'])
	cosine_sim = cosine_similarity(count_matrix,count_matrix)
	df = df.reset_index()
	titles = df['title']
	try:
		indices = pd.Series(df.index,index=df['title'])
		idx = indices[movie_title]
		sim_scores = list(enumerate(cosine_sim[idx]))
		sim_scores = sorted(sim_scores,key=lambda x : x[1],reverse = True)
		sim_scores = sim_scores[1:31]
		movie_indices = [i[0] for i in sim_scores]
		movies = df.iloc[movie_indices][['title','Release_Year','avg_rating']]
		movies = movies[:10]
		movies = movies.values.tolist()
		return movies
	except:
		return "No movies Found"



def autocomplete(request):
	if request.is_ajax():
		print('fucks')
	print('sucks')
	q = str(request.GET.get('term',''))
	print('hello',q)
	if request.is_ajax():
		q = str(request.GET.get('term',''))
		print('hello',q)
		movies = Movie.objects.filter(title__icontains=q)[:10]
		results = []
		for r in movies:
			results.append(r.title)
		data = json.dumps(results)

	else:
		data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data,mimetype)
