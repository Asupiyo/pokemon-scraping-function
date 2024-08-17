import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu/"

r = requests.get(url, timeout=5)
r = r.json()

id = r['id']
name = r['name']
image = r['sprites']['front_default']
types = r['types'][0]['type']['name']

print(id)
print(name)
print(image)
print(types)