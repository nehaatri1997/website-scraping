# website-scraping

Web Scraping and Data Analysis Project

This project demonstrates basic web scraping from Medium to extract article titles and perform data analysis and visualization on sample text data. The project uses requests and BeautifulSoup for web scraping, TextBlob for sentiment analysis, and matplotlib for data visualization.

# Project Overview
1. Web Scraping: Connects to Medium's website, extracts article titles, and displays the title of the first article.
2. Sentiment Analysis: Analyzes the sentiment of a sample text using TextBlob.
3. Data Visualization: Generates a bar chart based on example data.
   
# Requirements
Python 3.x
Packages: requests, beautifulsoup4, textblob, matplotlib, pandas

# Code Structure
Web Scraping (Medium Article Titles)
  Sends a request to Medium's homepage.
  Parses the page using BeautifulSoup to extract article titles from <h2> tags.
  Finds and prints the title of the first article for demonstration.

Sentiment Analysis (TextBlob)
  Analyzes the sentiment of a sample sentence.
  Prints sentiment as polarity and subjectivity values.

Data Visualization (Matplotlib and Pandas)
  Creates a simple DataFrame for demonstration.
  Visualizes the frequency of sample values in a bar chart.

