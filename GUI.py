import tkinter as tk
import tkinter.font
from ttkthemes import ThemedTk
from tkinter import ttk, messagebox
from tkinter import *

from twitter_data import twitter_scrape
from stocks import reddit_scrape
from stock_price import get_stock_prices
import datetime


class GUI:
    """
    The GUI class
    """

    def __init__(self):
        """
        Creates the main window and sets themes, style, and size
        """

        self._root = ThemedTk(theme="arc")
        self._root.title("MemeMoney")
        self._root.iconbitmap("iconimg\mememoney.ico")
        self._root.configure(bg="#f5f6f7")
        self._root.grid_columnconfigure(0, weight=1)
        self._root.geometry("800x600")

    def create_welcome_frame(self):
        """
        Creates the frame in which the title, subtitle, keyword request, and data will be displayed.
        """

        # sets font
        welcome_font = tk.font.Font(size=24, weight="bold")
        welcome_desc_font = tk.font.Font(size=12)
        sub_welcome_font = tk.font.Font(size=10)
        sub_welcome_font_bold = tk.font.Font(size=10, weight="bold", underline=True)

        # creates the frame w/ style, size, position
        welcome_frame = ttk.Frame(self._root)
        welcome_frame.grid(column=0, row=0, padx=20, pady=5, sticky="ew")
        welcome_frame.grid_columnconfigure(0, weight=1)

        # title and subtitle text
        welcome = ttk.Label(welcome_frame, text="MemeMoney", font=welcome_font, foreground="#000000")
        welcome.grid(column=0)

        welcome_desc = ttk.Label(welcome_frame, text="Providing you with hyped stock data.", font=welcome_desc_font)
        welcome_desc.grid(column=0, pady=10)

        # instruction text
        instr = ttk.Label(welcome_frame, text="Instructions:", font=sub_welcome_font_bold, wraplength=600, anchor="w")
        instr.grid(column=0, sticky="w", padx=86)

        instr_desc = "Enter a stock symbol and the program will display a table with " \
                     "the number of Reddit and Twitter mentions, the stock's closing price, " \
                     "and the price differential from one day to the next, for the previous " \
                     "three days, excluding weekends."

        instructions = ttk.Label(welcome_frame, text=instr_desc, font=sub_welcome_font, wraplength=600)
        instructions.grid(column=0, pady=5)

        # gets user input for keyword search for stock symbol
        input_request = ttk.Label(welcome_frame, text="Please enter a stock symbol (letters only):",
                                  font=welcome_desc_font)
        input_request.grid(column=0, pady=10)

        # creates entry field for user to type in input
        stock_entry = ttk.Entry(welcome_frame, width=30, font=welcome_desc_font)
        stock_entry.grid(column=0, pady=10)

        def get_entry():
            """
            Inner function that retrieves the user entered term to provide keyword to search
            """

            attempted_keyword = stock_entry.get()

            # checks to see if term is valid, based on US stock exchanges
            # only letters and less than 5 letters
            if attempted_keyword.isalpha() and len(attempted_keyword) <= 5:
                keyword = "$" + str(attempted_keyword.upper())
                return keyword

            # else messagebox pops up and provides an error
            else:
                messagebox.showinfo("Invalid Entry", "You did not enter a valid search term.")
                stock_entry.delete(0, "end")  # clears the entry box if invalid entry

        def get_data(platform):
            '''
            Inner function that gets the data from Reddit, Twitter, and Stock API's.

            Takes the platform as a parameter and returns a list of the data.
            '''

            keyword = get_entry()

            data_source = None

            # determines which function to call
            if platform == "twitter":
                data_source = twitter_scrape(keyword)
            if platform == "reddit":
                data_source = reddit_scrape(keyword)
            if platform == "stock_price":
                keyword = get_entry().strip("$")
                data_source = get_stock_prices(keyword)

            # if stock does not exist return nothing
            if data_source == "no such ticker":
                messagebox.showinfo("Invalid Entry", "Stock does not exist.")
                stock_entry.delete(0, "end")  # clears the entry box if invalid entry
                return

            day_delta = datetime.timedelta(days=1)
            today = datetime.date.today()

            data_list = []

            # creates list of [dates, mentions]
            for things in range(7):
                the_day = today - (things * day_delta)

                if the_day.isoweekday() != 6 and the_day.isoweekday() != 7 and the_day != today:
                    the_date = the_day
                    mentions = data_source[the_date]

                    data_list.append([the_date, mentions])

            return data_list

        def create_table():
            """
            Creates display table for twitter and reddit mentions, and stock price
            """

            # calls functions to get data to display
            twitter_data = get_data("twitter")
            reddit_data = get_data("reddit")
            stock_price_data = get_data("stock_price")

            # if stock does not exist return nothing
            if stock_price_data is None:
                return

            # creates table frame
            table_frame = ttk.Frame(self._root)
            table_frame.grid(column=0, row=1, padx=20, pady=5, sticky="ew")
            table_frame.grid_columnconfigure(0, weight=1)

            # creates table foundation - tkinter treeview
            table = ttk.Treeview(table_frame)
            style = ttk.Style()
            style.configure('Treeview', rowheight=20)

            table['columns'] = ('Date', 'Close Price', 'Reddit Mentions', 'Twitter Mentions', 'Total Mentions',
                                'Price Diff from Prev Day', 'Mention Diff from Prev Day')
            table.column('#0', width=0, stretch=NO)
            table.column('Date', anchor=CENTER, width=75)
            table.column('Close Price', anchor=CENTER, width=75)

            table.column('Reddit Mentions', anchor=CENTER, width=100)
            table.column('Twitter Mentions', anchor=CENTER, width=100)
            table.column('Total Mentions', anchor=CENTER, width=100)
            table.column('Price Diff from Prev Day', anchor=CENTER, width=150)
            table.column('Mention Diff from Prev Day', anchor=CENTER, width=150)

            table.heading('#0', text='', anchor=W)
            table.heading('Date', text='Date', anchor=CENTER)
            table.heading('Close Price', text='Close Price', anchor=CENTER)

            table.heading('Reddit Mentions', text='Reddit Mentions', anchor=CENTER)
            table.heading('Twitter Mentions', text='Twitter Mentions', anchor=CENTER)
            table.heading('Total Mentions', text='Total Mentions', anchor=CENTER)
            table.heading('Price Diff from Prev Day', text='Price Diff from Prev Day',
                          anchor=CENTER)
            table.heading('Mention Diff from Prev Day', text='Mention Diff from Prev Day',
                          anchor=CENTER)

            # creates the table
            id = 0
            first_index = 0

            for items in range(3):

                # makes sure the dates are all the same one
                if twitter_data[first_index][0] == reddit_data[first_index][0] and \
                        twitter_data[first_index][0] == stock_price_data[first_index][0] and \
                        reddit_data[first_index][0] == stock_price_data[first_index][0]:

                    total = reddit_data[first_index][1] + twitter_data[first_index][1]

                    # calculates mention and price differentials
                    try:
                        prev_total = reddit_data[first_index + 1][1] + twitter_data[first_index + 1][1]
                        prev_price = float(stock_price_data[first_index + 1][1])

                        if first_index < 2:
                            mention_diff = total - prev_total
                            price_diff = round(float(stock_price_data[first_index][1]) - prev_price, 3)
                        else:
                            mention_diff = "N/A"
                            price_diff = "N/A"
                    except IndexError:
                        mention_diff = "N/A"
                        price_diff = "N/A"

                    # creates the data rows for the table
                    table.insert(parent='', index='end', iid=id, text='', values=(twitter_data[first_index][0],
                                                                                  stock_price_data[first_index][1],
                                                                                  reddit_data[first_index][1],
                                                                                  twitter_data[first_index][1],
                                                                                  total,
                                                                                  price_diff,
                                                                                  mention_diff))

                    id += 1
                    first_index += 1

            table.pack(pady=20)

        # button that when pushed retrieves the user entered keyword
        search_button = ttk.Button(welcome_frame, text="Get Results", command=lambda: [create_table()])
        search_button.grid(column=0, pady=5)

    def end(self):
        """
        Closes out the root for the GUI
        """

        return self._root.mainloop()


gui = GUI()
gui.create_welcome_frame()
gui.end()
