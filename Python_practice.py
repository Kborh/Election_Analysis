
#counties = ['Arapahoe', 'Denver', 'jefferson']
# if 'El Paso' in counties:
#print('El Paso is in the list of counties.')
# else:
#print('El Paso is the list of counties. ')


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

# for county in counties_dict.keys():
# print(county)

# for voters in counties_dict.values():
# print(voters)

# for county in counties_dict:
# print(counties_dict.get(county))

for county, voters in counties_dict.items():
    #print(county, voters)

    # voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829},
    # {"county": "Denver", "registered_voters": 463353},
    # {"county": "Jefferson", "registered_voters": 432438}]

    # for county_dict in voting_data:
    # print(county_dict)

    # for county_dict in voting_data:
    # for value in county_dict.values():
    # print(value)

    #my_votes = int(input('How many votes did you get in the election?'))
    #total_votes = int(input('What is the total votes in the election?'))
    #percentage_votes = (my_votes / total_votes) * 100
    #print('I received' + str(percentage_votes) + '% of the total votes')

    #my_votes = int(input('How many votrd did you get in the election? '))
    #total_votes = int(input('What is the total votes in the election? '))
    #print(f'I received {my_votes / total_votes * 100}% of the total votes. ')


for county, voters in counties_dict.items():
   # print(county + ' county has ' + str(voters) + ' register voters. ')
    print(f'{county} county has {voters:,} registered voters. ')


# candidate_votes = int(
   # input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
    #f"You received {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    # f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)
