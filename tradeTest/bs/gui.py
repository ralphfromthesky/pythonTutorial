
import tkinter as tk
from tkinter import messagebox as mb

window = tk.Tk()
window.title('BITBOT')
window.geometry("340x400") # parent container like paren div in html
window.configure(bg='#333333')

#FUNCTION HERE
def login():
    pw = '123'
    uN ='ralph'
    if userNameEntry.get() == uN and passWordEntry.get() == pw:
        mb.showinfo(title='SUCCESS!', message='Successfully')
    else:
        mb.showinfo(title='ERROR!', message='wrong')

#CREATE HERE THE ELEMENT HERE
frame = tk.Frame(bg='#333333') # sub-parent container like div inside a div
label = tk.Label(frame, text="Hello, ralph!", bg='#333333', fg='#FFFFFF', font=("Arial", 20))
userNameLabel = tk.Label(frame, text="Username",bg='#333333', fg='#FFFFFF',  font=("Arial", 16))
userNameEntry = tk.Entry(frame)
passWordEntry = tk.Entry(frame, show="*")
passWordLabel = tk.Label(frame, text="Password", bg='#333333', fg='#FFFFFF', font=("Arial", 16))
loginButton =  tk.Button(frame, text="Login" ,bg='#333333', fg='#FFFFFF', font=("Arial", 16))
button = tk.Button(frame, command=login, text="Login" ,bg='#ff3399', fg='#FFFFFF' , font=("Arial", 16))

#SET OR DISPLAY THE ELEMENT HERE

frame.pack()
label.grid(column=2, row=0, sticky='news', columnspan=2, pady=20)
userNameLabel.grid(column=1, row=1, padx=20)
userNameEntry.grid(column=2, row=1, pady=10)
passWordLabel.grid(column=1, row=2)
passWordEntry.grid(column=2, row=2, pady=10)
button.grid(column=2, row=3, columnspan=2, pady=20)




# Run the main event loop
window.mainloop()
print('ralph')
