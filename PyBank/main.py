

import os

# Module for reading CSV files
import csv

csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)


    #initialize arrays for month, total, profit/loss and change in profit/loss
    month, value, to, changeval=[],[],[],[]  
    count=0
    total = 0
    for row in csvreader:   #loop 
        if row[0] != "Jan-2010":
            month.append(row[0])  #filter out the first month from array because we dont need it
        value.append(row[1])     #get profit/loss each month store in array called value
        count+=1;               #count total month
    
    intvalue= [int(x) for x in value]  #covert profit/loss from string to int
    total = sum(intvalue)               #calculate the sum of profit/loss
         
    for x in range(len(value)-1):       
        changeval.append(intvalue[x+1]-intvalue[x])   #calculate the change of profit/loss everymonth

    avg = round(sum(changeval) / (len(value) - 1),2)       #perform time series analysis

    to=dict(zip(month,changeval))       #zip(month and change in profit/loss) into a dictionary set

    #get min and max
    maxmonth=(max(to, key=to.get))
    maxval= max(to.values())
    minmonth = (min(to, key=to.get))
    minval = min(to.values())

#print to terminal
def print1():
    print("Financial Analysis \n-----------------------------\nTotal Month: {}\nTotal: ${}".format(count,total))
    print("Average Change: $"+str(avg))
    print("Greatest Increase in Profits: {} (${})".format(maxmonth, maxval))
    print("Greatest Decrease in Profits: {} (${})".format(minmonth, minval))

print1()




#save output to txt file
output_file = os.path.join(os.path.dirname(__file__), "final_output_pybank.txt")

with open(output_file, 'w') as the_file:
    the_file.write("Financial Analysis \n-----------------------------\nTotal Month: {}\nTotal: ${}".format(count,total))
    the_file.write("\nAverage Change: $"+str(avg))
    the_file.write("\nGreatest Increase in Profits: {} (${})".format(maxmonth, maxval)+"\nGreatest Decrease in Profits: {} (${})".format(minmonth, minval))