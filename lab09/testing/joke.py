import requests

response = requests.get('https://official-joke-api.appspot.com/random_joke')

#joke = response.json()
#print(joke)

if (response.status_code == 200):
    joke = response.json()
    print(f'Joke: {joke['setup']}')
    print(f'Punchline: {joke['punchline']}')
