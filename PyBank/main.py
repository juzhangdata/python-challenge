"""
This script analyzes the financial records of the company.
This script works with both .csv datasets provided.
This script prints a financial analysis, including "Total Months, Total Revenue, Average Revenue Change: $216825
Greatest Increase in Revenue(month), and Greatest Decrease in Revenue(month)".
"""

#import modules:
import os
import csv

#assign the file path:
csvpath = os.path.join('.','raw_data','budget_data_1.csv')

#use 'with open' to open file and store in a reader:
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    print(reader)

    #skip the header:
    next(reader)

    #create a lists of values:
    months = []
    revenue = []
    revenue_change = []

    #initiate variables:
    row_num = 0
    previous_revenue = 0
    total_revenue = 0

    #loop through rows:
    for row in reader:

        #append lists with values in each row
        months.append(row[0])
        revenue.append(row[1])
        total_revenue = total_revenue + int(row[1])

        #assign value to the current row number
        row_num = row_num + 1
        
        #calculate the revenue change values(compared with the previous row) for every row except the first:
        if row_num == 1:
            revenue_change_current = 'None'
            revenue_change.append(revenue_change_current)
        
        else:
            current_revenue = row[1]
            revenue_change_current = int(current_revenue) - int(previous_revenue)
            revenue_change.append(revenue_change_current)

        #save the current revenue as the revenue of 'previous row' so the next row can compare with it:
        previous_revenue = row[1]

    #calculate totals:
    total_data_rows = len(months)
    total_months = len(months)

    #calculate the sum of revenue change, and average revenue change:
    revenue_change_sum = int(revenue[total_data_rows-1]) - int(revenue[0])
    average_revenue_change = int(revenue_change_sum / total_months)

    #Calculate the greatest increase and decrease in revenue, and their corresponding months:
    greatest_increase_in_revenue = max(revenue_change[1:])
    greatest_increase_in_revenue_index = revenue_change.index(greatest_increase_in_revenue)
    greatest_increase_in_revenue_month = months[greatest_increase_in_revenue_index]
    greatest_decrease_in_revenue = min(revenue_change[1:])
    greatest_decrease_in_revenue_index = revenue_change.index(greatest_decrease_in_revenue)
    greatest_decrease_in_revenue_month = months[greatest_decrease_in_revenue_index]  

    #save financial analysis as a string
    report_string = "```\n" + "Financial Analysis\n" + "----------------------------\n"\
    + "Total Months: " + str(total_months) + "\n"\
    + "Total Revenue: $"  + str(total_revenue) + "\n"\
    + "Average Revenue Change: $"  + str(average_revenue_change) + "\n"\
    + "Greatest Increase in Revenue: "  + greatest_increase_in_revenue_month + " ("\
    + "$" + str(greatest_increase_in_revenue) + ")" + "\n"\
    + "Greatest Decrease in Revenue: "  + greatest_decrease_in_revenue_month + " ("\
    + "$" + str(greatest_decrease_in_revenue) + ")" + "\n"\
    + "```"

    #print financial analysis:
    print(report_string) 

    #save financial analysis to txt
    output_file = os.path.join("output.txt")
    with open(output_file, "w") as f:
        f.write(report_string)