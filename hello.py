import requests

# Download a web page

response = requests.get("https://api.github.com")
print(response.status_code) # should print 200

print("The perfect way to learn is to be consistent not showing intense.")