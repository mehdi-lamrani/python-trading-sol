import tkinter as tk

app = tk.Tk()
app.geometry('150x100')

radioValue = tk.IntVar()

rdioOne = tk.Radiobutton(app,text='January',
                         variable=radioValue,value=1)
rdioTwo = tk.Radiobutton(app,text='Febuary',
                         variable=radioValue,value=2)
rdioThree = tk.Radiobutton(app,text='March',
                           variable=radioValue,value=3)

rdioOne.grid(column=0,row=0)
rdioTwo.grid(column=0,row=1)
rdioThree.grid(column=0,row=2)

def prepare_frame():
    window_height = 500
    window_width = 900

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    app.geometry("{}x{}+{}+{}".format(window_width,window_height,x_coordinate,y_coordinate))
    import os
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


prepare_frame()

app.mainloop()