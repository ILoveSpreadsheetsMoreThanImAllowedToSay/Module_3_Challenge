import os
import csv

import platform
SysPath = ""
if platform.system() == "Darwin":
    #"Darwin" for the MacOS kernel
    #"Windows" for the Windows kernel
    #"Linus" for the Linux kernel
    SysPath = "."
else:
    ".."

# I asked ChatGPT to assist with the syntax of importing data from a raw github link and got the below
# I did this because I started working on another computer that was not my personal one with my cloned directory.  I also didn't have the option of storing things locally on that device, so alternatives were necessary which continue to work . . . so this implementation will remain.
# To demonstrate that I learned rather than simply copy/paste/replaced I will explain my understanding of each of the lines

# The urllib module is apparently a standard Python module for interfacing with URLs.  The 'request' component is for reading and opening the contents of those URLs
from urllib import request

# Plenty of Youtube tutorials out there for showing how to get the raw cvs link.  This one I found: https://www.youtube.com/watch?v=oPUmZu545TI
github_csv_url = "https://raw.githubusercontent.com/ILoveSpreadsheetsMoreThanImAllowedToSay/python-challenge/main/PyPoll/Resources/election_data.csv"

# The urlopen function does what might be expected, it opens the file specified in the url for use.
# The following read().decode(utf-8).splitlines helps decode the file as stored into a usable format; in this case - a list of lines, maintaining the CSV structure
response = request.urlopen(github_csv_url)
csv_data = response.read().decode('utf-8').splitlines()

# And now that the import of the flip-dipping thing is no longer frustrating and is playing nicely in a format that no longer threatens harm to my monitor by way of my fist, we can proceed with interacting with the csv in ways intended by the course thus far
csv_reader = csv.reader(csv_data)
csv_header = next(csv_reader)

Row_Count = 0

# I was determined to learn how to use dictionaries this time around rather than do some ballistic stuff with multiple list objects
Candidate_Dict = {}

# Loop over all rows in the csv, create and assign key-value pairs into a dictionary, also count the size of the csv as each line counts as a single vote
for row in csv_reader:
    if row[2] in Candidate_Dict:
        Candidate_Dict[row[2]] = Candidate_Dict[row[2]] + 1
    else:
        Candidate_Dict[row[2]] = 1 
    Row_Count = Row_Count + 1
    
# Similar approach to output as with PyBank, that is - use a single string to write to the file
election_results = (
"Election Results" + "\n" +
"-------------------------" + "\n" +
"Total Votes: " + str(Row_Count) + "\n" +
"-------------------------" + "\n")

for Candidate, Votes in Candidate_Dict.items():
  proportion = Votes / Row_Count
  election_results += Candidate + ": " + "{:.3%}".format(proportion) + " (" + str(Votes) + ")" + "\n"

Winning_Candidate = max(Candidate_Dict, key=Candidate_Dict.get)
election_results += (
"-------------------------" + "\n" +
"Winner: " + str(Winning_Candidate) + "\n" +
"-------------------------")

# Working on my personal device again when I wrote this Write section, should work for others when downloading locally.
with open(os.path.join(SysPath,'PyPoll','Analysis','election_results.txt'),'w') as output_file:
    output_file.write(election_results)

print(election_results)