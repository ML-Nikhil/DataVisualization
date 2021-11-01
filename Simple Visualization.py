# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:11:11 2021

@author: Nikhil J
@github: ML-Nikhil
"""
import statistics as ss
import pandas as pd
import seaborn as sns
import plotly
import matplotlib.pyplot as plt
import numpy as np
# Importing the Modified Dataset: DiamondNew

df1 = pd.read_csv('DiamondNew.csv')

# Creating Simple visualization

# 1. Histogram : range of feature on x and counts on y

plt.hist(df1['carat'])
sns.distplot(df1['carat'])
# the sns plotted a smooth curve : kde kernel density estimation: by default
sns.distplot(df1['carat'],kde=False) # to remove kde
sns.distplot(df1['carat'],kde=False, bins=100)

# Observation : Most carat values are left, so Right Skewed Distribution

# Using Transformed Plots to Show the distribution more sophisticated
# Using Log Transformation on Price

sns.distplot(np.log(df1.price),kde=False)

# The two peaks represents the diamonds with high and low price
# frequency , peak and outliers

# 2.  Bar Plots : Display count of categorical variables
# depicts relationship between categorical variable and numeric value

# To know the Number of diamonds in each cut type
n_cut = pd.crosstab(index =df1['cut'],columns='count')
print(n_cut)
n_cut.plot(kind='bar')
# this sns saves us from creating a n_cut variable 
sns.catplot('cut',data=df1,aspect=1.5,color='olive',kind='count') 
sns.countplot('cut',data =df1) # This is how we can obtain directly the counts

# Mean Price Distribution  of categories

sns.set(style='whitegrid')
ax = sns.barplot(x='cut',y ='price',estimator=np.mean,data =df1)
# Black bar ARE UNCERTAINTY . CI=95 def.

ax = sns.barplot(x='cut',y ='price',estimator=np.mean,data =df1,order=['Ideal','Good','Very Good','Fair','Premium'])

# Creating BarPlot with Grouping a Specific Feature

sns.barplot(x='cut',y='price',data =df1,hue='color')




































