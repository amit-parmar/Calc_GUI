from tkinter import *
main_window = Tk()

Label(main_window, text= "Enter Your name").grid(row = 0, column = 0)
Label(main_window, text= "Enter Your Age").grid(row = 1, column = 0)

my_name = Entry(main_window, width = 50, borderwidth=5)
my_name.grid(row = 0, column=1)
my_age = Entry(main_window, width = 50, borderwidth=5)
my_age.grid(row = 1, column =1)

def print_it():
    print(f"my name is: {my_name.get()}, my age is: {my_age.get()} ")

Button(main_window, text = "click_it", command=print_it ).grid(row = 2, column = 1)


main_window.mainloop()