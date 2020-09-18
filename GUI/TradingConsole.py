from service.daily_stocks import StockService

from PIL import Image,ImageDraw,ImageFont,ImageTk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import tkinter as tk
import time

win = tk.Tk()


v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()

p = "PASS"

v1.set(p)
v2.set(p)
v3.set(p)
v4.set(p)

vlist=[v1,v2,v3,v4]

stocks = [
    ("MSFT",1),
    ("AAPL",2),
    ("GOOG",3),
    ("AMZN",4)
]

order = [
    ("BUY","BUY"),
    ("SELL","SELL"),
    ("PASS","PASS")
]

for i in range(3):
    row = 0
    for val,type in enumerate(order):
        tk.Radiobutton(win,text=type[0],padx=20,variable=vlist[i],value=val).grid(row=row,column=i)
        row = row + 1


def place_order():
    txt.configure(text=("ORDERS ",  v1.get(),  v2.get(), v3.get(), v4.get()))

btn_order = tk.Button(win,
                   text="PLACE ORDER",
                   command=place_order)

btn_order.grid(columnspan=4,row=10)

txt = tk.Label(win, text="")
txt.grid(columnspan=4,row=11)

def prepare_frame():
    window_height = 800
    window_width = 900

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    win.geometry("{}x{}+{}+{}".format(window_width,window_height,x_coordinate,y_coordinate))
    import os
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


prepare_frame()

win.mainloop()
