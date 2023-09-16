import tweepy
import time
import random
from dotenv import load_dotenv
import os

print(os.getenv('PATH'))

load_dotenv()  # environment variable

# get the api keys and tokens
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BEARER_TOKEN = os.getenv(r"BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET_KEY = os.getenv("ACCESS_TOKEN_SECRET_KEY")

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET_KEY)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET_KEY)
api = tweepy.API(auth)


# client.create_tweet(text="Test one")

def song_bot():
    with open('lyrics.txt', 'r') as f:
        verses = f.read().split("\n\n")  # split according to empty lines

    random.shuffle(verses)
    tweeted_verse = set()  # creates a set to keep track of tweeted verses to avoid repetition

    for verse in verses:
        verse = verse.strip()  # remove white space

        if verse and (verse not in tweeted_verse):  # two condition: must be a verse and must not be in tweeted_verse
            client.create_tweet(text=verse)
            tweeted_verse.add(verse)  # will store to tweeted_verse now

            time.sleep(20*60*60) # interval of 20 hours for now. I still need to search for a free hosting platform.


song_bot()
