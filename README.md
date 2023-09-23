# Twitter Bot
This project uses Twitter automation tool to tweet song verses from a chosen artist at a given time interval. 
I have also implemented BeautifulSoup to scrape data from a lyrics website in order to grab the lyrics to hozier's songs and store it in a txt file. The txt file be the source of the tweet content.

check the account here:
```bash
 https://twitter.com/hozier_song
```
## Features
- Random verse selection- This bot randomly select verses from the given source. This is to avoid tweeting an entire song to the the followers' Twitter feed.
  
- No verse repetition- To maintain variety, this twitter bot will store tweeted verses in a set so that each tweets will be distinct
  
- Tweet Frequency-  Since I am using a free developer account, my API rate limit is hinders me from the freedom of tweeting in volume. Hence, the tweet frequency is added to make sure I do not go over the rate limit.
  
## Installation
- Install dotenv to create an environment.
  ```bash
   pip install python-dotenv
  ```

- Install tweepy to access Twitter API
  ```bash
  pip install tweepy
  ```
  
- Install BeautifulSoup
  ```bash
  pip install beautifulsoup4
  ```

## Prerequisites
- Twitter Developer Account
  Create a developer account in order to access Twitter API. This is also needed in order to get API keys and tokens.

- Tweepy Library:
   Tweepy library should be installed to interact with Twitter API.
  
- Song Lyrics Text Files or DataBase:
    A source or multiple sources of song lyrics should be available in order for this project to work.
  
- Twitter API Rate Limits:
   Be aware of Twitter API Limits. This may vary depending on the kind of Developer account you      have. For this project, I am using a free version so the API limit has 50 requests in 24 hours and 1,500 tweets per month.

- BeautifulSoup Knowledge
  In order to get the lyrics from a website the user must have a knowledge on how web scraping works.



