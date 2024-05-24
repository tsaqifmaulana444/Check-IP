import socket
import requests
import pprint
import json

hostname = input("Enter Domain: ")
ip_address = socket.gethostbyname(hostname)

request_url = "https://geolocation-db.com/jsonp/" + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for key, value in geolocation.items():
	pprint.pprint(f"{key} : {value}")

#print(f'Domain Name: {hostname}, IP Address: {ip_address}')
