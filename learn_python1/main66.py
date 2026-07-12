# How to connect to an API using python.


import requests


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code==200:
       pokemon_data = response.json()                    # using this json method we can convert we converted into a python dictionary
       return pokemon_data                
    else:
        print("failed to retrieve data")

pokemon_name="typhlosion"                             # BY CHANGING NAME HERE WE CAN GET THE INFO OF ALL POKEMON SO API IS CONNECTED
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name:{pokemon_info["name"]}")
    print(f"ID:{pokemon_info["id"]}")
    print(f"Height:{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")