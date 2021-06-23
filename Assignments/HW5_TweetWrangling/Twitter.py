"""
Programmer: Chris Tralie / IDS 301 Class
Purpose: To load in Trump's tweets since 11/1/2016, and
         to do some data wrangling on them
"""

import pickle
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# A dictionary for converting from the 3 letter months
# that Twitter gives back to a 2-digit month string
MONTHS = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}


def get_devices(tweets):
    """
    Print out a dictionary which counts how many tweets 
    Trump made on each different type of device
    Parameters
    ----------
    tweets: list of dictionary
        A list of tweets, each of which is a dictionary
    """
    devices = {} # The dictionary will hold "device name":counts
    for tweet in tweets: # This is one way to loop through a list
        device = tweet['source']
        # If the device hasn't been seen yet, we need to make
        # A key for it in the dictionary
        if not (device in devices):
            devices[device] = 0 # Set the initial count to be zero
        devices[device] += 1 # Add one to the counts for this device
    print(devices)

def get_most_favorited(tweets):
    """
    Print out the tweet with the maximum number of retweets
    Parameters
    ----------
    tweets: list of dictionary
        A list of tweets, each of which is a dictionary
    """
    # First, we setup a parallel numpy array with the same
    # number of elements as there are tweets
    counts = np.zeros(len(tweets))
    # Then, this loop fills the list with the retweet counts
    for i, tweet in enumerate(tweets):
        counts[i] = tweet['retweet_count']
    # Finally, we can use the nifty "argmax" function in
    # numpy to pull out the index with the maximum counts
    max_index = np.argmax(counts)
    # We then use this index back in the original tweets list
    # to print out the tweet with the maximum counts
    print(tweets[max_index])

def get_tweet_date(tweet):
    date = tweet['created_at']
    # Separate out date into components in a list
    # Each element is a different component separated
    # by a space
    fields = date.split() 
    # The year is the last field
    year = fields[-1]
    # Use the dictionary defined at the top of the file
    # to convert from a three letter month to a two digit month
    month = MONTHS[fields[1]] 
    # This magic code formats a day to be 2 digits, potentially
    # with a leading zero
    day = "%02d"%int(fields[2]) 
    return year + "/" + month + "/" + day


#tweets = pickle.load(open("trumpSinceElection.dat", "rb"))
tweets = json.load(open("trumpSinceElection.json", "r"))
get_devices(tweets)
get_most_favorited(tweets)
print(get_tweet_date(tweets[0]))