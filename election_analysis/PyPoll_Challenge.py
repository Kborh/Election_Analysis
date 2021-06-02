# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_vote = 0
<<<<<<< HEAD
largest_county_turnout = ""
=======
largest_voter_turnout = ''
>>>>>>> c796ea3a97a249fbb54d46701a27035315cb8ee7

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_names:
            # 4b: Add the existing county to the list of counties.
            county_names.append(county_name)
        # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
<<<<<<< HEAD
    for county in county_votes:
=======
    for county in county_names:
>>>>>>> c796ea3a97a249fbb54d46701a27035315cb8ee7
        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]
        # f'{county}: {county_vote:,})\n'
        # 6c: Calculate the percentage of votes for the county.
<<<<<<< HEAD
        county_percentage = float(county_vote)/float(total_votes) * 100
=======
        county_percentage = int(county_vote)/int(total_votes) * 100
>>>>>>> c796ea3a97a249fbb54d46701a27035315cb8ee7

        # 6d: Print the county results to the terminal.
        county_result = (
            f'{county}: {county_percentage:.1f}% ({county_vote:,})\n'
        )
        print(county_result, end='')
        # 6e: Save the county votes to a text file.
<<<<<<< HEAD
        txt_file.write(county_result)

    # 6f: Write an if statement to determine the winning county and get its
    # vote count.
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f'------------------------\n'
        f'Largest County Turnout {largest_county_turnout}\n'
        f'------------------------\n')

    print(largest_county_turnout)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
=======
        txt_file.write(election_results)

    # 6f: Write an if statement to determine the winning county and get its
    # vote count.
    if (county_vote > winning_count):
        largest_county_vote = county_vote
        largest_voter_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    largest_voter_turnout = (
        f'------------------------\n'
        f'Largest County Turnout {largest_voter_turnout}\n'
        f'------------------------\n')

    print(largest_voter_turnout)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_voter_turnout)
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_options:
>>>>>>> c796ea3a97a249fbb54d46701a27035315cb8ee7

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
