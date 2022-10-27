import urllib.request

URL = "https://www.google.com/"

response = urllib.request.urlopen(URL)
print(response.read())