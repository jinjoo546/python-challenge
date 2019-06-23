import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes = 0
candidatelist= []
votecount = []
percentage = []
maxnum = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes = totalvotes + 1
        candidatename = row[2]

        if candidatename in candidatelist:
            index = candidatelist.index(candidatename)
            votecount[index] = votecount[index]+ 1

        else:
            candidatelist.append(candidatename)
            votecount.append(1)
  
maxvotes = votecount[0]    

for n in range(len(candidatelist)):
    vpercent = round(votecount[n]/totalvotes *100, 3)
    percentage.append(vpercent)

    if votecount[n] > maxvotes:
        maxvotes = votecount[n]
        maxnum = n

winner = candidatelist[maxnum]    

print("Election Results")
print("----------------------")
print(f"Total Votes: {totalvotes}")
print("----------------------")
for n in range(len(candidatelist)):
    print(f"{candidatelist[n]}: {percentage[n]}% ({votecount[n]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------"'\n')

file = open("textfile.txt", "w")
file.write("Election Results"'\n')
file.write("----------------------"'\n')
file.write(f"Total Votes: {totalvotes}"'\n')
file.write("----------------------"'\n')
for n in range(len(candidatelist)):
    file.write(f"{candidatelist[n]}: {percentage[n]}% ({votecount[n]})"'\n')
file.write("----------------------"'\n')
file.write(f"Winner: {winner}"'\n')
file.write("----------------------"'\n')
file.close