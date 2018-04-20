import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=172.27.128.1&key=AIzaSyBEW7jLQJt3uw6T_X4DYj_hb6GP0VTPUeM'
req = requests.get(url)
print(req.json())