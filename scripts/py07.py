import random
import string
import numpy as np

import pandas as pd
from scipy.stats import skewnorm

## Code for creating weeks


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Get the date today
def createWeeks():# so far set to only work for 3 years back
    today = datetime.now()
    # Get the date three years ago
    three_years_ago = today - relativedelta(years=3)
    # Initialize a list to hold all the days
    days = []
    # Start from the date three years ago
    current_date = three_years_ago
    # While the current date is before today
    while current_date <= today:
        # Add the current date to the list of days
        days.append(current_date)
        # Add one day to the current date
        current_date += timedelta(days=1)
    # Initialize a list to hold all the weeks
    weeks = []
    # Start from the first day
    current_day = 0
    # While there are still days left
    while current_day < len(days):
        # Get the next 7 days
        week = days[current_day:current_day+7]
        
        # Add the week to the list of weeks
        weeks.append(week)
        
        # Move to the next week
        current_day += 7
    
    # Print the first 5 weeks
    for i in range(5):
        print('Week', i+1, ':', weeks[i])
    return weeks
    
        ### ene of code for creating weeks

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_tweets(tweet_dates):
    tweets = []
    for date in tweet_dates:
        tweet_text = generate_random_string()
        tweets.append((date, tweet_text))
    return tweets


def tweetDatesGenOne(age):
    tweetdates=[]
    rate = age_group(age)
    #create weeks object
    weeks = createWeeks()# weeks 
    #Now apply the rate 
    for week in weeks: # for each week we select random dates and add to our tweet_dates
        num_tweets = np.random.poisson(rate)
        tweetdates += list(np.random.choice(week, size=num_tweets, replace=True))
    return tweetdates

def age_group(x):
    if 16 <= x <= 25:
        return 8
    elif 26 <= x <= 35:
        return 6
    elif 36 <= x <= 45:
        return 4
    elif 46 <= x <= 55:
        return 3
    elif 56 <= x <= 65:
        return 2
    elif 66 <= x <= 75:
        return 1
    elif x >= 76:
        return 0
    else:
        return 0



# Code for generating ages


# skewnorm requires location parameter to be zero to maintain the skew direction correctly. So we adjust after generation
def genAges(numberofAges):
    skewness = -5 # Positive values are right skewed as more people on twitter are younger
    rand_var = skewnorm.rvs(a=skewness, loc=40, scale=10, size=numberofAges)
    return rand_var


## putting everything together
# create a list of ages. For each age we will then create tweets appropriately. 

        
def genTweetsAll(howmany):
    # set up a weeks object
    data = []# will be all the tweets
    
    x = genAges(howmany)
    
    # for each age in our list generate the tweets for a user of that age and add it to our "data"
    for y in x:
        dates = tweetDatesGenOne(y)#create the dates based on ages
        tweets = generate_tweets(dates)# create the tweets based on dates
        # append the age y to the each tuple in the list tweets thus creating entire records
        tweetstriples = [(y,) + tweet for tweet in tweets]
        data.append(tweetstriples)
        
    return data


#flattening and dataframes
# Generate the data
data = genTweetsAll(100)
# Flatten the data
flat_data = [item for sublist in data for item in sublist]
# Create a DataFrame
df = pd.DataFrame(flat_data, columns=['Age', 'Date', 'Tweet Content'])
# Print the DataFrame
print(df)



if __name__ == '__main__':
    # Put the number of tweets you want to generate here
    num_tweets = 100
    tweets_data = genTweetsAll(num_tweets)
    flat_data = [item for sublist in tweets_data for item in sublist]
    df = pd.DataFrame(flat_data, columns=['Age', 'Date', 'Tweet Content'])
    print(df)



    # For testing, print out the first 10 records
    #for record in tweets_data[:10]:
        #print(record)
