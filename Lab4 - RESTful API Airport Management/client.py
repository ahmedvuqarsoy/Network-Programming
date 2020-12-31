import requests
from colorama import Fore, Back, Style

BASE = 'http://127.0.0.1:5000'

while True:
	print(Fore.RED + '========================================')
	print(Fore.GREEN + 'Please provide the city names to find related Flights Data.')
	source = input(Fore.BLUE + 'Source City: ')
	destination = input(Fore.BLUE + 'Destination City: ')
	if(source and destination):
		LINK = BASE + '/flights' + '/' + source + '/' + destination
		print(Fore.WHITE + LINK)
		response = requests.get(LINK)
		print(response.json())
		print(Fore.RED + '========================================')
	else:
		print('Please provide both of the cities.')
		print(Fore.RED + '========================================')