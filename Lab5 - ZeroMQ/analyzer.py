import zmq
import csv
import re
import datetime

# CSV file to read
FILE = './data.csv'

# Get age in form of months
def getage(now, dateOfBirth):
	years = now.get("year") - dateOfBirth.get("year")
	months = now.get("month") - dateOfBirth.get("month")
	if (now.get("day") < dateOfBirth.get("day")):
		months -= 1
		while months < 0:
			months += 12
			years -= 1
	months += (12* years)
	return months


# Get current year, month and day
now = {}
now['year'] = datetime.datetime.now().year
now['month'] = datetime.datetime.now().month
now['day'] = datetime.datetime.now().day


# Read CSV file and find how many months the person lives
with open(FILE, 'r') as fileRead:
	# with open(FILE, 'w') as fileWrite:
	reader = csv.reader(fileRead, delimiter=',')
		# writer = csv.writer(fileWrite, lineterminator='\n')

	lineCount = 0
	for row in reader:
		if lineCount == 0:
			print(f'[COLUMN NAMES]: {", ".join(row)}')
			lineCount += 1
		else:
			dateOfBirth = {}
			date = row[3]
			dateOfBirth['day'] = int(date.split('.', 3)[0])
			dateOfBirth['month'] = int(date.split('.', 3)[1])
			dateOfBirth['year'] = int(date.split('.', 3)[2])
			print(f'{row[1]} {row[2]} lives for {getage(now, dateOfBirth)} months.')
			lineCount += 1
	print(f'We read {lineCount} lines.')



# dateOfBirth = {'year': 2001, 'month': 1, 'day': 29}
# print(getage(now, dateOfBirth))





# with open(FILE, 'rt') as file:
# 	# writer = csv.writer(file, delimiter=',')
# 	data = csv.reader(file)
# 	print(data)
# 	for line in data:
# 		print(line)