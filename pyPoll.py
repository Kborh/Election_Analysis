import csv
import os
# Assign a vsriable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# open the election result and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    # print(election_data)
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    # print(headers)

# Print each row in the CSV file
    for row in file_reader:
        # print(row)
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Save the result to our text file.
with open(file_to_save, 'w') as txt_file:

    # print the total vote count to the terminal.
    election_results = (
        f'\nElection Result\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n\n'
        f'County Votes:\n')
    print(election_results, end='')
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through
    # 1. Interate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrive vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentqge of
        # vote to the # terminal
        candidate_results = (
            f'{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n')
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # print the winning candidate to terminal
            winning_candidate_summery = (
                f'---------------------------\n'
                f'Winner: {winning_candidate}\n'
                f'Winning Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:.1f}%\n'
                f'---------------------------\n')
            print(winning_candidate_summery)

    # if true then set winning_count = votes and winning_percent =
    # vote_percentage.
    winning_couunt = votes
    winning_percentage = vote_percentage
    # And, set the winning_candidate equal to the candidate's name
    winning_candidate = candidate_name
    # 4. Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage} % of the vote.")

    # Print the candidate vote directionary.
    # print(candidate_votes)

    # Print the total votes
    # print(total_votes)
    # for row in file_reader:
    # print('test')
    # Close the file.
    # election_data.close()
    # Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:
        # Write some data to the file.
        txt_file.write("Arapahoe, Denver, Jefferson")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

    # Close the file
    # outfile.close()
