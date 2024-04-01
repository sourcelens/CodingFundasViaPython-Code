import requests
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(api_url)
print ( response.json() )