# Author: Hussain Al Zerjawi
# Purpose: Practicing webhooks using Python
# Date: 12/10/2022

import requests
import json

# Destination URL to which the webhook should send the POST request when an event occurs.
webhook_url = "http://127.0.0.1:5000/webhook"

# The payload/data that is being sent.
data = {"name": "Test Tester", "Company": "Ooredoo"}

# Send the data using the requests Library as a POST request
r = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})