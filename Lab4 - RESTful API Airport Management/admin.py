import requests
from time import sleep

BASE = 'http://127.0.0.1:5000'

while True:
	print('========================================')
	print("""===WELCOME TO THE ADMIN PANEL===
1. Authentication
2. Am I Authenticated?
3. Get Flight
4. Add Flight
5. Update Flight
6. Delete Flight
7. Logout
8. Exit""")
	command = input('Please provide a number between 1-6:')
	if command == '1':
		LINK = BASE + '/authentication_authorization'
		username = input('Username: ')
		password = input('Password: ')
		print(LINK)
		response = requests.post(LINK, {'username': username, 'password': password})
		print(response.json())
	elif command == '2':
		LINK = BASE + '/authentication_authorization'
		print(LINK)
		response = requests.get(LINK)
		print(response.json())
	elif command == '3':
		print('Please provide the city names to find related Flights Data.')
		source = input('Source City: ')
		destination = input('Destination City: ')
		if(source and destination):
			LINK = BASE + '/flights' + '/' + source + '/' + destination
			print(LINK)
			response = requests.get(LINK)
			print(response.json())
		else:
			print('Please provide both of the cities.')
	elif command == '4':
		LINK = BASE + '/authentication_authorization'
		response = requests.get(LINK).json()
		if(response['authenticated']):
			print('Enter the related information:')
			LINK = BASE + '/flights'
			source = input('Source City (Paris): ')
			destination = input('Destination City (Paris): ')
			info = input('Information (VIP Flight): ')
			passengers = int(input('The Number of Passengers (300): '))
			arrival = input('Arrival Date and Time (2020-12-31 23:00:00): ')
			departure = input('Departure Date and Time (2020-12-31 23:00:00): ')
			if(source and destination and info and passengers and departure and arrival):
				response = requests.post(LINK, {'source': source, 'destination': destination,
					'info': info, 'passengers': passengers, 'arrival': arrival, 'departure': departure})
				print(response.json())
			else:
				print("Please, provide all the required fields")
		else:
			print('If you want to, add flights please authenticate yourself.')
	elif command == '5':
		LINK = BASE + '/authentication_authorization'
		response = requests.get(LINK).json()
		if(response['authenticated']):
			print('Enter the updated information:')
			LINK = BASE + '/flights'
			id = int(input("Which flight ID do you want: "))
			if(str(id) == ''):
				print('Please provide Flight ID')
				continue
			source = input('Source City (Paris): ')
			destination = input('Destination City (Paris): ')
			info = input('Information (VIP Flight): ')
			passengers = input('The Number of Passengers (300): ')
			arrival = input('Arrival Date and Time (2020-12-31 23:00:00): ')
			departure = input('Departure Date and Time (2020-12-31 23:00:00): ')
			
			data = {}
			data['id'] = id

			if(source):
				data['source'] = source
			if(destination):
				data['destination'] = destination
			if(info):
				data['info'] = info
			if(passengers):
				data['passengers'] = int(passengers)
			if(arrival):
				data['arrival'] = arrival
			if(departure):
				data['departure'] = departure

			response = requests.put(LINK, data)
			print(response.json())
		else:
			print('If you want to, add flights please authenticate yourself.')
	elif command == '6':
		LINK = BASE + '/authentication_authorization'
		response = requests.get(LINK).json()
		if(response['authenticated']):
			print('Enter the Flight ID:')
			LINK = BASE + '/flights'
			id = int(input("Which flight ID do you want: "))
			if(str(id) == ''):
				print('Please provide Flight ID')
				continue
			data = {}
			data['id'] = id
			response = requests.delete(LINK, data=data)
			print(response.json())
	elif command == '7':
		LINK = BASE + '/authentication_authorization'
		response = requests.get(LINK).json()
		if(response['authenticated']):
			LINK = BASE + '/end_session'
			response = requests.get(LINK)
			print(response.json())
	elif command == '8':
		break;
	else:
		print('Please, provide the valid number');
