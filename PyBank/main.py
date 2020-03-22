#import required modules
import os
import csv

#define variable to store location of csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#define necessary variables and lists
dates = []
total = []
profit_loss = []
avg_change = []

sum_total = 0
previous_month = 0

#open and read csv file
with open(csvpath, 'r') as csv_file:
    
    csvreader = csv.reader(csv_file, delimiter=',')

#define variable to store csv header
    csv_header = next(csvreader)

#loop through csv file and append the date column to list    
    for row in csvreader:
        dates.append(row[0])

#define variable to store the number of months based on the lenght of the list
        number_of_months = len(dates)

#append profit/loss values to list and calculate the total using the sum function
        total.append(int(row[1]))
        sum_total = sum(total)

#loop through list, calculate the month to month changes in profits and losses, and append those to lists
        next_month = int(row[1])
        monthly_change = next_month - previous_month
        previous_month = next_month
        profit_loss.append(monthly_change)
        avg_change.append(monthly_change)

#use pop function to remove the first value in the list in order to accurately calculate the average change in profits/losses
avg_change.pop(0)
average_change = sum(avg_change) / len(avg_change)

#use max and min functions to identify the greatest gain and loss
greatest_gain = max(profit_loss)
greatest_loss = min(profit_loss)

#use index function to identify the dates related to the greatest gain and greatest loss
greatest_gain_month = dates[profit_loss.index(greatest_gain)]
greatest_loss_month = dates[profit_loss.index(greatest_loss)]

#print results to terminal
print("---------------------------------------------------")
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${sum_total}")
#add .2f to round the value to 2 decimal places
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_gain_month} (${greatest_gain})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})")
print("---------------------------------------------------")

#define variable to store the location of the text output file
output_path = os.path.join("financial_analysis.txt")

#open and write results to text file
with open(output_path, 'w') as text:
    text.write("---------------------------------------------------\n")
    text.write("Financial Analysis\n")
    text.write("---------------------------------------------------\n")
    text.write(f"Total Months: {number_of_months}\n")
    text.write(f"Total: ${sum_total}\n")
#add .2f to round the value to 2 decimal places
    text.write(f"Average Change: ${average_change: .2f}\n")
    text.write(f"Greatest Increase in Profits: {greatest_gain_month} (${greatest_gain})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})\n")
    text.write("---------------------------------------------------")