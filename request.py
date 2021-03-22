import requests

url = 'http://localhost:5000/result'
r = requests.get(url,json={'Time':5.0, 'Amount':2.0})

print(r.json())

