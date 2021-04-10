from tweepy import OAuthHandler
from tweepy import API
from config import con_key, con_sec, a_token, a_secret
import datetime
import tweepy as tw

# Testing time to run
# import functools
# import time
#
# def timer(func):
#     @functools.wraps(func)
#
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer
#
# @timer

def twitter(keyword):
        '''
        The twitter function initializes the API authentication and gets all mentions of a specified
        stock symbol within a 3 day period from the current date.

        It takes as a parameter the keyword (stock symbol) to be searched.
        It returns a dictionary with the dates : # of mentions as the key-value pairing.
        '''

        # Consumer key authentication(consumer_key,consumer_secret can be
        # collected from our twitter developer profile)
        auth = OAuthHandler(con_key, con_sec)

        # Access key authentication(access_token,access_token_secret can be
        # collected from our twitter developer profile)
        auth.set_access_token(a_token, a_secret)

        # Set up the API with the authentication handler
        api = API(auth, wait_on_rate_limit=True)

        # takes into account invalid entries, returns nothing if so
        if keyword is None:
            return

        # Set up search parameters
        search_symbol = keyword         # should be the keyword parameter
        ignore_rts = search_symbol + " -filter:retweets"        # ignores retweets

        # Define date ranges we are searching.
        day_delta = datetime.timedelta(days=1)
        today = datetime.date.today()
        end_time = today - 3 * day_delta

        # Searches for tweets with specified keyword and creates list of dates
        tweets = tw.Cursor(api.search, q=ignore_rts, lan="en", since=end_time,).items()
        tweets_list = [tweet.created_at for tweet in tweets]

        # create dictionary to hold date and mention counter
        data = {}

        # establishes data dictionary -- excludes weekend days
        for things in range(7):
            the_day = today - (things * day_delta)

            if the_day.isoweekday() != 6 and the_day.isoweekday() != 7 and the_day != today:
                data[today - (things * day_delta)] = 0

        # increases mention counter by 1 every time a data appears in the tweets_list
        for items in tweets_list:
            if items.date() in data:
                data[items.date()] += 1

        else:
            return data

if __name__ == "__main__":
    print(twitter("$ELYS"))