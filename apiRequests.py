#NASA Astronomy Picture of the Day (APOD) API
import requests

# Setting up a API endpoint
api_key = '8iUee8PaqJdKhWegfpIgP5b7KG0n2QQ5UvaWCyHW'
url =f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

#Sending a GET reuqests
response = requests.get(url)
if response.status_code == 200: 
    data = response.json()
else: 
    print("Failed to fetch data.")

# Parse and display specific information
print(f"Title: {data['title']}")
print(f"Date: {data['date']}")
print(f"Explanation: {data['explanation']}")
print(f"URL: {data['url']}")
