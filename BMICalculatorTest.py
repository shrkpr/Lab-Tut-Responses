import logging
#initialising user input and setting user input to lower case
unit_choice = input('Key in your prefered unit of choice, Metric or Imperial: ')
unit_choice = unit_choice.lower()
#initialising var bmi
bmi = 0

#try and except block
try: 
    # matches str to 'metric' or 'imperial'
    if unit_choice == 'metric':
        #changes var type to float 
        height = float(input('Key in your height in meters: '))
        weight = float(input('Key in your weight in kilograms: '))
        #if height < 0 raise ValueError as height is squared in the formula so it'll return a +ve bmi value
        if height < 0:
            raise ValueError
        #bmi formula
        bmi = weight / height**2
        #format each critera of bmi with \t
        if 0 < bmi and bmi < 16:
            print("%.2f\t Severe Thinness"%bmi)
            
        elif 16 <= bmi and bmi < 17:
            print("%.2f\t Moderate Thinness"%bmi)
        
        elif 17 <= bmi and bmi < 18.5:
            print("%.2f\t Mild Thinness"%bmi)
            
        elif 18.5 <= bmi and bmi < 25:
            print("%.2f\t Normal"%bmi)
            
        elif 25 <= bmi and bmi < 30:
            print("%.2f\t Overweight"%bmi)
        
        elif 30 <= bmi and bmi < 35:
            print("%.2f\t Obese Class I"%bmi)
        
        elif 35 <= bmi and bmi < 40:
            print("%.2f\t Obese Class II"%bmi)
        
        elif bmi > 40:
            print("%.2f\t Obese Class III"%bmi) 
        # raises ValueError if -ve weight is keyed
        else:
            raise ValueError

    # when user selects imperial units
    elif unit_choice == 'imperial':
        #changes var type to float 
        height = float(input('Key in your height in inches: '))
        weight = float(input('Key in your weight in pounds: '))
         #if height < 0 raise ValueError as height is squared in the formula so it'll return a +ve bmi value
        if height < 0:
            raise ValueError
        #format each critera of bmi with \t
        bmi = 703*weight / height**2
        
        if 0 < bmi and bmi < 16:
            print("%.2f\t Severe Thinness"%bmi)
            
        elif 16 <= bmi and bmi < 17:
            print("%.2f\t Moderate Thinness"%bmi)
        
        elif 17 <= bmi and bmi < 18.5:
            print("%.2f\t Mild Thinness"%bmi)
            
        elif 18.5 <= bmi and bmi < 25:
            print("%.2f\t Normal"%bmi)
            
        elif 25 <= bmi and bmi < 30:
            print("%.2f\t Overweight"%bmi)
        
        elif 30 <= bmi and bmi < 35:
            print("%.2f\t Obese Class I"%bmi)
        
        elif 35 <= bmi and bmi < 40:
            print("%.2f\t Obese Class II"%bmi)
        
        elif bmi > 40:
            print("%.2f\t Obese Class III"%bmi) 
        # raises ValueError if -ve weight is keyed
        else:
            raise ValueError
        
    else:
        raise ValueError
    #prints error message whenever ValueError is raised
except ValueError:
    print('Key in a valid input!')
    
    
# solution 
import sys

try:
    a = str(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    bmi = 0.0

    if a == "metric":
        bmi = c / b**2
        print("{0:.2f}".format(bmi), end=" ")
        if bmi < 16:
            print("\tSevere Thinness")
        elif bmi == 16 and bmi == 17:
            print("\tModerate Thinness")
        elif 17 <= bmi <= 18:
            print("\tMild Thinness")
        elif 18.5 <= bmi <= 25:
            print("\tNormal")
        elif 25 <= bmi <= 30:
            print("\tOverweight")
        elif 30 <= bmi <= 35:
            print("\tObese Class I")
        elif 35 <= bmi <= 40:
            print("\tObese Class II")
        elif bmi > 40:
            print("\tObese Class III")
    elif a == "imperial":
        bmi = (703*c) / b**2
        print("{0:.2f}".format(bmi), end=" ")
        if bmi < 16:
            print("\tSevere Thinness")
        elif bmi == 16 and bmi == 17:
            print("\tModerate Thinness")
        elif 17 <= bmi <= 18:
            print("\tMild Thinness")
        elif 18.5 <= bmi <= 25:
            print("\tNormal")
        elif 25 <= bmi <= 30:
            print("\tOverweight")
        elif 30 <= bmi <= 35:
            print("\tObese Class I")
        elif 35 <= bmi <= 40:
            print("\tObese Class II")
        elif bmi > 40:
            print("\tObese Class III")

except (IndexError, ValueError):
    print("Your input is invalid!")
