from flask import Flask
import requests

app = Flask(__name__)

API_KEY = '**********************************'#add here your google api key
address = '1 hack drive, menlo park, CA'

params = {
     'key': API_KEY,
    'address': address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

#base_url ='https://maps.googleapis.com/maps/api/staticmap?'

response = requests.get(base_url, params=params).json()
response.keys()

@app.route('/')
def startTest():
    return response#.json()
