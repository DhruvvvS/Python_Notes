# Connecting API with Python
# API stands for Application Programming Interface. 
# It is a set of rules and protocols that allows different software applications to communicate with each other. 
# APIs enable developers to access and use the functionality of other applications, services, or platforms without having to understand their internal workings.

# To connect to an API in Python, you can use the requests library, which allows you to send HTTP requests and handle responses easily.
from tkinter.messagebox import OK

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    # The URL is constructed by combining the base URL with the specific endpoint for fetching Pokémon information, which includes the Pokémon's name.
    url = f"{base_url}pokemon/{pokemon_name}"

    # get method is used to send a GET request to the specified URL.
    response = requests.get(url)

    print(response)
    # The response object contains the server's response to the HTTP request.
    # If the request was successful (status code 200), we can access the data returned by the API using the .json() method, which parses the JSON response into a Python dictionary.
    return response.json()

pokemon_name = input("Enter the name of a Pokémon: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")

## Posting data to an API:
payload = {
    "title": "My Post",
    "body": "Hello World",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

print(response.status_code)  # 201 = created
print(response.json())

## Putting and Deleting data to an API:

# PUT - update existing data
response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "Updated Title"}
)
print(response.json())

# DELETE - delete data
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 = deleted

""" Concept                Description
requests.get()          Fetch data from API
requests.post()         Send data to API
requests.put()          Update data
requests.delete()       Delete data
response.json()         Parse response as dict
response.status_code    Check if request succeeded
raise_for_status()      Auto-raise errors
headers                 Pass API keys, tokens
Session                 Reuse connection & headers"""


""" Code              Meaning
    200             OK — success
    201             Created
    400             Bad Request
    401             Unauthorized (wrong API key)
    404             Not Found
    500             Server Error"""