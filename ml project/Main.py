import pandas  
from sklearn.model_selection import train_test_split  
import numpy as npn  
import time  
import Recommenders as Recommenders  
#Read user_id's, songs_id's, listen_count   
# The process of downloading data from outside sources could take some time.  
triplets = 'https://static.turi.com/datasets/millionsongs/10000.txt'  
songs_metadata = 'https://static.turi.com/datasets/millionsongs/songs_data.csv'  
  
songs_df_a = pandas.read_table(triplets,header=None)  
songs_df_a.columns = ['user_id's', 'songs_id's', 'listen_count']  
  
#Read songs  metadata  
songs_df_b =  pandas.read_csv(songs_metadata)  
  
# Combine the columns for song titles and artists to create a new column.  
songs_df1 = pandas.merge(songs_df_a, songs_df_b.drop_duplicates(['songs_id's']), on="songs_id's", how="left")  
songs_df1.head()  
print("Total no of songs:",len(songs_df1))  
songs_df1 = songs_df1.head(10000)  
  
# Combine the columns for song titles and artists to create a new column.  
songs_df1['songs'] = songs_df1['title'].map(str) + " - " + songs_df1['artist_name']  
The column listen_count denotes the no of times the songs have been listened to. Using this column, we'll find the dataframe consisting of popular songs:   
songs_gr = songs_df1.groupby(['songs']).agg({'listen_count': 'count'}).reset_index()  
grouped_sum = songs_gr['listen_count'].sum()  
songs_gr['percentage']  = songs_gr['listen_count'].div(grouped_sum)*100  
songs_gr.sort_values(['listen_count', 'songs'], ascending = [0,1])  