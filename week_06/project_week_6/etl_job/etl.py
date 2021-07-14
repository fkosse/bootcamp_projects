import pymongo
import time
import logging
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

time.sleep(10)  # seconds

webhook_url = ""

s  = SentimentIntensityAnalyzer()

pg = create_engine('postgresql://tweet_collector: @postgresdb:5432/tweet_collections', echo=True)

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use withing the MongoDB server
db = client.tweets

# Select the collection of documents you want to use withing the MongoDB database
collection = db.tweet_data

pg.execute("CREATE TABLE IF NOT EXISTS tweets (username VARCHAR(256), text TEXT, sentiment NUMERIC, followers INTEGER);")

entries = collection.find()

for e in entries:
    sentiment = s.polarity_scores(e['text'])  # assuming your JSON docs have a text field
    username = e['username']
    text = e['text']
    score = sentiment['compound']
    followers = e['followers_count']
    query = "INSERT INTO tweets VALUES (%s, %s, %s, %s);"
    pg.execute(query, (username, text, score, followers))
    print(e)
    print(sentiment)

while True:
    query = "SELECT text, sentiment FROM tweets ORDER BY RANDOM() LIMIT 1;"
    bot_tweet = pg.execute(query).fetchall()
    logging.critical(str(bot_tweet[0][1]))

    if bot_tweet[0][1] < 0:
        smiley = ":("
    elif bot_tweet[0][1] == 0:
        smiley = "\U0001F610"
    elif bot_tweet[0][1] > 0:
        smiley = ":)"

    data = {'text' : bot_tweet[0][0] + " . " + smiley }
    requests.post(url=webhook_url, json = data)
    time.sleep(20)




