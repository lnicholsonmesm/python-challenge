'''
- You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
-The total number of votes cast
-A complete list of candidates who received votes
-The percentage of votes each candidate won
-The total number of votes each candidate won
-The winner of the election based on popular vote.
'''

#DATA MANIPULATION STUFF
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    votecsvheaders = next(csvreader)
    polldata = [stuff for stuff in csvreader]
    

# print(votecsvheaders, polldata[0:3])
candidate_vote =[stuff[2] for stuff in polldata]

#TOTAL VOTES
total_votes = len(candidate_vote)

#VOTES FOR RUNNING PERSON
khanvotes = len([stuff for stuff in candidate_vote if stuff == 'Khan'])
correyvotes = len([stuff for stuff in candidate_vote if stuff == 'Correy'])
livotes = len([stuff for stuff in candidate_vote if stuff == 'Li'])
otooleyvotes = len([stuff for stuff in candidate_vote if stuff == "O'Tooley"])

#make a voter dictionary
vote_dict = {
    "Khan": khanvotes,
    "Correy": correyvotes,
    "Li": livotes,
    "O'Tooley": otooleyvotes
}
maxvotes = 0 

for entry,value in vote_dict.items():
    if value > maxvotes:
        maxvotes = value
        winner = entry

# max(khanvotes,correyvotes,livotes,otooleyvotes)

# % BREAKDOWN OF VOTES
khanpct = khanvotes/total_votes
correypct = correyvotes/total_votes
lipct = livotes/total_votes
otooleypct = otooleyvotes/total_votes

#for counterbit in range(0, len(moneys)-1):
 #   mom_delta.append(moneys[counterbit+1] - moneys[counterbit])


print(
    f"This is your great Poll.\n",
    "Election Results\n",
    "-------------------------\n",
    f"Total Votes: [tot_votes]\n",
    "-------------------------\n",
    f"Khan: {khanpct*100:.1f}% ({khanvotes})\n",
    f"Correy: {correypct*100:.1f}% ({correyvotes})\n"
    f"Li: {lipct*100:.1f}% ({livotes})\n",
    f"O'Tooley: {otooleypct*100:.1f}% ({otooleyvotes})\n",
    "-------------------------\n",
    f"Winner: {winner}\n",
    "-------------------------"
)

#create a file in a place with a name
#f = open('FinancialAnalysis.txt', 'w') this would make the file

filepath = os.path.join('Analysis', 'analysis.txt') 
f = open(filepath, 'w')
f.writelines(
    [
       "This is your great Poll.\n",
       "Election Results\n",
       "-------------------------\n",
       f"Total Votes: {total_votes}\n",
       "-------------------------\n",
       f"Khan: {khanpct*100:.1f}% ({khanvotes})\n",
       f"Correy: {correypct*100:.1f}% ({correyvotes})\n"
       f"Li: {lipct*100:.1f}% ({livotes})\n",
       f"O'Tooley: {otooleypct*100}% ({otooleyvotes})\n",
       "-------------------------\n",
       f"Winner: {winner}\n",
       "-------------------------"
    ]
)
f.close()