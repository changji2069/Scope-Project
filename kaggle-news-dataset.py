import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import pylab as pyplt
plt.rcParams['figure.figsize'] = (6,6)
from keras.preprocessing.text import Tokenizer, text_to_word_sequence

# process Kaggle news-category-dataset to fit the format of NG20, R52, BBC, etc. (labels : {type, news})
# load Kaggle dataset
df_kaggle = pd.read_csv('News_Category_Dataset.csv', encoding = 'ISO-8859-1')

# replace similar categories into root category
arts = ['ARTS','ARTS & CULTURE']
entertainment = ['COMEDY','ENTERTAINMENT','MEDIA']
black_voices= ['BLACK VOICES']
education = ['COLLEGE','EDUCATION']
business =['BUSINESS']
crime = ['CRIME']
good_news = ['GOOD NEWS']
green = ['GREEN']
health = ['HEALTHY LIVING']
impact = ['IMPACT']
latino_voices = ['LATINO VOICES']
parents = ['PARENTS']
LGBTQ = ['QUEER VOICES']
religion = ['RELIGION']
tech = ['SCIENCE','TECH']
sport = ['SPORTS']
food = ['TASTE']
world = ['THE WORLDPOST','WORLDPOST','WORLD NEWS']
travel = ['TRAVEL']
women = ['WOMEN']
politics = ['POLITICS']
categories = [arts, entertainment, black_voices, education, business, crime, good_news, green, health, impact,
              latino_voices, parents, LGBTQ, religion, tech, sport, food, world, travel, women, politics]
categories_str = ['arts', 'entertainment', 'black_voices', 'education', 'business', 'crime', 'good_news', 'green',
              'health', 'impact', 'latino_voices', 'parents', 'LGBTQ', 'religion', 'tech', 'sport', 'food',
              'world', 'travel', 'women','politics']
cate_pair = zip(categories_str, categories )

for name, category in cate_pair:
    for type in category:
        df_kaggle.category = df_kaggle.category.map(lambda x: name if x == type else x)

# remove confusing categories
remove_list = ['STYLE', 'WEIRD NEWS','FIFTY']
for type in remove_list :
    df_kaggle = df_kaggle[df_kaggle.category != type]

# remove date, link, author, and replace category -> type
delete = ['date','link','authors']
for _ in delete :
    del df_kaggle[_]
df_kaggle.rename(columns={'category':'type'})

# using headlines and short_description as 'text' (by defining a new column named 'text')
df_kaggle['text'] = df_kaggle.headline + " " + df_kaggle.short_description
delete2 = ['headline', 'short_description']
for _ in delete2:
    del df_kaggle[_]

# view the filtered dataframe
newcat = df_kaggle.groupby('category')
print(newcat.size())

# saving as json and csv
df_kaggle.to_json('kaggle_filtered.json')
df_kaggle.to_csv('kaggle_filtered.csv')
