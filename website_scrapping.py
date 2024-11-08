# -*- coding: utf-8 -*-
"""website scrapping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1atrH_TylvGsFC1ZGczE0ChLbr11ZsBiW
"""

pip install requests beautifulsoup4

# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Step 1 https://www.imdb.com/: Send a request to the website
url = "https://medium.com/"
response = requests.get(url)

# Check if the request was successful (HTTP status code 200 means OK)
if response.status_code == 200:
    print("Successfully fetched the webpage")

    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Extract specific data
    # In this case, we are extracting all the <h2> tags that may contain article titles
    titles = soup.find_all('h2')  # You can modify this based on the website structure

    # Step 4: Print the extracted data
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title.get_text().strip()}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# title of the first article

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the first article title (adjust based on Medium's HTML structure)
    first_article_title_element = soup.find('h3')  # Example: look for the first <h3> tag

    if first_article_title_element:
        first_article_title = first_article_title_element.get_text().strip()
        print("Title of the first article:", first_article_title)
    else:
        print("Could not find the title of the first article.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

soup.find_all('h2', class_='article-title')

"""Natural Language Processing (NLP):"""

from textblob import TextBlob

text = "This is a great product!"
analysis = TextBlob(text)
print(analysis.sentiment)  # Output: Sentiment(polarity=0.8, subjectivity=0.75)

"""Data Visualization"""

import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have data to create a DataFrame
# Replace this with your actual data loading or creation process
data = {'A place to read, write, and deepen your understanding': ['Value1', 'Value2', 'Value3']}
df = pd.DataFrame(data)  # Create the DataFrame 'df'

df['A place to read, write, and deepen your understanding'].value_counts().plot(kind='bar')
plt.show()