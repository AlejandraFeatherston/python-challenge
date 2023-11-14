import csv
import os

budget_data_csv = "/Users/alejandrafeatherston-rajcic/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

totalmonths = 0
totalprofits = 0
changeprofits = 0
changeofprofits_list = []
greatestincrease = 0
lowestincrease = 0

profit_loss = 0

with open (budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        totalmonths +=1
        totalprofits = int(row[1])+ totalprofits

        changeprofits = int(row[1])-profit_loss
        profit_loss = int(row[1])
        changeofprofits_list.append(changeprofits)    


    
averageprofitchange = round((sum(changeofprofits_list[1:]))/(len(changeofprofits_list[1:])),2)

max = max(changeofprofits_list)
min = min(changeofprofits_list)

print("Total months: " + str(totalmonths))
print("Total: " + str(totalprofits))
print("Average  change: " + str(averageprofitchange))
print("Greatest increase: " + str(max))
print("Greatest decrease: " +str(min))


analysis_file = "PyBank/analysis/analysis.txt"

with open(analysis_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("Total months: " + str(totalmonths)+"\n")
    txtfile.write("Total: " + str(totalprofits)+"\n")
    txtfile.write("Average  change: " + str(averageprofitchange)+"\n")
    txtfile.write("Greatest increase: " + str(max)+"\n")
    txtfile.write("Greatest decrease: " +str(min)+"\n")