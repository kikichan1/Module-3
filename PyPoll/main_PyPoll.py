# Modules
import os
import csv

# Set paths for files
csv_path = './Resources/election_data.csv'
output_file = './Analysis/election_result.txt'

# Initialize variables
total_votes = 0
candidate_vote_count = {}
highest_votes = 0
winner = None
candidate_vote_count_str = ""

# Read in the CSV file and split the data on commas
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header row to actual data rows
    header = next(csv_reader)

 # Loop through the data
    for row in csv_reader:

        # Calculate the total number of votes cast
        total_votes += 1

        # Find out the list of candidates with the respective vote count
        candidate = row[2]        

        if candidate in candidate_vote_count:
            candidate_vote_count[candidate] += 1
        else:
            candidate_vote_count[candidate] = 1

# Find out the winner with the highest vote count
for candidate in candidate_vote_count:
    votes = candidate_vote_count[candidate]
    percentage = (votes / total_votes) * 100
    candidate_vote_count_str += f"{candidate}: {percentage:.3f}% ({votes})\n"

    if votes > highest_votes:
        highest_votes = votes
        winner = candidate
      
# Compile the election results
election_results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{candidate_vote_count_str}"
    "-------------------------\n"
    f"Winner: {winner}\n"
)
                  
# Print the election results
print(election_results)

# Export results to a text file
with open(output_file, 'w') as file:
    file.write(election_results)