from tkinter import *

def classify():
    num = entry.get()
    i = 2
    div = int(num) / int(i)
    while i <= int(num):
        if i == int(num):
            print(num + " " + "is a prime number.")
            break 
        elif div.is_integer():
            print(num + " " + "isn't a prime number.")
            break       
        i += 1
        div = int(num) / int(i)

window = Tk()

butt = Button(window, text="Click to classify.", command=classify)
butt.pack(side = BOTTOM)

entry = Entry()
entry.config(font=(20))
entry.insert(0, "Enter your number here.")
entry.pack()

window.mainloop() 