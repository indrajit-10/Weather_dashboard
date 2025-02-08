from flask import Flask, render_template, request
from weather import get_weather

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    
    if weather_data:
        return render_template('weather.html', weather=weather_data, city=city)
    else:
        return render_template('index1.html', error="City Not Found!")
    
if __name__ == '__main__':
    app.run(debug=True)