#import dependencies
import os
import csv

#find paths of files
csvpath1 = os.path.join('.', 'raw_data', 'employee_data1.csv')
csvpath2 = os.path.join('.', 'raw_data', 'employee_data2.csv')

#create a dictionary to hold values for output
new_employee_data = []
    
#state abbreviation reference
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

#create a function to use for both files
def convert_data(csvpath):
    
    #open file with reader
    with open(csvpath, newline='') as file1:
        reader1 = csv.DictReader(file1)
        print(reader1)

        #loop through rows in file
        for row in reader1:

            #collect emp id values
            emp_id=(row["Emp ID"])

            #collect first name and last name values
            name_split = row["Name"].split(" ")
            first_name=(name_split[0])
            last_name=(name_split[1])

            #collect dob values
            dob_split = row["DOB"].split("-")
            dob = dob_split[1] + "/" + dob_split[2] + "/" + dob_split[0]

            #collect ssn values
            ssn=("***-**-" + row["SSN"][7:])

            #collect state values
            state = us_state_abbrev[row["State"]]
            
            #add a new row as a list to the dictionary
            new_employee_data.append({"Emp ID":row["Emp ID"],"First Name":first_name,"Last Name":last_name,"DOB":dob,"SSN":ssn,"State":state})

#call function to collect data from each file:
convert_data(csvpath1)

#open output file to write
csvpath = os.path.join("output.csv")
with open(csvpath, "w") as csvfile:

    #specify fieldnames and initiate the output file:
    fieldnames = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #write in the output file with the dictionary, following fieldnames
    writer.writeheader()
    writer.writerows(new_employee_data)