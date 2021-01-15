import csv
import os
# Assign a vsriable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the election result and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    # print(election_data)
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print each row in the CSV file
    for row in file_reader:
        print(row)

# Print the header row
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
    # print('test')
# Close the file.
# election_data.close()
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
# outfile.close()
