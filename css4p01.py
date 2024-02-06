# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:04:33 2024

@author: Lerato
"""

import pandas as pd 

# Do: Extracting, Tranforming and Loading of data
df = pd.read_csv("movie_dataset.csv")
#df.dropna(inplace=True)


# Do: Exploratory Data Analysis
A1 = df['Title'] [df['Rating'] == df['Rating'].max()] 


A2 = df['Revenue (Millions)'].mean()


A3 = df[df['Year'] >= 2015][df['Year'] <= 2017]['Revenue (Millions)'].mean()


A4 = len(df[df['Year'] == 2016])



A5 = len(df[df['Director'] == 'Christopher Nolan'])


A6 = len(df[df['Rating'] >= 8.0])


A7 = df['Rating'][ df['Director'] == 'Christopher Nolan' ].median()



year_group = df.groupby(['Year']).mean()
A8 = year_group['Rating'].idxmax()


movs_2006 = len(df[df['Year'] == 2006])
movs_2016 = len(df[df['Year'] == 2016])
A9 = ((movs_2016-movs_2006)/movs_2006)*100

actors_series = df['Actors']
all_actors = [actor.strip() for actors in actors_series.str.split(',') for actor in actors]             
all_actors_series = pd.Series(all_actors)
A10 = all_actors_series.value_counts().idxmax()
                     
genres_series = df['Genre']
all_genres = [genres.strip() for genres in genres_series.str.split(',')for genres in genres]
all_genres_set = set(all_genres)
A11 = len(all_genres_set)

matrix = df.corr()




