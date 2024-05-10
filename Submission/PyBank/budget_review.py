import os
import csv

# Set path for file
csvpath = "PyBank/Resources/budget_data.csv"
output_file = "Pybank/budget_analysis.txt"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
total_change = 0
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Update total number of months
        total_months += 1
        
        # Extract month and profit/loss
        month = row[0]
        profit_loss = int(row[1])
        
        # Calculate net total amount of profit/loss
        net_total += profit_loss
        
        # Calculate change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change
            
            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = month
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = month
                greatest_decrease["amount"] = change
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = total_change / (total_months - 1)

# Write the analysis results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# Print confirmation message
print("Financial analysis results have been written to 'budget_analysis.txt' file.")