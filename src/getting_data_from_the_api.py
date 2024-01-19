import requests

param = {'page': 1, 'per_page': 100, 'text': 'NAME:снабжение', 'area': '1384'}

url = 'https://api.hh.ru/vacancies'
countrise = 'https://api.hh.ru/areas/113'
response = requests.get(url, params=param)
# response = requests.get(countrise)
# for i in response.json()['areas']:
#     print(i)
for i in response.json()['items']:
    print(i)