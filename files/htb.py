import requests
url = 'https://www.hackthebox.eu/api/invite/how/to/generate'
response = requests.post(url)
print(response.data)