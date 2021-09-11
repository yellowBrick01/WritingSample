# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:55:53 2021

@author: pdmuser
"""
#Import statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

#Reading data from CSV file
data = pd.read_csv('clean_listings.csv')


#Creating a copy of dataframe
df = data.copy()
#print(df.columns)

#Statistics for 'number_of_reviews'
print("Here is an overview of 'number_of_reviews' column:")
print(df['number_of_reviews'].describe())
print('The average number of reviews per listing is:' , round(df.number_of_reviews.mean(),1))
print('The standard deviation of the number of reviews per listing is:' , round(df.number_of_reviews.std(),1))
print('The minimum number of reviews per listing is:' , df.number_of_reviews.min())
print('The 25th percentile of number of reviews per listing is:' , df.number_of_reviews.quantile(0.25))
print('The median of the number of reviews per listing is:' , df.number_of_reviews.quantile(0.5))
print('The 75th percentile of price is:' , df.number_of_reviews.quantile(0.75))
print('The maximum number of reviews per listing is:' , df.number_of_reviews.max())
print("The range of the 'number_of_reviews' column:", df.number_of_reviews.max()-df.number_of_reviews.min())

