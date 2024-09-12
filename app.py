from flask import Flask, render_template, request, redirect, url_for
from add import add_weather_data_to_db, get_weather_data_from_db
import requests
from datetime import datetime
## Flask framework to convert and display attributes using Janja
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city_name']
        return redirect(url_for('result', city=city_name))
    return render_template('home.html')

@app.route('/result/<city>')
def result(city):
    weather_data = get_weather_data_from_db(city)
    
    if weather_data:
        temperature = weather_data.temperature
        description = weather_data.description
        weather_condition = weather_data.weather_condition
        wind_speed = weather_data.wind_speed
        wind_direction = weather_data.wind_direction
    else:
        api_key = '095cd7f930e21d99793d0b6cd8ca8dad'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temperature = data['main']['temp'] - 273.15 
            description = data['weather'][0]['description']
            weather_condition = data['weather'][0]['main']
            wind_speed = data['wind']['speed']
            wind_direction = data['wind']['deg']
            
            add_weather_data_to_db(city, temperature, description, weather_condition, wind_speed, wind_direction)
        else:
            error_message = data.get('message', 'City not found')
            return render_template('error.html', message=error_message, response_status_code=response.status_code)
    
    return render_template('result.html', 
                            city=city, 
                            temperature=temperature, 
                            description=description, 
                            weather_condition=weather_condition, 
                            wind_speed=wind_speed, 
                            wind_direction=wind_direction)

if __name__ == '__main__':
    app.run(debug=True, port=555)
