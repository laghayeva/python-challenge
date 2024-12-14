# -*- coding: UTF-8 -*-
"""
Module 3 PyBank Python Challenege
Author: Liaman Aghayeva
Date: 12/14/24
"""
#Importing CSV and OS
import csv
import os

#Defining the path
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

#Defining Variables
total_month = 0
total_net = 0
net_change_list = []
avg_change = 0
max_increase = ["", 0]
max_decrease = ["", 0]

#Reading in the CSV file
with open(file_to_load) as financial_data:
  reader = csv.reader(financial_data, delimiter= ",")

#Skipping the header
  header = next(reader)

#Defining the rirst row and initializing variables
  first_row = next(reader)
  previous_profit = int(first_row[1])
  total_month += 1
  total_net += int(first_row[1])

#Creating a FOR loop to iterate through rows and calculate outputs
  for row in reader:
    total_month += 1
    total_net += int(row[1])
    current_change = int(row[1]) - previous_profit
    net_change_list.append(current_change)
    previous_profit = int(row[1])
    avg_change = round(sum(net_change_list)/len(net_change_list),2)

    if current_change > max_increase[1]:
      max_increase[0] = row[0]
      max_increase[1] = current_change

    if current_change < max_decrease[1]:
      max_decrease[0] = row[0]
      max_decrease[1] = current_change


# Formatting output
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n"
)

# Printing outputs to the terminal
print(output)

# Exporting the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)