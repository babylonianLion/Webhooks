# Author: Hussain Al Zerjawi
# Purpose: Practicing webhooks using Python
# Date: 12/10/2022

import requests
import json

# Destination URL to which the webhook should send the POST request when an event occurs.
# Postman alternative endpoint webhook_url = "https://03b940fa-82e7-4694-82c9-a13a8df7641c.mock.pstmn.io"
webhook_url = "https://webhook.site/03c00641-845b-479e-bd67-e33d0a408485"

# The payload/data that is being sent.
data = {"name": "Mr Tester", "Company": "Ooredoo", "Age": 28, "Date": "12-10-2022", "Activate": True}

# Send the data using the requests Library as a POST request
r = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})