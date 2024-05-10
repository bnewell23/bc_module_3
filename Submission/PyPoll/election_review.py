import os
import csv

# Set path for file
csvpath = "PyPoll/Resources/election_data.csv"
output_file = "election_results.txt"

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": None, "votes": 0}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Iterate over each row
    for row in csvreader:
        # Update total number of votes
        total_votes += 1
        
        # Extract candidate name
        candidate_name = row[2]
        
        # Update candidate's total votes
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
        
        # Check if candidate has more votes than current winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Write the analysis results to a text file
# Xpert assisted with creating txt file with below results

with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner['name']}\n")
    txtfile.write("-------------------------\n")

# Print confirmation message
print("Analysis results have been written to 'election_results.txt' file.")