import os 
import csv


bank_data = []

def financial_analysis(datums):
    print("Financial Analysis")
    print("------------------------------------------------------------")

    print(f"Total Months: {len(datums)} ")

    total_profits = 0
    average_change = 0
    sum_of_changes = 0
    greatest_increase = 0
    greatest_decrease = 0
    decrease_month = ""
    increase_month = ""

    lookback = 0
    difference = 0 

    for i in range(len(datums)):
        
        total_profits += int(datums[i][1])
        #if we evaluate this on i = 0 then it breaks bc 8k - 0 = 8k, but that is not the difference.
        if i != 0: 
            difference =  int(datums[i][1]) - lookback
            sum_of_changes = sum_of_changes + difference
        print(sum_of_changes)

        if greatest_decrease > difference:
            greatest_decrease = difference
            decrease_month = datums[i][0]
        if greatest_increase < difference:
            greatest_increase = difference
            increase_month = datums[i][0]

        
        lookback = int(datums[i][1])
        


    print(f"Total: {total_profits}")
    
    avg_change = sum_of_changes / (len(datums) - 1)
    print(f"Average Change: {round(avg_change,2)}")

    print(f"Greatest Increase in Profits: {increase_month} : {greatest_increase}")
    print(f"Greatest Decrease in Profits: {decrease_month} : {greatest_increase}")






    

    
os_path = os.path.join('resources', 'budget_data.csv')

# Read in the CSV file
with open(os_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:

        bank_data.append(row)

    bank_data.pop(0)

financial_analysis(bank_data)
