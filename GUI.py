import tkinter as tk
import tkinter.font
from ttkthemes import ThemedTk
from tkinter import ttk, messagebox

from twitter_data import twitter

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

        # button that when pushed retrieves the user entered keyword
        search_button = ttk.Button(welcome_frame, text="Get Results", command=lambda: [twitter(get_entry())])
        search_button.grid(column=0, pady=10)

    def end(self):
        '''
        Closes out the root for the GUI
        '''

        return self._root.mainloop()

gui = GUI()
gui.create_welcome_frame()
gui.end()










