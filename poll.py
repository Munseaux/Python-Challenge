import os
import csv
import sys


def count_votes(datums):
    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {len(datums)}")
    print("------------------------------------")
    candidates = {}
    name = ""
    votes = []
    total = 0
    winner = ""
    winning_number = 0

    #This finds all unique candidate names in the dataset
    for i in range(len(datums)):
        if(name != datums[i][2]):
            name = datums[i][2]
            candidates[name] = 0
        votes.append(name)

    #This counts up the total votes, and also populates the dictionary for candidate vote totals. 
    for person in candidates:
        candidates[person] = votes.count(person)
        total = total + votes.count(person)
    
    #now that we have all the right values in the right places we can print everything. 
    for person in candidates:
        
        print(f"{person}: {round((candidates[person] /total) * 100, 4)}% {candidates[person]}")
        
        #find the winner
        if int(candidates[person]) > winning_number:
            winner = person
            winning_number = candidates[person]

    print("------------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------------")

    #print to file
    write_path = os.path.join("solutions_output", "poll_solution.txt")

    with open(write_path, 'w') as f:
        sys.stdout = f

        print("Election Results")
        print("------------------------------------")
        print(f"Total Votes: {len(datums)}")
        print("------------------------------------")
        
        for person in candidates:
            print(f"{person}: {round((candidates[person] /total) * 100, 4)}% {candidates[person]}")

        print("------------------------------------")
        print(f"Winner: {winner}")  
        print("------------------------------------")

    return 0


read_path = os.path.join('resources', 'election_data.csv')

election_data = []

# Read in the CSV file
with open(read_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:

        election_data.append(row)

    election_data.pop(0)

#call function to do all the work for me

count_votes(election_data)

