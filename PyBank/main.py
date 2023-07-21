
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

csvpath = os.path.join(SysPath, 'PyBank', 'Resources', 'budget_data.csv')
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
# +1 added at the end of each of these as the ChangeData list will cetagorically have a reduced index value compared to the comparison lists - Index 0 will not have a valid point to subtract against.
MaxChangeIndex = ChangeData.index(max(ChangeData))+1
MinChangeIndex = ChangeData.index(min(ChangeData))+1

# I found that it would make more sense to me to make a single string to be used as the output
financial_analysis = (
"Financial Analysis" + "\n" +
"----------------------------" + "\n" +
"Total Months: " + str(len(MonthData)) + "\n" +
"Total: $" + str(sum(ProfitsData)) + "\n" +
"Average Change: $" + str(round(sum(ChangeData) / (len(ChangeData)-1),2)) + "\n" +
"Greatest Increase in Profits: " + str(MonthData[MaxChangeIndex]) + " ($" + str(max(ChangeData)) + ")" + "\n" +
"Greatest Decrease in Profits: " + str(MonthData[MinChangeIndex]) + " ($" + str(min(ChangeData)) + ")" + "\n"
)

with open(os.path.join(SysPath,'PyBank','Analysis','financial_analysis.txt'),'w') as output_file:
    output_file.write(financial_analysis)

print(financial_analysis)