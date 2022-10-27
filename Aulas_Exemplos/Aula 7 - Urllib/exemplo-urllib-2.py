import urllib.request

URL = "https://www.google.com/"

response = urllib.request.urlopen(URL)

#cabeçalho de requisição
headers = response.info()
print('DATA: %s' %headers['date'])
print(headers)