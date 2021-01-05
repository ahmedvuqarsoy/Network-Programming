import zmq
from operator import itemgetter

# 0MQ Settings
context = zmq.Context()

# Array Accept from Analyzer
arrayReceiver = context.socket(zmq.PULL)
arrayReceiver.connect('tcp://127.0.0.1:4445')


array = []

while True:
	message = arrayReceiver.recv()

	# b'array' -> a string representation of array -> list object
	arr = eval(message.decode('utf-8'))

	# Add coming to array
	array.append(arr)
	print(sorted(array, key=itemgetter(4)))


# array = [
# ['1', 'Jabrayil', 'Yunusov', '21.11.1949', 853],
# ['2', 'Farid', 'Harunov', '29.12.2000', 240],  
# ['3', 'Hajiahmad', 'Ahmadzada', '29.01.2001', 239],
# ['4', 'Sanan', 'Khalilov', '18.08.1998', 268],
# ['5', 'Farid', 'Ahmadzada', '13.08.2004', 196],
# ['6', 'Ugur', 'Ahmadzada', '28.10.2015', 62],
# ['7', 'Javidan', 'Amirov', '20.12.2013', 84]
# ]

# for i in range(len(array)):
# 	print(array[i])

# print("Sorted Array")

# sortedArray = sorted(array, key=itemgetter(4))
# for i in range(len(sortedArray)):
# 	print(sortedArray[i])

