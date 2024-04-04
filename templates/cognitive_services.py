import requests
import json

# Set your subscription key and endpoint
subscription_key = 'aa82d1d47b2941cf8eeb40fea7e920f5'
endpoint = 'https://sweta-vison-services.cognitiveservices.azure.com/'

# URL of the image to analyze
image_url = 'https://seasalttherapy.com/wp-content/uploads/2021/01/Rashes.jpg'

# API endpoint for analyzing images
analyze_url = f'{endpoint}/vision/v3.1/analyze'

# Parameters for the analyze request
params = {
    'visualFeatures': 'Description,ImageType',
    'language': 'en'
}

# Request headers
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

# Request body with image URL
data = {'url': image_url}

# Send the request
response = requests.post(analyze_url, headers=headers, params=params, json=data)

# Get the JSON response
result = response.json()

# Display the description
if 'description' in result:
    description = result['description']['captions'][0]['text']
    print(description)
else:
    print('Description not found')










