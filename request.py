import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r = requests.post(url,json={'LATITUDE':35.58, 'LONGITUDE':-121.49})
print(r.json())
