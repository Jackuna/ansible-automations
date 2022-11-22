import requests
import git

print("Hello from Python Script")
request_h = requests.get('https://api.github.com/users/naveenkrnl')
print (request_h.json())
