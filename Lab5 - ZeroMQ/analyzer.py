import zmq
import json
import datetime

# 0MQ Settings
context = zmq.Context()

# CSV Recevier from Data Seperator
csvReceiver = context.socket(zmq.PULL)
csvReceiver.connect('tcp://127.0.0.1:4444')


# Array and Age Sender to Reducer
arraySender = context.socket(zmq.PUSH)
arraySender.bind('tcp://127.0.0.1:4445')


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


# Read CSV row and find how many months the person lives
while True:
	message = csvReceiver.recv()

	# b'array' -> a string representation of array -> list object
	arr = eval(message.decode('utf-8'))
	# print(arr[3])
	dateOfBirth = {}
	date = arr[3]
	dateOfBirth['day'] = int(date.split('.', 3)[0])
	dateOfBirth['month'] = int(date.split('.', 3)[1])
	dateOfBirth['year'] = int(date.split('.', 3)[2])
	

	# Append that how many months a person lives
	arr.append(getage(now, dateOfBirth))
	# print(arr)

	# Send them to Reducer
	arrJson = json.dumps(arr)
	arraySender.send_string(arrJson)