import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

#Q1: When was the first positive COVID case in Harrisonburg? When was the first positive case in Rockingham County?
HarrisonburgCases = []
data = parse_nyt_data("data/covid/us-counties.csv") #Using the already setup function to parse the NYT dataset
for i in data: 
    date, county, state, fips, cases, deaths = i 
    if county == "Harrisonburg city" and state == "Virginia" and int(cases) > 0 : #Filtering the huge NYT dataset search to only include Harrisonburg VA, and positive cases
        HarrisonburgCases.append((date, county, state, fips, cases, deaths)) #When it finds an entry that matches the criteria, it adds it to a list soley for Harrisonburg positive cases. 
        

print("The first positive COVID case in Harrisonburg is on: ", HarrisonburgCases[0][0]) #Since NYT already orders the data, pulling the first entry of Harrisonburg Covid Cases in my made list will give us the first positive case in harrisonburg

#Redo the exact same process for Rockingham County 

RockinghamCases = []
for i in data: 
    date, county, state, fips, cases, deaths = i 
    if county == "Rockingham" and state == "Virginia" and int(cases) > 0 : 
        RockinghamCases.append((date, county, state, fips, cases, deaths))
        

print("The first positive COVID case in Rockingham County is on: ", RockinghamCases[0][0])

#End of Q1

#Q2 On what date was the greatest number of new cases reported in Harrisonburg? What date in Rockingham County?
HburgMost = []
HburgmostDifference = 0
HburgpreviousCases = None

for i in HarrisonburgCases:
    date, county, state, fips, cases, deaths = i
    if HburgpreviousCases != None: #Skips the first entry since there is no previous case to compare with 
        Hburgdifference = cases - HburgpreviousCases #Storing the difference between entries in Harrisonburg cases
        if Hburgdifference > HburgmostDifference:
            HburgmostDifference = Hburgdifference
            HburgMost = []
            HburgMost.append(i) #At the end, will store the entry after the greatest difference as the loop is from perspective of current case

    HburgpreviousCases = cases #After the first loop, previous cases will be one behind 'cases', allowing the difference to be calcuulated

print("The date with the greatest number of new cases in Harrisonburg is: ", HburgMost[0][0])

#Redo the exact same process for Rockingham County

RockMost = []
RockmostDifference = 0
RockpreviousCases = None

for i in RockinghamCases:
    date, county, state, fips, cases, deaths = i
    if RockpreviousCases != None: #Skips the first entry since there is no previous case to compare with 
        Rockdifference = cases - RockpreviousCases #Storing the difference between entries in Harrisonburg cases
        if Rockdifference > RockmostDifference:
            RockmostDifference = Rockdifference
            RockMost = []
            RockMost.append(i) #At the end, will store the entry after the greatest difference as the loop is from perspective of current case

    RockpreviousCases = cases #After the first loop, previous cases will be one behind 'cases', allowing the difference to be calcuulated

print("The date with the greatest number of new cases in Rockingham County is: ", RockMost[0][0])

#End of Q2

#Q3 What was the worst seven-day period in Harrisonburg city for new COVID cases? What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal.

Hburg7Most =[]
Hburg7MostDifference = 0 
Hburg7previousCases =[]


for i in HarrisonburgCases:
    date, county, state, fips, cases, deaths = i

    Hburg7previousCases.append(cases)

    if Hburg7previousCases[7:] != []: #Becomes true once there are 7 previous cases to look through
        Hburg7Difference = cases - Hburg7previousCases[0] #Calculating the 7 day difference in cases

        if Hburg7Difference > Hburg7MostDifference:
            Hburg7MostDifference = Hburg7Difference
            Hburg7Most = []
            Hburg7Most.append(i)#Will store entry of the last day on the highest 7 day difference 

        Hburg7previousCases = Hburg7previousCases[1:] # Removes the first entry so the list contains the next 7 day period to check if greater

#Once the greatest 7 day difference is found, and the last day of that period is stored. Go Back and store the 6 dates before in a combined list.

for i in HarrisonburgCases:
    Hburg7previousCases.append(i)

    if Hburg7previousCases[7:] != []:
        Hburg7previousCases = Hburg7previousCases[1:] #Stores the full entries up until the last day of the highest 7 day difference

    if i == Hburg7Most[0]:
        Hburg7Most = Hburg7previousCases
        


print("The worst seven-day period in Harrisonburg is: ")

for i in Hburg7Most:
        date, country, state, fips, cases, deaths = i
        print(date)

#Redo the exact same process for Rockingham County

RockMost =[]
Rock7MostDifference = 0 
Rock7previousCases =[]


for i in RockinghamCases:
    date, county, state, fips, cases, deaths = i

    Rock7previousCases.append(cases)

    if Rock7previousCases[7:] != []:
        Rock7Difference = cases - Rock7previousCases[0]

        if Rock7Difference > Rock7MostDifference:
            Rock7MostDifference = Rock7Difference
            Rock7Most = []
            Rock7Most.append(i)

        Rock7previousCases = Rock7previousCases[1:]

for i in RockinghamCases:
    Rock7previousCases.append(i)

    if Rock7previousCases[7:] != []:
        Rock7previousCases = Rock7previousCases[1:]

    if i == Rock7Most[0]:
        Rock7Most = Rock7previousCases
        


print("The worst seven-day period in Rockingham County is: ")

for i in Rock7Most:
        date, county, state, fips, cases, deaths = i
        print(date)

#End of Q3




