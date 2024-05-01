import csv

# Open the CSV file
with open("python-challenge-main/PyBank/Resources/budget_data.csv", "r") as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    
    # Initialize variables to store the total number of months and total profit/losses
    total_months = 0
    total_profit_losses = 0
    
    # Initialize variables to store the previous and current profit/losses
    previous_profit_losses = 0
    current_profit_losses = 0
    
    # Initialize variables to store the greatest increase and decrease in profits
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Increment the total number of months
        total_months += 1
        
        # Add the current profit/losses to the total
        current_profit_losses = int(row["Profit/Losses"])
        total_profit_losses += current_profit_losses
        
        # Calculate the change in profits/losses
        change = current_profit_losses - previous_profit_losses
        
        # Update the previous profit/losses
        previous_profit_losses = current_profit_losses
        
        # Update the greatest increase in profits
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = row["Date"]
            greatest_increase["amount"] = change
        
        # Update the greatest decrease in profits
        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = row["Date"]
            greatest_decrease["amount"] = change
    
    # Calculate the average change in profits/losses
    average_change = total_profit_losses / total_months
    
    # Print the results
    print(f'''
Financial Analytics:
      
--------------------------------------------------
      
Total months {total_months}

Total: ${total_profit_losses}

Average Change: ${average_change:.2f}

Greatest Increase in profits: {greatest_increase["date"]} ${greatest_increase["amount"]}

Greatest Decrease in profits: {greatest_decrease["date"]} ${greatest_decrease["amount"]}
''')

# Write the results to a text file
with open("python-challenge-main/PyBank/Analysis/analysispybank.txt", "w") as file:
    file.write(f'''Financial Analytics:
      
--------------------------------------------------
      
Total months {total_months}

Total: ${total_profit_losses}

Average Change: ${average_change:.2f}

Greatest Increase in profits: {greatest_increase["date"]} ${greatest_increase["amount"]}

Greatest Decrease in profits: {greatest_decrease["date"]} ${greatest_decrease["amount"]}''')