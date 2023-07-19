
import os
import csv

# Information about platform.system() to identify OS running on to adjust filepath courtesy of Stack Overflow:
# https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on
import platform
SysPath = ""
if platform.system() == "Darwin":
    #"Darwin" for the MacOS kernel
    #"Windows" for the Windows kernel
    #"Linus" for the Linux kernel
    SysPath = "."
else:
    ".."
# This was such a pain in the patootie to get my system to run until I realized that the example code for os.path-containing activities would not work without modification.
# This bit was included to minimize disruption for the non-MacOS users (everyone but me, I guess)
# I lovehate computers.

csvpath = os.path.join(SysPath, 'PyBank','Resources', 'budget_data.csv')
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
