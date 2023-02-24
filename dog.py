import requests
dog = input()

pre_results = requests.get(f'https://dog.ceo/api/breed/{dog}/images/random')

result = pre_results.json()

print(result["message"])

