import csv

votescast = 0
candidate_list = []
votes_per_candidate = []
percentagevotes_per_candidate = []
winner = ""
candidate_info = {}

election_data_csv = "PyPoll/Resources/election_data.csv"

with open(election_data_csv, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    for row in csvreader:
        votescast += 1
        votes_per_candidate.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    for i in range(len(candidate_list)):
        count = 0
        for j in range(len(votes_per_candidate)):
            if candidate_list[i] == votes_per_candidate[j]:
                count +=1
        candidate_info[candidate_list[i]] = count
    
    for x in range(len(candidate_list)):
        candidate_info[percentagevotes_per_candidate[x]]=(candidate_info[candidate_list[x]]/votescast*100)
print(candidate_info)