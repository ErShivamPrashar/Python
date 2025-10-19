
'''
this program is the simple 
arithematic operation 
using python language
'''

import time
while(1):

    start = time.time()  # start excution time

    first_num1 = float(input("Enter the first number : "))
    first_num2 = float(input("Enter the Second number : "))
    print(f"sum of two number is {first_num1+first_num2}")
    print(f"substract of two number is {first_num1-first_num2}")
    print(f"multiply of two number is {first_num1*first_num2}")
    print(f"divisin of two number is {first_num1/first_num2}")
    print(f"division of these floor is {first_num1//first_num2}")
    print(f"Remainder of two number is {first_num1%first_num2}")
    
    end = time.time()         # end excution time
    c = end-start         #total excution time

    print(f"total excution time is {c}")