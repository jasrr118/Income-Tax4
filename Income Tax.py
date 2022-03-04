# -*- coding: utf-8 -*-
"""
Income Tax Calculator
Jasmine Starr
Project 1
"""

gross_income = float(input("Enter Gross Income: "))
dependants = int(input("Enter the number of Dependants: "))

income_tax = (gross_income - 9990 - dependants*(3000)) * 0.20

print(f'The income tax is ${income_tax:.1f}')