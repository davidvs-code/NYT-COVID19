# COVID 19 Data
# git clone https://github.com/nytimes/covid-19-data.git

import csv
import matplotlib.pyplot as plt
import numpy as np 

filename = 'covid-19-data/us-counties.csv'

# Extract county specific data from csv file
san_mateo_date   = []
san_mateo_cases  = []
san_mateo_deaths = []

with open(filename, 'r') as csvfile:
	counties = csv.DictReader(csvfile, delimiter=',')
	for row in counties:

		if row['county'] == 'San Mateo':
			san_mateo_date.append(row['date'])
			san_mateo_cases.append(row['cases'])
			san_mateo_deaths.append(row['deaths'])


sm_cases  = list(san_mateo_cases)
sm_deaths = list(san_mateo_deaths)


# Calculate the diffirence in cases and deaths
cases_diff  = []
deaths_diff = []
counter = 0

for num in range(len(san_mateo_cases)-1):
	cases_diff.append([float(san_mateo_cases[num+1]) - float(san_mateo_cases[num])])
	deaths_diff.append([float(san_mateo_deaths[num+1]) - float(san_mateo_deaths[num])])


#### Create figures

# Plot raw signals
# plt.figure(1)
# plt.plot(sm_cases)
# plt.xlabel('Date')
# plt.ylabel('Cummulative Cases')
# #plt.legend()
# plt.show()	

# plt.figure(2)
# plt.plot(sm_deaths)
# plt.xlabel('Date')
# plt.ylabel('Cummulative Deaths')
# #plt.legend()
# plt.show()	

# plt.figure(3)
# plt.plot(cases_diff)
# plt.xlabel('Day')
# plt.ylabel('New Cases')
# #plt.legend()
# plt.show()	

# plt.figure(4)
# plt.plot(deaths_diff, 'r-')
# plt.xlabel('Day')
# plt.ylabel('New Deaths')
# #plt.legend()
# plt.show()	

