import requests
import json


r = requests.post("http://localhost:5000/api/users", 
json={
"firstName": "injected",
"lastName" : "injected",
"email" : "injected@email.com",
"password" : "injected",
})


print(f"Status Code: {r.status_code}, Response: {r.json()}")



