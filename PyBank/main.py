import csv
import os

budget_data_csv = "/Users/alejandrafeatherston-rajcic/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

summonths = 0
sumprofits = 0
changeprofits = 0
changeofprofits_list = []
greatestincrease = ["",0]
greatestdecrease = ["", 999999999999]

profit_loss = 0

with open (budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        
        sumprofits = int(row[1]) + sumprofits
        summonths +=1

        changeprofits = int(row[1]) - profit_loss
        profit_loss = int(row[1])

        changeofprofits_list.append(changeprofits)
    
        if changeprofits > greatestincrease[1]:
            greatestincrease[0]=row[0]
            greatestincrease[1]= changeprofits
        if changeprofits < greatestdecrease[1]:
            greatestdecrease[0]=row[0]
            greatestdecrease[1]=changeprofits

averageprofitchange = round((sum(changeofprofits_list[1:]))/(len(changeofprofits_list[1:])),2)

print("Total months: " + str(summonths))
print("Total: " + str(sumprofits))
print("Average  change: " + str(averageprofitchange))
print("Greatest increase: " + str(greatestincrease[1]))
print("Greatest decrease: " +str(greatestdecrease[1]))


analysis_file = "PyBank/analysis/analysis.txt"

with open(analysis_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("Total months: " + str(summonths)+"\n")
    txtfile.write("Total: " + str(sumprofits)+"\n")
    txtfile.write("Average  change: " + str(averageprofitchange)+"\n")
    txtfile.write("Greatest increase: " + str(greatestincrease[1])+"\n")
    txtfile.write("Greatest decrease: " +str(greatestdecrease[1])+"\n")