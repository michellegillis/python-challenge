import os
import csv
polldata = os.path.join("Resources", "election_data.csv")

candidates = []
candidate_votes = {}

with open(polldata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    totalvotes = 0
    for row in csvreader:
        totalvotes += 1
        candidatename = row[2]
        if candidatename not in candidates:
            candidates.append(candidatename)
            candidate_votes[candidatename] = 0
        candidate_votes[candidatename] += 1
    print("Total Votes: " + str(totalvotes))
    print(candidate_votes)

write_file = open(os.path.join("analysis", "pypolloutput.txt"), 'w+')
write_file.write("Election Results\n")   
   