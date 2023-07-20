import csv

# I asked ChatGPT to assist with the syntax of importing data from a raw github link and got the below
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
Candidate_Dict = {}

# If a Dictionary key-value pair does not exist the following will assign one such value.  Dictionary keys are unique
for row in csv_reader:
    if row[2] in Candidate_Dict:
        Candidate_Dict[row[2]] = Candidate_Dict[row[2]] + 1
    else:
        Candidate_Dict[row[2]] = 1 
    Row_Count = Row_Count + 1
    
print("\n")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Row_Count}")
print("-------------------------")
for Candidate, Votes in Candidate_Dict.items():
  print(f"{Candidate}: {(Votes / Row_Count):.3%} ({Votes})")
Winning_Candidate = max(Candidate_Dict, key=Candidate_Dict.get)
print("-------------------------")
print(f"Winner: {Winning_Candidate}")
print("-------------------------")
print("\n")