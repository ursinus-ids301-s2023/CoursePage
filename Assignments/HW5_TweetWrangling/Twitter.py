import matplotlib.pyplot as plt
import numpy as np
import json

## Months final, for the plot_coronavirus_timeline function
MONTHS = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def get_tweet_date(tweet):
    year = ""
    month = ""
    day = ""
    if "created_at" in tweet:
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
    elif "date" in tweet:
        date = tweet["date"].split()[0]
        year, month, day = date.split("-")
    return year + "/" + month + "/" + day

def get_devices(tweets):
    """
    Print out a dictionary which counts how many tweets 
    Trump made on each different type of device
    Parameters
    ----------
    tweets: list of dictionary
        A list of tweets, each of which is a dictionary
    """
    ## TODO: Fill this in
    pass

def get_most_favorited(tweets):
    """
    Print out the tweet with the maximum number of retweets
    Parameters
    ----------
    tweets: list of dictionary
        A list of tweets, each of which is a dictionary
    """
    ## TODO: Fill this in
    pass


tweets = json.load(open("tweets_01-08-2021.json"))

