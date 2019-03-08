import os
from decimal import Decimal
# Module for reading CSV files
import csv

csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')


with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    csv_header = next(csvreader)

    Candidate=[] #create candidate array

    d=([a[2] for a in csvreader])  #append to list

    candidate = {}.fromkeys(d,0)   #set key from list and set value to 0
    print(candidate)

    for x in d: 
        candidate[x] +=1   #count the vote
    print(candidate)
    totalvote= sum(candidate.values())

    winner = (max(candidate, key=candidate.get))    #get the winner


    print("Election Results\n------------------------------")     #print to ternimal
    print("Total Votes: "+str(totalvote)+"\n------------------------------")
    for can in sorted(candidate, key=candidate.get, reverse=True):
        print(f"{can:10} {round(Decimal(candidate[can]/totalvote*100),3)}%   ({candidate[can]})")
    print("------------------------------"+"\nWinner: "+winner+"\n------------------------------")


# write to txt file
output_file = os.path.join(os.path.dirname(__file__), "final_output_pypoll.txt")

with open(output_file, 'w') as the_file:
    the_file.write("Election Results\n------------------------------")
    the_file.write("\nTotal Votes: "+str(totalvote)+"\n------------------------------\n")
    for can in sorted(candidate, key=candidate.get, reverse=True):
        the_file.write(f"{can:10} {round(Decimal(candidate[can]/totalvote*100),3)}%   ({candidate[can]})\n")
    the_file.write("------------------------------"+"\nWinner: "+winner+"\n------------------------------")