import zmq
import sys

context = zmq.Context()

csvReceiver = context.socket(zmq.PULL)
csvReceiver.connect('tcp://127.0.0.1:4444')

while True:
	message = csvReceiver.recv()
	print(message.decode('utf-8'))
	# b'array' -> a string representation of array -> list object
	arr = eval(message.decode('utf-8'))
	print(arr[3])