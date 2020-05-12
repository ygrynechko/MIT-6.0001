# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:29:33 2020

@author: Gugu
"""

#user input
starting_salary = int(input("Enter your starting salary: "))

#provided variables
semi_annual_raise = 0.07
current_savings = 0
cost_of_house = 1000000
portion_down_payment = 0.25
annual_return = 0.04
#calculated variables
down_payment = cost_of_house * portion_down_payment
monthly_salary = starting_salary/12
overall_salary = 0
#calculate avg monthly salary over 36 months
for i in range(1,37):
    if i%7==0:   
        monthly_salary= monthly_salary*semi_annual_raise + monthly_salary
    overall_salary = overall_salary + monthly_salary
    print(monthly_salary, overall_salary, i)
    i +=1

monthly_salary = round(overall_salary/36,2)


#variables needed for last loop
num_guesses = 0
epsilon = 100
low = 0
high = 1
guess = (low + high)/2.0
#loop

if overall_salary < down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs((((monthly_salary)* guess)*36) - down_payment) >= epsilon: 
    
        if (((monthly_salary)* guess)*36) < down_payment:
            low = guess
        else: 
            high = guess
        guess = round((high + low)/ 2.0,4)
        num_guesses +=1
    
    print('num_guesses= ',num_guesses,"guess:", guess)

