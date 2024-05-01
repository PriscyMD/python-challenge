import csv

# Create a list to store the data
data = []

# Open the CSV file and read the data
with open("PyPoll/Resources/election_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        data.append(row)

# Calculate the total number of votes
total_votes = len(data)

# Calculate the number of votes for each candidate
cand1 = sum(1 for row in data if row[2] == "Charles Casper Stockham")
cand2 = sum(1 for row in data if row[2] == "Diana DeGette")
cand3 = sum(1 for row in data if row[2] == "Raymon Anthony Doane")

# Calculate the percentage of votes for each candidate
pc_cand1 = cand1 / total_votes * 100
pc_cand2 = cand2 / total_votes * 100
pc_cand3 = cand3 / total_votes * 100

# Determine the winner
winner = max(cand1, cand2, cand3)
if winner == cand1:
    winner_name = "Charles Casper Stockham"
elif winner == cand2:
    winner_name = "Diana DeGette"
else:
    winner_name = "Raymon Anthony Doane"

# Print the results
print(f'''
Election Results:
      
--------------------------------------------------
      
Total votes: {total_votes}

--------------------------------------------------

Charles Casper Stockham: {pc_cand1:.2f}% ({cand1})

Diana DeGette: {pc_cand2:.2f}% ({cand2})

Raymon Anthony Doane: {pc_cand3:.2f}% ({cand3})

--------------------------------------------------

Winner: {winner_name}

--------------------------------------------------
''')

# Write the results to a file
with open("PyPoll/Analysis/analysispypoll.txt", "w") as file:
    file.write(f'''
Election Results:
      
--------------------------------------------------
      
Total votes: {total_votes}

--------------------------------------------------

Charles Casper Stockham: {pc_cand1:.2f}% ({cand1})

Diana DeGette: {pc_cand2:.2f}% ({cand2})

Raymon Anthony Doane: {pc_cand3:.2f}% ({cand3})

--------------------------------------------------

Winner: {winner_name}

--------------------------------------------------
''')