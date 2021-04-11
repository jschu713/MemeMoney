from psaw import PushshiftAPI
import pandas as pd
import datetime as dt

def reddit_scrape(ticker):
    """searches Reddit for comments containing ticker_symbol

    param ticker: stock ticker to be searched
    """
    data = {}

    end_epoch = int(dt.datetime.utcnow().timestamp())

    api = PushshiftAPI()

    # create dictionary with epoch dates as keys (spans a week)
    for day in range(2, 9):
        # data[end_epoch - (day * 86400)] = 0

        test = end_epoch - (day * 86400)
        convert = dt.datetime.fromtimestamp(test)
        data[convert.date()] = 0
        

    # pulls number of comments stock is mentioned in and attaches number to corresponding dictionary keys
    for key in data:
        start_epoch = key
        api_request_generator = api.search_submissions(q=ticker, after=start_epoch, before=end_epoch)
        stock_submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])
        data[key] = stock_submissions.size
        end_epoch = start_epoch

    return data

if __name__ == "__main__":

    # Testing
    print(reddit_scrape("$NAKD"))