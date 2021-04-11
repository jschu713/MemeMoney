import tkinter as tk
import tkinter.font
from ttkthemes import ThemedTk
from tkinter import ttk, messagebox
from tkinter import *

from twitter_data import twitter_scrape
import datetime

class GUI:
    '''
    The GUI class
    '''

    def __init__(self):

        # creates the main window, sets thems, style, and, size
        self._root = ThemedTk(theme="arc")
        self._root.title("MemeMoney")
        self._root.configure(bg="#f5f6f7")
        self._root.grid_columnconfigure(0, weight=1)
        self._root.geometry("800x600")

    # def create_table_frame(self):
    #     # creates the frame w/ style, size, position
    #     table_frame = ttk.Frame(self._root)
    #     table_frame.grid(column=0, row=1, padx=20, pady=5, sticky="ew")
    #     table_frame.grid_columnconfigure(0, weight=1)
    #
    #     test = ttk.Label(table_frame, text="Table Goes Here", foreground="#000000")
    #     test.grid(column=0)

    def create_welcome_frame(self):
        '''
        Creates the frame in which the title, subtitle, keyword request, and data will be displayed.
        '''

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
            '''
            Inner function that retrieves the user entered term to provide keyword to search
            '''

            attempted_keyword = stock_entry.get()

            # checks to see if term is valid, based on US stock exchanges
            # only letters and less than 5 letters
            if attempted_keyword.isalpha() and len(attempted_keyword) <= 5:
                keyword = "$" + str(attempted_keyword.upper())
                return keyword

            # else messagebox pops up and provides an error
            else:
                messagebox.showinfo("Invalid Entry", "You did not enter a valid search term.")
                stock_entry.delete(0, "end")            # clears the entry box if invalid entry

        def get_twitter_data():
            keyword = get_entry()

            twitter_data = twitter_scrape(keyword)

            day_delta = datetime.timedelta(days=1)
            today = datetime.date.today()

            for things in range(7):
                the_day = today - (things * day_delta)

                if the_day.isoweekday() != 6 and the_day.isoweekday() != 7 and the_day != today:
                    the_date = the_day
                    mentions = twitter_data[the_date]

                    return the_date, mentions

        def create_table():

            twitter_data = get_twitter_data()

            table_frame = ttk.Frame(self._root)
            table_frame.grid(column=0, row=1, padx=20, pady=5, sticky="ew")
            table_frame.grid_columnconfigure(0, weight=1)

            table = ttk.Treeview(table_frame)
            style = ttk.Style()
            style.configure('Treeview', rowheight=25)

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

            # to test the table format with manually entered data
            table.insert(parent='', index='end', iid='0', text='', values=('2021-04-08', 52.12, 100, 200, 300, 10, 10))
            table.insert(parent='', index='end', iid='1', text='', values=(twitter_data[0], 52.12, 100, 200,
                                                                           twitter_data[1], 10, 10))


            table.pack(pady=20)

        # button that when pushed retrieves the user entered keyword
        search_button = ttk.Button(welcome_frame, text="Get Results", command=lambda: [create_table()])
        search_button.grid(column=0, pady=10)


    def end(self):
        '''
        Closes out the root for the GUI
        '''

        return self._root.mainloop()

gui = GUI()
gui.create_welcome_frame()
gui.end()










