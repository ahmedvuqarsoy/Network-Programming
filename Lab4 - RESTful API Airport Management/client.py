import requests

BASE = "http://127.0.0.1:5000"

# source = 'NewYork'
# destination = 'Doha'

# LINK = BASE + '/flights/' + source + '/' + destination
# print(LINK)
# response = requests.get(LINK)
# print(response.json())


# ADMIN AUTHENTICATION

# authentication_authorization
# end_session

# LINK = BASE + '/authentication_authorization'
# print(LINK)
# response = requests.get(LINK)
# response = requests.post(LINK, {'username': 'admin', 'password': 'admin'})
# print(response.json())



# ADD DATA
# LINK = BASE + '/flights'
# print(LINK)
# response = requests.post(LINK, {'source': 'Istanbul', 'destination': 'Paris', 'info': 'New Year', 'passengers': 333, 'arrival': '2020-12-31 23:00:00', 'departure': '2020-12-31 23:00:00'})
# print(response.json())


# UPDATE DATA
# LINK = BASE + '/flights'
# print(LINK)
# response = requests.put(LINK, {'id': 7, 'passengers': 1000})
# print(response.json())


# DELETE DATA
LINK = BASE + '/flights'
print(LINK)
response = requests.delete(LINK, data={'id': 7})
print(response.json())