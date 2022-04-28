import requests
import json

url = "https://api.upbit.com/v1/ticker?markets=KRW-SRM"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers).json()

test = json.dumps(response, indent=4)
listt = json.loads(test)
print(test)
#print(listt)
print(round(listt[0]['signed_change_rate']*100, 3))