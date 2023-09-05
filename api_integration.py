# app.py
#API Integrations (Using Requests Library):
from app import app
import requests

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')
    weather_data = response.json()
    # Process and return weather data
