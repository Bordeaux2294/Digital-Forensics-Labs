import requests
url = "https://www.seantmiller.com/"
response = requests.get(url,verify=False).headers
print(response['server'])
