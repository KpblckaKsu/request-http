import requests
from pprint import pprint

def get_popular_videos():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1643414400&todate=1643500800&order=desc&sort=activity&tagged=python&site=stackoverflow"
    response = requests.get(url, headers={'User-agent': 'netology'})

    return response.json()

result = get_popular_videos()
#pprint(result)

list_questions = result['items']
for i in list_questions:
    pprint(i['title'])

