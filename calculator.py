#importing necessary libraries like tkinter which is for the user interface generation
from tkinter import *
import tkinter
from tkinter import messagebox

#calculating function
def proces():
    try:
        
        #get input from text box for numbers and operators
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)

        #save numbers as float
        number1=float(number1)
        number2=float(number2)

        #perform operation based on operator
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2

        #displaying answer in the E4 section of the application box
        Entry.insert(E4,0,answer)
        print(answer)

    #defining exceptions that might occur
    except ValueError:
        messagebox.showwarning("ERROR!","Please provide correct inputs.")
    except UnboundLocalError:
        messagebox.showwarning("ERROR!","Please enter the correct operator.")
    except ZeroDivisionError:
        messagebox.showwarning("ERROR!","A number cannot be divided by zero.")
        
#defining application's format in rows and columns        
top = tkinter.Tk()
L1 = Label(top, text="-----------------CALCULATOR APPLICATION-----------------",).grid(row=0,column=0)
L2 = Label(top, text="Enter first number:",).grid(row=1,column=0)
L3 = Label(top, text="Enter second number:",).grid(row=2,column=0)
L4 = Label(top, text="Choose the operation (+ or - or * or /):",).grid(row=3,column=0)
L4 = Label(top, text="Answer:",).grid(row=4,column=0)

#getting numbers and operatora as input
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)

#getting answer here
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Calculate",command = proces).grid(row=5,column=1,)

top.mainloop()
