# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:26:53 2021

@author: pdmuser
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

#Reading data from CSV file
data = pd.read_csv('clean_listings.csv')


#Creating a copy of dataframe
df = data.copy()



df['neighbourhood_merged'] = df["neighbourhood_group_cleansed"] +" "+ df["neighbourhood_cleansed"]
#print(df.columns)
#print(df.head(10))
bar_df = df.groupby(['neighbourhood_merged','first_review_year']).mean()[['review_scores_rating']]
#print(bar_df.head(10))
bar_df.reset_index(inplace=True)
bar_df_fin_ver = bar_df.rename(columns = {'index':'group_by_values'})
#num_vars = bar_df_fin_ver.columns[bar_df_fin_ver.dtypes != 'objects']
#print(bar_df_fin_ver[num_vars].isnull())
#print(bar_df_fin_ver.shape)
#bar_df_fin_ver=bar_df_fin_ver[bar_df_fin_ver.review_scores_rating.notnull()]
#print(bar_df_fin_ver.shape)
bar_df_fin_ver_v2 = bar_df_fin_ver.sort_values('review_scores_rating',ascending = False).groupby('neighbourhood_merged').head(2)
#print (bar_df_fin_ver_v2.head(10))
final_df = bar_df_fin_ver_v2.head(100)
#print(final_df.head(25))
#final_df[['borough','neighbourhood']] = final_df.neighbourhood_merged.str.split(".",expand=True)
#print('After column split.')
#print(final_df.columns)
#print(final_df['borough'].unique())
#print(final_df.columns)
final_df= final_df.pivot('neighbourhood_merged','first_review_year','review_scores_rating')
#final_df= final_df.pivot('first_review_year','neighbourhood_merged','review_scores_rating')
#print(final_df.head(10))
#final_df_v2 = final_df.dropna()
#print(final_df_v2)

#print(final_df.head(5))
ax = sns.heatmap(final_df)
plt.title("Heatmap Flight Data")
plt.show()
#sns.set_style("whitegrid")
#x = final_df['neighbourhood_merged']
#y = final_df['review_scores_rating']
#print(x)
#print(y)
#sns.heatmap(final_df)
#sns.barplot(x = 'neighbourhood_merged', y = 'review_scores_rating', hue = 'neighbourhood_merged', data = final_df,
            #palette = 'YlOrBr',
            #saturation = .75,             
            #)
#plt.legend(loc='lower left')

#plt.show()