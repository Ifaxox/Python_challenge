# Python script that analyzes the records to calculate each of the following values:
# -->>1 The total number of months included in the dataset
# -->>2 The net total amount of "Profit/Losses" over the entire period
# -->>3 The changes in "Profit/Losses" over the entire period, and then the average of those changes
# -->>4 The greatest increase in profits (date and amount) over the entire period
# -->>5 The greatest decrease in profits (date and amount) over the entire period


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# create variables
total_months = 1
profit_loss_list = []
net_profit_loss = 0
prev_month_profit_loss = 0
profit_loss_change = 0
# open and read csv
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # skipping the first row
    first_row = next(csvreader)
    # print(f"Header: {csv_header}")
    # this prints -->> Header: Date, Profit/Losses)
    # get the first profit/loss
    prev_month_profit_loss = int(first_row[1])
    net_profit_loss = int(first_row[1])
    # Read each row of data after the header
    for row in csvreader:
        # what this means is total_months = total_months + 1
        total_months += 1
        # 2 what this means is Net total amount of "profit/losses" over the entire period
        profit_loss = int(row[1])
        profit_loss_change = profit_loss - prev_month_profit_loss
        profit_loss_list.append(profit_loss_change)
        net_profit_loss += profit_loss
        prev_month_profit_loss = profit_loss
        # print(row)
    # 3 The sum of "Profit/Losses" over the entire period, and then the average of those changes
    sum_profit_loss = sum(profit_loss_list)
    average_profit_loss = round(sum_profit_loss / (total_months - 1), 2)
    # Find the greatest increase and decrease in profits
    greatest_increase = max(profit_loss_list)
    greatest_decrease = min(profit_loss_list)
    # Find the corresponding dates for the greatest increase and decrease
    greatest_increase_date = csv_header[0]
    greatest_decrease_date = csv_header[0]
    # Get the index of the greatest increase and decrease in the profit/loss list
    greatest_increase_index = profit_loss_list.index(greatest_increase)
    greatest_decrease_index = profit_loss_list.index(greatest_decrease)
    # Get the corresponding dates for the greatest increase and decrease
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header
        for i, row in enumerate(csvreader):
            if i == greatest_increase_index:
                greatest_increase_date = row[0]
            if i == greatest_decrease_index:
                greatest_decrease_date = row[0]
# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

 
# Export the results to a text file
output_file = "financial_analysis.txt"

with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_profit_loss}\n")
    txt_file.write(f"Average Change: ${average_profit_loss}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
print("Financial Analysis exported to financial_analysis.txt")
    