"""
Module 3 PyPoll Challenge
Author: Liaman Aghayeva
Date: 12/14/24
"""

# Importing CSV ans OS
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# Initializing variables
total_votes = 0

# Defining lists and dictionaries to track candidate names and vote counts
votes_per_candidate = {}
candidate_output = ""

# Winning Candidate and Winning Count Tracker
winning_count = 0

# Opening the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skiping the header row
    header = next(reader)

    # Looping through each row of the dataset and process it
    for row in reader:

        # Printing a loading indicator (for large datasets)
        print(". ", end="")

        # Incrementing the total vote count for each row
        total_votes += 1


        # Getting the candidate's name from the row
        candidate_name = row[2]

          # If the candidate is not already in the candidate list, add them

        if candidate_name not in votes_per_candidate:
          votes_per_candidate[candidate_name] = 0

          # Adding a vote to the candidate's count
        votes_per_candidate[candidate_name] += 1


    # Looping through the candidates to determine vote percentages and identify the winner
    # Getting the vote count and calculate the percentage
    # Updating the winning candidate if this one has more votes

for candidate, votes in votes_per_candidate.items():
  candidate_output += f"{candidate}: {round(votes / total_votes*100,3)}% ({votes})\n"
  if votes > winning_count:
    winning_count = votes
    winner = candidate

# Generating and printing Election Results summary
output = (
    "\n\nElection Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{candidate_output}\n"  # Example for showing the first candidate
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

print(output)

 # Saving the Election Results summary to a text file

with open(file_to_output, "w") as text_file:
  text_file.write(output)