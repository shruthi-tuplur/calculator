from calendar import c, different_locale
from itertools import product
from sqlite3 import Row
from timeit import repeat
from tkinter import *
from turtle import bgcolor, clear

root = Tk()
root.title('Simple Calculator')
root.configure(background= 'pink')

e = Entry(root, width = 50, fg = 'black', background= 'pink', borderwidth= 5)
position = 0

e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
 
 


operation = ''
total = 0
number_list = []

def insert_array():
    entryField = int(e.get())
    number_list.append(entryField)
    
def button_clear():
  global position 
  global number_list
  position = 0
  global operation
  e.delete(0, END)  
  operation = 'nothing'  
  number_list = []
  
  
  
def button_addition(): 
    global position 
    position = 0
    global operation
    insert_array()
    x = int(e.get()) 
    operation = "add"
    
def button_multiplication():
    global position
    position = 0 
    global operation
    insert_array()
    operation = "multiply" 
    
def button_division():
    global position
    position = 0
    global operation
    insert_array()
    operation = "divide"    
    
def button_subtraction():
    global position
    position = 0
    global operation
    insert_array()
    operation = "subtract"     
 

def button_click(number):
    global operation
    global number_list
    #storing input in a variable; if x is 0, that means there currently isn't any amount stored in the variable, meaning the calculator is "empty", i.e. it has been cleared
    x = int(number)
    global position
    if position == 0:
        e.delete(0, END)
    e.insert(position, number)
    position += 1 
    
    
def button_equal():
    global y
    global operation
    global number_list
    global total
    insert_array()
    if operation == 'add':
        total = 0
        for n in  number_list:
            total += n 
        print(total)    
        print(number_list)
    elif operation == 'multiply':
        total = 1
        for n in  number_list:
            total *= n    
    elif operation == 'subtract':
        total = 2 * number_list[0]
        print(total)
        for n in number_list:
          print(n)  
          total = total - (n)     
    elif operation == 'divide':
        total = int(number_list[0] ** 2)
        for n in number_list:
          total = total / (n)                     
    e.delete(0, END)
    e.insert(0, total) 
    

  
 

button_1 = Button(root, text = '1', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(9))
button_0 = Button(root, text = '0', padx = 40, pady = 20, fg = 'magenta', command = lambda: button_click(0))


button_c = Button(root, text = 'clear', padx = 225, pady = 20, fg = 'magenta', command = button_clear)
button_equal = Button(root, text = '=', padx = 112, pady = 20, fg = 'magenta', command = button_equal)
button_add = Button(root, text = '+', padx = 39, pady = 20, fg = 'magenta', command = button_addition)
button_subtract = Button(root, text = '-', padx = 39, pady = 20, fg = 'magenta', command = button_subtraction)
button_multiply = Button(root, text = 'x', padx = 39, pady = 20, fg = 'magenta', command = button_multiplication)
button_divide = Button(root, text = '÷', padx = 39, pady = 20, fg = 'magenta', command = button_division)

#put buttons on screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 1, column = 3)
button_subtract.grid(row = 2, column = 3)
button_multiply.grid(row = 3, column = 3)
button_divide.grid(row = 4, column = 3)

button_equal.grid(row = 4, column = 1, columnspan = 2)
button_c.grid(row = 5, column = 0, columnspan = 4)



root.mainloop()