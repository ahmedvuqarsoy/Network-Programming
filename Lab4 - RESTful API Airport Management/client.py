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

LINK = BASE + '/authentication_authorization'
print(LINK)
response = requests.get(LINK)
# response = requests.post(LINK, {'username': 'admin', 'password': 'admin'})
print(response.json())