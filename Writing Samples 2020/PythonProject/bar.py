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
bar_df = df.groupby('neighbourhood_merged').mean()[['review_scores_rating']]
#print(bar_df.head())
bar_df.reset_index(inplace=True)
bar_df_fin_ver = bar_df.rename(columns = {'index':'group_by_values'})
#print(bar_df_fin_ver.columns)
bar_df_fin_ver_v2 = bar_df_fin_ver.sort_values('review_scores_rating',ascending = False).groupby('neighbourhood_merged').head(2)
#print (bar_df_fin_ver_v2)
#final_df = bar_df_fin_ver_v2.tail(5)
print(bar_df_fin_ver_v2.head(5),bar_df_fin_ver_v2.tail(5))
#print(final_df)
sns.set_style("whitegrid")


#x = final_df['neighbourhood_merged']
#y = final_df['review_scores_rating']
#print(x)
#print(y)

#sns.barplot(x = 'neighbourhood_merged', y = 'review_scores_rating', hue = 'neighbourhood_merged', data = final_df,
            #palette = 'YlOrBr',
            #saturation = .75,             
            #)
#plt.legend(loc='lower left')
#sns.barplot(data=data, palette="deep")
#plt.show()