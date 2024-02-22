# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 

url = "http://localhost:5000/login"

# Making a get request 
response = requests.get('http://localhost:5000/login',
            auth = HTTPBasicAuth('user1', 'abc123'))
  
# print request object 
print(response)