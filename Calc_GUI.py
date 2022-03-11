from tkinter import *
main_window = Tk()
main_window.title("Amit's Calc")
# Display
e = Entry(main_window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=35)


#numbers on display

def number_display(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(0, str(current_value)+str(number))

def clear():
    list_number.clear()
    e.delete(0, END)

def Add():
    num1 = e.get()
    global n1
    global math
    math = "add"
    n1 = int(num1)
    e.delete(0, END)

def Sub():
    num1=e.get()
    global n1
    global math
    math = "sub"
    n1 = int(num1)
    e.delete(0, END)


def Mul():
    num1 = e.get()
    global n1
    global math
    math = "mul"
    n1 = int(num1)
    e.delete(0, END)

def Div():
    num1 = e.get()
    global n1
    global math
    math = "div"
    n1 = int(num1)
    e.delete(0, END)

def Equal():
    num2 = e.get()
    e.delete(0, END)
    if(math == "add"):
        e.insert(0, n1 + int(num2))
    if (math == "sub"):
        e.insert(0, n1 - int(num2))
    if (math == "mul"):
        e.insert(0, n1 * int(num2))
    if (math == "div"):
        e.insert(0, n1 / int(num2))

#Digits

but9 = Button(main_window, text = "9", padx=45, pady=20, command=lambda :number_display(9)).grid(row = 1, column = 0 )
but8 = Button(main_window, text = "8", padx=45, pady=20, command=lambda :number_display(8)).grid(row = 1, column = 1 )
but7 = Button(main_window, text = "7", padx=45, pady=20, command=lambda :number_display(7)).grid(row = 1, column = 2 )

but6 = Button(main_window, text = "6", padx=45, pady=20, command=lambda :number_display(6)).grid(row = 2, column = 0 )
but5 = Button(main_window, text = "5", padx=45, pady=20, command=lambda :number_display(5)).grid(row = 2, column = 1 )
but4 = Button(main_window, text = "4", padx=45, pady=20, command=lambda :number_display(4)).grid(row = 2, column = 2 )

but3 = Button(main_window, text = "3", padx=45, pady=20, command=lambda :number_display(3)).grid(row = 3, column = 0 )
but2 = Button(main_window, text = "2", padx=45, pady=20, command=lambda :number_display(2)).grid(row = 3, column = 1 )
but1 = Button(main_window, text = "1", padx=45, pady=20, command=lambda :number_display(1)).grid(row = 3, column = 2 )

but0 = Button(main_window, text = "0", padx=45, pady=20, command=lambda :number_display(0)).grid(row = 4, column = 1 )

butadd = Button(main_window, text = "+", padx=45, pady=20, command=Add ).grid(row = 5, column = 0 )
butsub = Button(main_window, text = "-", padx=45, pady=20, command=Sub ).grid(row = 5, column = 1 )
butmul = Button(main_window, text = "x", padx=45, pady=20, command=Mul ).grid(row = 5, column = 2 )
butdiv = Button(main_window, text = "/", padx=45, pady=20, command=Div ).grid(row = 6, column = 0 )

butcls = Button(main_window, text = "cls", padx=45, pady=20, command=clear ).grid(row = 6, column = 1 )
buteql = Button(main_window, text = "=", padx=45, pady=20, command= Equal ).grid(row = 6, column = 2 )


main_window.mainloop()
