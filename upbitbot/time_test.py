from textwrap import indent
import time
import json
import webbrowser
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError

import requests

url = "https://api.upbit.com/v1/orderbook?markets=KRW-BORA"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers).json()

print(json.dumps(response, indent=4))