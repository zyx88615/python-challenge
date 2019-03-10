
import os

# Module for reading CSV files
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
csvpath = os.path.join(os.path.dirname(__file__), 'employee_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    id,name,dob,ssn,state=[],[],[],[],[]
    k=[]
    for row in csvreader:
        k.append(row)
        if row[4] in us_state_abbrev.keys():
            row[4] = us_state_abbrev.get(row[4])

        id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
    for x in range(len(dob)):
        dob[ x]= (datetime.strptime(dob[x ],'%Y-%m-%d'))
        dob[ x ]=dob[x].strftime('%m-%d-%Y')
        ssn[ x ]="***-**-"+ssn[x][7:]
    for a in k:
        state.append(a[4])
    zzip = zip(id,name,dob,ssn,state)



output_file = os.path.join("output2.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the first row (column headers)
    writer.writerow(['ID','Name','Date of Birth','SSN','State'])

    # Write the second row
    for x in range(len(id)):
        writer.writerow([id[x],name[x],dob[x],ssn[x],state[x]])
