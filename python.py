import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
df = pd.read_csv("netflix_data.csv")
df.head()
df.tail()
df.info() # there are 2 numerical variables and 10 categorical variables in the dataset. There exists some missing values in the dataset.
df.shape # there are 6234 rows and 12 columns in the dataset.
df.describe(include="object").T # statistical summary of the columns with categorical variables in the dataset.
'''
there are two genre types in the dataset with Movie having the highest view of 4265
the most viewed title is Limitless
the director with the most view is Rul Campos, Jan Suter
United States is the most featured country 
TV-MA has the highest rating with 2027 count.
'''
df.duplicated().sum() # there are no duplicates in the dataset.
df.isnull().sum() # there are missing values in the columns : director, cast. country. date_added and rating.
'''
To treat missing values, 
delete rows where missing values exist in the columns date_added and rating because it appears insignificant"
replace the mode (United States) in rows with missing values for the country column
introduce a placeholder "Other" for missing rows in the director and cast columns.
'''
df1= df.copy() # make a copy of the original dataset
df1.columns
df1.dropna(subset=["date_added", "rating"], inplace=True) # drop rows with missing values in columns date_added and rating
df1["country"] = df1["country"].fillna(df1["country"].mode()[0]) # Replace missing values in the country column with its mode.
df1[["director", "cast"]] = df1[["director", "cast"]].fillna("Other") # introduce a placeholder "Other" to replace missing values in the director and cast columns respectively.
df1.isnull().sum() # there are no more missing values in the dataset.
'''
Perform Data visualisation on the dataset using the seaborn, matplotlib and pyplot libraries respectively
'''
sns.countplot(data=df,x='type') # use the countplot in the seaborn library to view the most watched type.
plt.xticks(rotation=90)
plt.title('Most Watched Type')
plt.show()
# Use Matplotlib to visualise the rating distribution
type_counts = df1["type"].value_counts() # count the total ratings using value_counts()
plt.bar(type_counts.index, type_counts.values, color = ["lightblue", "lightgreen"]) # Using Matplotlib, create the bar plot
plt.xticks(rotation=90) # Customize the plot
plt.title('Most Watched Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show() # Display the plot
# Use Plotly to visualise the rating distribution
type_counts = df1['type'].value_counts() # calculate the ratings value counts.
fig= go.Figure(go.Bar(x=type_counts.index, y= type_counts.values, marker_color = ["lightgreen", "lightcoral"]))
fig.update_layout ( # Customize the plot
    title='Most watched Type',
    xaxis_title='Type',
    yaxis_title='Count',
    xaxis_tickangle=-45,
    template='plotly_dark'
)
fig.show() # Display the plot
'''
From the data visualisation, the most watched genre type is movies.
use seaborn, matplotlib and plotly to visualise the ratings distribution
'''
sns.countplot(data=df1,x='rating',hue ='type', palette ='Set1') # use seaborn to visualise the ratings distribution
plt.xticks(rotation=90) # Customise the plot
plt.title('Rating Distribution')
plt.show() # Dispaly the plot
# Use Matplotlib to visualise the rating distribution
rating_counts = df1['rating'].value_counts() # calculate the ratings value counts.
plt.bar(rating_counts.index, rating_counts.values) # Using Matplotlib, create the bar plot
plt.xticks(rotation=90) # Customize the plot
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show() # Display the plot
# Use Plotly to visualise the dataset
rating_counts = df1['rating'].value_counts() # calculate the ratings value counts.
fig= go.Figure(go.Bar(x=rating_counts.index, y= rating_counts.values)) # Using Plotly to create the bar plot
fig.update_layout ( # Customize the plot
    title='Rating Distribution',
    xaxis_title='Rating',
    yaxis_title='Count',
    xaxis_tickangle=-45,
    template='plotly_dark'
)
fig.show() # Display the plot
'''
From the data visualisation, genre type: movies have the highest rating and TV-MA rated highest amongst all the ratings followed by TV-14 and R.
'''