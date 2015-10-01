# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:09:33 2015

@author: tjfamodu
"""

#### Homework 2 ####

# BASIC LEVEL PART 1: Read in the data with csv.reader() and store it in a 
# list of lists called 'data'. Hint: This is a TSV file, and csv.reader() needs
# to be told how to handle it. https://docs.python.org/2/library/csv.html

chipotle = "/Users/tjfamodu/GA_Data_Science/Dat-9-repo/DAT-DC-9/data/chipotle.tsv"

import csv
with open(chipotle) as tsv:
    data = [row for row in csv.reader(tsv,delimiter="\t")]
    print(data)
    

# BASIC LEVEL PART 2: Separate the header and data into two different lists.

with open(chipotle) as tsv:
    data = [row for row in csv.reader(tsv,delimiter="\t")]
    header = data[0]
    data = data[1:]


# INTERMEDIATE LEVEL PART 3: Calculate the average price of an order. 
# Hint: Examine the data to see if the 'quantity' column is relevant to this 
# calculation. Hint: Think carefully about the simplest way to do this!


with open(chipotle) as tsv:
    data = [row for row in csv.reader(tsv,delimiter="\t")]
    header = data[0]
    data = data[1:]
    prices = [float(row[4][1:-1]) for row in data]
    print(prices)
    average = round(sum(prices)/ 1834,0)
    print(average)
## The quantity column does not matter for calculation


#INTERMEDIATE LEVEL PART 4: Create a list (or set) of all unique sodas and 
# soft drinks that they sell. Note: Just look for 'Canned Soda' and 'Canned 
# Soft Drink', and ignore other drinks like 'Izze’.

unique_sodas = []
with open(chipotle) as tsv:
    for row in csv.reader(tsv,delimiter="\t"):
        if 'Canned' in row[2]:
            unique_sodas.append(row[3][1:-1])
unique_sodas = set(unique_sodas)
print(unique_sodas)
  
    
# ADVANCED LEVEL PART 5: Calculate the average number of toppings per burrito.
# Note: Let's ignore the 'quantity' column to simplify this task. Hint: 
# Think carefully about the easiest way to count the number of toppings!
    
toppings = []
with open(chipotle) as tsv:
    for row in csv.reader(tsv,delimiter="\t"):
        if 'Burrito' in row[2]:
            toppings.append(row[3]).count(',')
print(toppings)
        
        

# ADVANCED LEVEL PART 6: Create a dictionary in which the keys represent chip 
# orders and the values represent the total number of orders. Expected output: 
# {'Chips and Roasted Chili-Corn Salsa': 18, ... } Note: Please take the 
# 'quantity' column into account! Optional: Learn how to use 'defaultdict' 
# to simplify your code.
from collections import defaultdict
with open(chipotle) as tsv:
#    for row in csv.reader(tsv,delimiter="\t"):
    chips = defaultdict(int)
    for row in data:
        if 'Chips' in row[2]:
            chips[row[2]] += int(row[1])
print(chips)

