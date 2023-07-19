
import os
import csv

#csvpath = "/Users/junebug/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')
MonthData = []
ProfitsData = []
ChangeData = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        MonthData.append(row[0])
        ProfitsData.append(int(row[1]))
        ChangeData.append(0)
    
for i in range(1,len(ProfitsData)):
    ChangeData[i-1] = ProfitsData[i] - ProfitsData[i-1]
          
MaxChangeIndex = ChangeData.index(max(ChangeData))+1
MinChangeIndex = ChangeData.index(min(ChangeData))+1

print("\n")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(MonthData)}")
print(f"Total: ${sum(ProfitsData)}")
print(f"Average Change: ${round(sum(ChangeData) / (len(ChangeData)-1),2)}")
print(f"Greatest Increase in Profits: {MonthData[MaxChangeIndex]} (${max(ChangeData)})")
print(f"Greatest Decrease in Profits: {MonthData[MinChangeIndex]} (${min(ChangeData)})")
print("\n")
