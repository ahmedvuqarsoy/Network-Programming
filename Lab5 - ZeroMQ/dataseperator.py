import zmq
import csv
import json

FILE = './data.csv'

context = zmq.Context()

# Socket to send CSV rows to Analyer
csvRowSender = context.socket(zmq.PUSH)
csvRowSender.bind('tcp://127.0.0.1:4444')

with open(FILE, 'r') as fileRead:
	reader = csv.reader(fileRead, delimiter=',')

	lineCount = 0
	for row in reader:
		if lineCount == 0:
			print(f'[COLUMN NAMES]: {", ".join(row)}')
			lineCount += 1
		else:
			rowJson = json.dumps(row)
			print(rowJson)
			csvRowSender.send_string(rowJson)
			lineCount += 1
	print(f'We read {lineCount} lines.')