# Create a Python script that analyzes the votes and calculates each of the following values:
# -->>1 The total number of votes cast
# -->>2 A complete list of candidates who received votes
# -->>3 The percentage of votes each candidate won
# -->>4 The total number of votes each candidate won
# -->>5 The winner of the election based on popular vote



# Import dependencies
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
# Create variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0
# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row
    # Iterate through each row in the CSV
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        # Get the candidate name from the current row
        candidate_name = row[2]
        # Add the candidate to the candidate_votes dictionary if not already present
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        # Increment the candidate's vote count by 1
        candidate_votes[candidate_name] += 1
# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Calculate and print the results for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Check if the current candidate has the most votes
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file

# Print the analysis results
output_file = "election_results.txt"

with open(output_file, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------------\n")
    # Calculate and write the results for each candidate
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        # Check if the current candidate has the most votes
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write(f"-------------------------\n")
print("Election results exported to election_results.txt")

