import urllib.request

URL = "https://www.google.com/"

response = urllib.request.urlopen(URL)

#dados retornados pela requisição
dados = response.read()
print('LENGTH: %s' %len(dados))
print(dados)