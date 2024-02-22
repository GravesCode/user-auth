# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 

url = "http://localhost:5000/login"

# Making a get request 
user = "foo"
password = "bar"

response = requests.get(url, auth = HTTPBasicAuth(user, password))

if response.status_code != 200:
    try:
        error_data = response.json()  # Attempt to parse JSON response
        error_message = error_data.get("error", "Invalid credentials")
    except ValueError:
        error_message = "Invalid credentials"  # Fallback if response is not JSON

    print(f"Authentication failed:", error_message, "\nCode:", response.status_code)
else:
    # Handle successful response (status code 200)
    print("Authentication successful!")
    print(response.text)