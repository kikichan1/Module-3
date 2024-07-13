# Modules
import os
import csv

# Set paths for files
csv_path = './Resources/budget_data.csv'
output_file = './Analysis/financial_analysis.txt'

# Initialize variables
total_months = 0
total = 0
changes = []
previous_value = None
total_change = 0
max_change = -float('inf')
max_change_month = None
min_change = +float('inf')
min_change_month = None

# Read in the CSV file and split the data on commas
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header row to actual data rows
    header = next(csv_reader)

    # Loop through the data
    for row in csv_reader:

        # Calculate the total months
        total_months += 1

        # Calculate the total
        total += int(row[1])
        current_value = int(row[1])

        # Calculate the changes in profits
        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)
            total_change += change
            
            # Calculate the greatest increase in profits
            if change > max_change:
                max_change = change
                max_change_month = str(row[0])

            # Calculate the greatest decrease in profits
            if change < min_change:
                min_change = change
                min_change_month = str(row[0])

        previous_value = current_value

    # Calculate the average changes in profits    
    if total_months > 1:
        average_change = total_change / (total_months - 1)
    else:
        average_change = 0
    formatted_average = f"{average_change:.2f}"      
    
    # Compile the financial analysis
    financial_analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total}\n"
        f"Average Change: ${formatted_average}\n"
        f"Greatest Increase in Profits: {max_change_month} (${max_change})\n"
        f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n"
    )
    
    # Print the financial analysis
    print(financial_analysis)

    # Export results to a text file
    with open(output_file, 'w') as file:
        file.write(financial_analysis)