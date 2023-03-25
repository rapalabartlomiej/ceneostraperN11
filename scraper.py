import requests
#product_code = input("podaj kod produktu")
product_code = "128917874"
url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
response = requests.get(url)
print(response)

