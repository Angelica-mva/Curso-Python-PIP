import requests

url_api_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(url_api_categories)
    print (r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(categories)
    print(type(categories))
    for category in categories:
        print(category['name'])

