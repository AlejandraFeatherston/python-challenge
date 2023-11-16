import csv

votescast = 0
candidate_list = []
totalvotes = []
percentagevotes_per_candidate = 0
percentagevotes_per_candidate_list = []
candidate_votes = []

election_data_csv = "PyPoll/Resources/election_data.csv"

with open(election_data_csv, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    for each_row in csvreader:
        votescast += 1
        totalvotes.append(each_row[2])

        if each_row[2] not in candidate_list:
            candidate_list.append(each_row[2])
        
    for i in range(len(candidate_list)):
        total = 0
        for j in range(len(totalvotes)):
            if candidate_list[i] == totalvotes[j]:
                total += 1
        candidate_votes.append(total)
    
    for x in range(len(candidate_list)):
        percentagevotes_per_candidate = round(candidate_votes[x]/votescast*100,3)
        percentagevotes_per_candidate_list.append(percentagevotes_per_candidate)
    
    winnerIndex = percentagevotes_per_candidate_list.index(max(percentagevotes_per_candidate_list))
    
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(votescast))
    print("-----------------------------")
    for a in range(len(candidate_list)):
        print(str(candidate_list[a]) + ": " + str(percentagevotes_per_candidate_list[a]) + "% (" + str(candidate_votes[a]) + ")")
    print("-----------------------------")
    print("Winner: " + str(candidate_list[winnerIndex]))
    print("-----------------------------")

analysis_results = "PyPoll/analysis/analysis_results.txt"

with open(analysis_results, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------------\n")
    txtfile.write("Total Votes: " + str(votescast) + "\n")
    txtfile.write("-----------------------------\n")
    for a in range(len(candidate_list)):
        txtfile.write(str(candidate_list[a]) + ": " + str(percentagevotes_per_candidate_list[a]) + "% (" + str(candidate_votes[a]) + ")\n")
    txtfile.write("-----------------------------\n")
    txtfile.write("Winner: " + str(candidate_list[winnerIndex]) + "\n")
    txtfile.write("-----------------------------\n")
