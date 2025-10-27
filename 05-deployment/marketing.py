import requests

url = 'http://localhost:9696/05-deployment-hw'
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

convert = requests.post(url, json=client).json()

print('response:', convert)