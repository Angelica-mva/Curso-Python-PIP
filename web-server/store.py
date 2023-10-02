import requests

url_api_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(url_api_categories)
    print (r.status_code)
    print(r.text)
    print(type(r.text)) #Hasta aquí el codigo entrega la información pero en FORMATO TEXTO
    categories = r.json() #Convierte a formato JSON (lista de diccionarios)
    print(categories) 
    print(type(categories)) #con este print corroboro que esté en JSON
    for category in categories: #busca solo el valor de las llaves "name" de cada diccionario
        print(category['name']) 

