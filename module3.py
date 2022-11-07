











from tkinter import *



root = Tk()

label = Label(master=root,
              text='Hello World',
              background='yellow',
              width=100,
              height=30)
label.pack()
button = Button(master=root, text='Press', command=onclick)
button.pack(pady=10)


root.mainloop()