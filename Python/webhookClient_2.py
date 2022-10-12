import requests
import json

webhook_url = "https://webhook.site/03c00641-845b-479e-bd67-e33d0a408485"

data = {"name": "Mr Tester", "Company": "Ooredoo", "Age": 28, "Date": "12-10-2022", "Activate": True}

r = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})