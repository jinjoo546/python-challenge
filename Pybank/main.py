import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

totalmonths = 0
totalprofit = 0
difference = 0
accumulatedchange = 0
loss = 0
increase = 0
decrease = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        totalmonths = totalmonths + 1
        totalprofit = totalprofit + int(row[1])
        
        if totalmonths > 1:
                difference = int(row[1]) - loss
       
        accumulatedchange= accumulatedchange + difference
        loss = int(row[1])

        if difference < decrease:
            decrease = difference
            decreasemonth = row[0]
        
        if difference > increase:
            increase = difference
            increasemonth = row[0]

print(totalmonths)
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print("Average Change: $" + str(round(accumulatedchange / (totalmonths-1),2)))
print(f"Greatest Increase in Profits: {increasemonth} (${increase})")
print(f"Greatest Decrease in Profits: {decreasemonth} (${decrease})")

file = open("textfile.txt", "w")
file.write("Financial Analysis"'\n')
file.write("------------------------"'\n')
file.write(f"Total Months: {totalmonths}"'\n')
file.write(f"Total: ${totalprofit}"'\n')
file.write("Average Change: $" + str(round(accumulatedchange / (totalmonths-1),2)))
file.write('\n'f"Greatest Increase in Profits: {increasemonth} (${increase})"'\n')
file.write(f"Greatest Decrease in Profits: {decreasemonth} (${decrease})"'\n')
file.close