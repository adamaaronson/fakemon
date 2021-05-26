import tweepy
import time
from os import environ
from fakemon import generate_fakemon

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

interval = 60 * 60 * 2
# interval = 30 # just for testing!!!

while True:
    fakemon = generate_fakemon()
    api.update_status(str(fakemon))
    print('Successfully tweeted!')
    time.sleep(interval)
