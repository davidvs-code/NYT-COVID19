# COVID 19 Data
# rmdir covid-19-data
# git clone https://github.com/nytimes/covid-19-data.git

import csv
import matplotlib.pyplot as plt
import numpy as np 


u = []
v = []
w = []
x = []
y = []
z = []


filename = 'covid-19-data/us-counties.csv'


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


# Plot raw signals

# plt.figure(1)
# plt.plot(sm_cases)
# plt.xlabel('Date')
# plt.ylabel('Number')
# #plt.legend()
# plt.show()	

plt.figure(2)
plt.plot(sm_deaths)
plt.xlabel('Date')
plt.ylabel('Number')
#plt.legend()
plt.show()	












