from itertools import count

import requests
from pprint import pprint
import json
import csv

url = 'https://api.stackexchange.com/2.3/questions'

# headers ={"fromdate":"2021-07-07","todate":"2021-07-11","order":"desc",
#           "sort":"week","tagged":"Python","filter":"default",
#           "site":"stackoverflow","run":"true"}
# 1625702400 1625875200
params = {"fromdate": "2021-07-07", "todate": "2021-07-09", "order": "desc", "sort": "activity", "tagged": "python",
          "site": "stackoverflow"}

response = requests.get(url, params=params)
url_response = response.json()
data = url_response["items"]

with open("data.json", "w", ) as file:
    for item in data:
        pprint(item)
        file.write(json.dumps(item))
    pprint(item['owner'])
