# -*- coding: utf-8 -*-
import requests
import json

# API authorization
headers = {'x-api-key': 'UNIQUE_API_KEY', 'accept': 'application/json', 'accept': 'text/csv'}

# Choose endpoint
endpoint = 'https://www.capology.com/api/v2/soccer/renewals/club/manchester-city/'

# Retrieve json
json = requests.get(endpoint, headers=headers).text
print(json)
