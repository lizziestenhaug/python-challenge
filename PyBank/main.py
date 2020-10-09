import os
import csv

# Load CSV File
budget_data = os.path.join('..', 'Python-Challenge','PyBank', 'Resources', 'budget_data.csv')

total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []

#Opening CSV files 
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip header row
    csv_header = next(csvreader)

    #Reading the first row 
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    
    
    for row in csvreader:
        dates.append(row[0])
        
        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months included in the dataset 
        total_months += 1

        #The net total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + int(row[1])


 #The average of the changes in "Profit/Losses" over the entire period
    avg_change = sum(profits)/len(profits)

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    

#Displaying information
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# output to text
with open('PyBank.txt', 'w') as text_file: 
    print("Financial Analysis", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Months: {str(total_months)}", file=text_file)
    print(f"Total: ${str(total_profit_loss)}", file=text_file)
    print(f"Average Change: ${str(round(avg_change,2))}", file=text_file)
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})", file=text_file)
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})", file=text_file)

