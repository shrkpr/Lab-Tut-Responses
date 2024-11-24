import logging
import sys

# initialising variables
payment_norm = 0
payment_ot = 0
ot_hrs = 0
overtime_time_limit = 40.0

# user input
total_hrs = input('Key in the number of working hours: ')
input_rate = input('Key in the normal rate: ')
ot_rate = input('Key in the overtime rate: ')

# try and except to catch errors
try: 
    # convert user input to floats
    total_hrs = float(total_hrs)
    input_rate = float(input_rate)
    ot_rate = float(input_rate)
    
    # to check if user input is beyond 168 hrs (theoretical max hrs in a week), and is an instance of a float, if not proceed with the calculations
    if total_hrs > 100 or total_hrs < 0:
        # raises a value error if user input is beyond 168 hrs
        raise ValueError
    if input_rate < 0:
            raise ValueError
    elif not isinstance(total_hrs,float):
        # raises a value error if user input is not a float
        raise ValueError
    
    else:
        # employee's overtime hours
        ot_hrs = total_hrs - 40
        # to check if employee had any overtime
        if ot_hrs < 0:
            ot_hrs = 0
            payment_norm = total_hrs*input_rate
            payment_ot = 0
            print("Normal Salary:$%.2f, Extra Salary:$%.2f, Total Salary:$%.2f"%(payment_norm, payment_ot,payment_norm))
        # else proceed with calcuating the employee's rate with OT pay   
        else: 
            payment_ot = ot_hrs*input_rate
            payment_norm =  (total_hrs-overtime_time_limit)*input_rate
            total = payment_ot + payment_norm
            print("Normal Salary:$%.2f, Extra Salary:$%.2f, Total Salary:$%.2f"%(payment_norm,payment_ot,total))
# captures ValueError exception, logs the exception, and prints the input is invalid
except ValueError as e:
    logging.exception(e)
    print(e)
    print('Your input is invalid')


# Solution

import sys
# uses commmand prompt inputs
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    normal = 0.0
    normalh = 0.0
    extra = 0.0
    total = 0.0
    hours = 0.0
# calculations when there is no ot
    if a < 40:
        normal = a * b
        total = normal + extra
        print("Normal Salary:{0:.2f},".format(normal), "Extra Salary:{0:.2f},".format(extra), "Total Salary:{0:.2f}".format(total), end="")
#calculations when there is ot 
    elif 40 < a < 100:
        hours = a - 40
        normalh = a - hours
        normal = normalh * b
        extra = hours * c
        total = normal + extra
        print("Normal Salary:{0:.2f},".format(normal), "Extra Salary:{0:.2f},".format(extra), "Total Salary:{0:.2f}".format(total), end="")

    elif a > 100:
        print("Your input is invalid!")
# index error bc user may type in 4 or more arguments in the cmd prompt
except (IndexError, ValueError):
    print("Your input is invalid!")