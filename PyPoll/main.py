#import required modules
import os
import csv

#define variable to store location of csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#define necessary variables and lists
vote_count = 0
candidates = []
unique_candidate = []
votes = []
vote_percentage = []

#open and read csv file
with open(csvpath, 'r') as csv_file:
    
    csvreader = csv.reader(csv_file, delimiter=',')

#define variable to store csv header
    csv_header = next(csvreader)

#loop through csv file and count number of votes
    for row in csvreader:
        vote_count = vote_count + 1

#append csv file candidate column to list
        candidates.append(row[2])

#loop through candidate list, identify all unique candidates using the set function and add to unique candidate list
    for name in set(candidates):
        unique_candidate.append(name)

#count number of votes for each candidate and add to votes list
        number_of_votes = candidates.count(name)
        votes.append(number_of_votes)

#calculate percentage of votes that went to each candidate and add to list
        percent = (number_of_votes / vote_count) * 100
        vote_percentage.append(percent)

#run max function to identify highest number of votes and identify the name of the candidate related to that number of votes
    highest_vote = max(votes)
    winner = unique_candidate[votes.index(highest_vote)]

#print results to terminal
print("--------------------------------------")
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------------------")
#loop through the lists using the length of the unique_candidate list as the range to print out each candidates results
for names in range(len(unique_candidate)):
    print(f"{unique_candidate[names]}: {vote_percentage[names]: .3f}% ({votes[names]})")
print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

#define variable to store the location of the text output file 
output_path = os.path.join("election_results.txt")

#open and write results to text file
with open(output_path, 'w') as text:
    text.write("--------------------------------------\n")
    text.write("Election Results\n")
    text.write("--------------------------------------\n")
    text.write(f"Total Votes: {vote_count}\n")
    text.write("--------------------------------------\n")
#loop through the lists using the length of the unique_candidate list as the range to print out each candidates results
    for names in range(len(unique_candidate)):
        text.write(f"{unique_candidate[names]}: {vote_percentage[names]: .3f}% ({votes[names]})\n")
    text.write("--------------------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("--------------------------------------")