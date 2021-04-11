from alpha_vantage.timeseries import TimeSeries
import datetime
import config_stock_price
from dateutil import parser

# Method returns a dictionary containing date : close price of the stock
def get_stock_prices(stock_symbol):
    # User needs to get their own API key from Alpha Vantage
    API_KEY = config_stock_price.api_key

    # Number of days before today to extract data from
    NUM_DAYS = 7

    # Gets daily stock prices from API
    try:
        time_series = TimeSeries(key=API_KEY, output_format='json')
        data, meta_data = time_series.get_daily(symbol=stock_symbol)

        # Creates a dictionary to store dates and close prices of the stock
        stock_prices = {}

        # Gets today's date
        today = datetime.date.today()

        # Copies data from the specified number of previous days, excluding days that U.S. market is closed
        num_previous_day = 1
        time_delta = 1
        while num_previous_day <= NUM_DAYS:
            previous_date = str(today - datetime.timedelta(days=time_delta))
            if previous_date in data.keys():
                stock_prices[parser.parse(previous_date).date()] = data[previous_date]['4. close']
                num_previous_day += 1
            time_delta += 1

        # Returns a dictionary with dates and close prices
        return stock_prices

    # Returns error when ticker does not exist
    except ValueError:
        error = 'no such ticker'
        return error

if __name__ == "__main__":

    # Testing
    print(get_stock_prices("ELYS"))
