from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#create window
window = Tk()
window.geometry("300x350")
window.config(bg="purple")

#create image
photo=Image.open("C:\\Users\\nazli\\OneDrive\\Masaüstü\\fotoğraflar\\images.jpg")
photo_size=photo.resize((160,90))
tk_photo=ImageTk.PhotoImage(photo_size)
photo_label=Label(window,image=tk_photo)
photo_label.pack()


#calculator sends message
def calculator():
    try:
        result1=float(my_entry.get())
        result2=float(my_entry2.get())
        output=result1/(result2*result2)
        if result2>3 :
            my_info = messagebox.showinfo("Calculator", "Please enter your height in meters")
        else:
            if  output <= 18.5:
                result_label3.config(text=f"You are weak \nYour body mass index {output}")
            if output > 18.5 and output <= 24.9:
                result_label3.config(text=f"Your weight is normal \nYour body mass index {output}")
            if output > 24.9 and output <= 29.9:
                result_label3.config(text=f"You are overweight \nYour body mass index {output}")
    except:
        my_info = messagebox.showinfo("Calculator", "Please input a number")

#weihgt label
weight_label = Label(window, text="Enter your weight")
weight_label.config(bg="black", fg="white", pady=6, padx=15)
weight_label.pack()

#weight entry
my_entry = Entry(window)
my_entry.focus()
my_entry.pack()

#height label
height_label = Label(window, text="Enter your height")
height_label.config(bg="black", fg="white", pady=6, padx=15)
height_label.pack()

#height entry
my_entry2 = Entry(window)
my_entry2.pack()

#calculator button
my_button = Button(window,text="Calculate",command=calculator)
my_button.config(fg="black",pady=7)
my_button.pack()

#result label
result_label3=Label(window, bg="purple", fg="white")
result_label3.pack()


mainloop()
