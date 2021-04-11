from tkinter import *
from tkinter import ttk

#import stock_price
#data = get_stock_price()

# Tkinter treeview table
root = Tk()
root.title('Table')
root.geometry('900x900')

style = ttk.Style()
style.configure('Treeview',rowheight=25)

table = ttk.Treeview(root)

# Creates columns for the table
table['columns'] = ('Date', 'Close Price', 'Reddit Mentions','Twitter Mentions','Total Mentions',
                    'Price Difference from Previous Day','Mention Difference from Previous Day')
table.column('#0', width=0, stretch=NO)
table.column('Date', anchor=CENTER, width=75)
table.column('Close Price',anchor=CENTER,width=75)
table.column('Reddit Mentions',anchor=CENTER,width=100)
table.column('Twitter Mentions',anchor=CENTER,width=100)
table.column('Total Mentions',anchor=CENTER,width=100)
table.column('Price Difference from Previous Day',anchor=CENTER,width=200)
table.column('Mention Difference from Previous Day',anchor=CENTER,width=210)

# Creates headings for the table
table.heading('#0',text='', anchor=W)
table.heading('Date', text='Date',anchor=CENTER)
table.heading('Close Price', text='Close Price',anchor=CENTER)
table.heading('Reddit Mentions',text='Reddit Mentions',anchor=CENTER)
table.heading('Twitter Mentions',text='Twitter Mentions',anchor=CENTER)
table.heading('Total Mentions',text='Total Mentions',anchor=CENTER)
table.heading('Price Difference from Previous Day',text='Price Difference from Previous Day',anchor=CENTER)
table.heading('Mention Difference from Previous Day',text='Mention Difference from Previous Day',anchor=CENTER)

# Can be used to test the table format with manually entered data
table.insert(parent='',index='end', iid='0', text='',values=('2021-04-08', 52.12, 100, 200, 300, 10, 10))

# Can be used to pass in data from other methods (returned in the form of dictionary)
#id = 0
#for key, value in data.items():
#    table.insert(parent='',index='end', iid=id, text='',values=(key, value, 100, 200, 300, 10, 10))
#    id += 1

table.pack(pady=20)

root.mainloop()