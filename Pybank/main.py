import csv,os

# File path to budget data
#budget_filepath = os.path.join("Resources","budget_data.csv")
budget_filepath = "Resources/budget_data.csv"
# Variables to track
total_number_of_months = 0
net_total = 0
#total_profit_change = 0
previous_total = 0
deltas = 0
test = list()
running_total = 0
avg_per_month = 0
high_swing = 0
low_swing = 0
high_month = ""
low_month = ""

# Code to read file
with open(budget_filepath) as dataset:
    reader = csv.reader(dataset)
    header = next(reader)
    for row in reader:
        total_number_of_months += 1
        test.append((row[0],int(row[1]))) 
        net_total += int(row[1])
       
       
       # previous_total = 0 if total_number_of_months == 1 else ( total_number_of_months -1)
    for i in range(len(test)-1):  

     #total_profit_change += abs(int(row[1]) - previous_total)
        change = test[i+1][1] - test[i][1]
        #high_swing = max(high_swing,change)
        #low_swing = min(low_swing, change)
        deltas += change
        if high_swing < change:
            high_swing = change
            high_month = test[i+1][0]
           # continue
       # else:
           # change > high_swing
           # high_swing = change

        if low_swing > change:
            low_swing = change
            low_month = test[i+1][0]
            

    #for row in range(len(net_total)-1):
        previous_total = int(row[1])
output = open("analysis/PyBankText.txt","w")
output.write("Financial Analysis\n") 
output.write("------------------\n")
output.write("Total Months {}\n".format(total_number_of_months))
output.write("Total: {}\n".format(net_total))
output.write("Average Change {}\n".format(deltas/(len(test)-1)))
output.write("Greatest Increase In Profits: {} ({})\n".format(high_month, high_swing))
output.write("Greatest Decrease In Profits: {} ({})\n".format(low_month, low_swing))
output.close()
