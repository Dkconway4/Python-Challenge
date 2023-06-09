import csv,os
election_filepath = os.path.join("Resources","election_data.csv")
#Variables to track
total_votes = 0
candidate_list = 0
voting_percentage = 0
candidate_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
winner = None

#Code to read file
with open(election_filepath) as dataset:
    reader = csv.reader(dataset)
    header = next(reader)
    thisdict = {}
    for row in reader:
        total_votes +=1
        current_name = row[2]
        if current_name in thisdict:
            thisdict[current_name]+=1
        else:
            thisdict[current_name]=1
output = open("analysis/PyPollText.txt","w")
output.write("Election Results\n")
output.write("------------------\n")
output.write("Total Votes {}\n".format(total_votes))

for name,number in thisdict.items():
    if not winner:
        winner = name
    else:
        if number > thisdict[winner]:
            winner = name
    output.write("{}: {:.3f}% ({})\n".format(name,number/total_votes*100,number))
output.write("------------------\n")
output.write("Winner {}\n".format(winner))
output.write("------------------\n")
