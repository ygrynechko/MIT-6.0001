# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:04:10 2020

@author: Gugu
"""

#user input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
#provided variables
current_savings = 0
portion_down_payment = 0.25
annual_return = 0.04
#calculated variables
down_payment = total_cost * portion_down_payment
number_of_months = 0
#note: monthly savings = (annual_salary/12)* portion_saved 
#loop calculating months
while current_savings < down_payment:
    if number_of_months % 6 == 0 and number_of_months!=0:
        annual_salary = annual_salary + annual_salary * semi_annual_raise
    number_of_months+=1
    current_savings = current_savings + (current_savings*annual_return/12) + ((annual_salary/12)* portion_saved) 
print("Number of months to save:",number_of_months)


