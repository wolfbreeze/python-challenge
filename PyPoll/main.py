# import libraries
import os
import csv

# create and define all varibles needed
totalVotes = 0
candidateList = []
voteCountList = []


csvpath = os.path.join("data","election_data.csv")
#print(csvpath)
with open(csvpath, newline='') as polldata:
    #skip the header row
    polldata.readline()

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(polldata, delimiter=',')

    #  Each row is read as a row
    for row in csvreader:
        totalVotes = totalVotes+1
        candidate = row[2]
        
        #figure the math
        if not candidate in candidateList:
            candidateList.append(candidate)
            voteCountList.append(1)
        else:
            indexofCandidate =  candidateList.index(candidate)
            curVoteTally = voteCountList[indexofCandidate]
            voteCountList[indexofCandidate] = curVoteTally+1

#create and open output file to write resuts to                        
outputpath = os.path.join("Output","VoteResults.txt")

lines = []

resultsfile = open(outputpath, "w")

#create the output
lines.append("Election Results")
lines.append("-------------------------")
lines.append("Total Votes: "+str(totalVotes))
lines.append("-------------------------")
winningVotes = 0
for candidate in candidateList:
    votes = voteCountList[candidateList.index(candidate)]
    pctVotes = (votes/totalVotes)*100
    if votes > winningVotes:
        winner = candidate
        winningVotes = votes
    lines.append(candidate+": "+str(round(pctVotes,2))+"% "+"("+str(votes) +")")
lines.append("-------------------------")
lines.append("Winner: "+winner)
for line in lines:
    print(line)
    print(line,file=resultsfile)
resultsfile.close()  
