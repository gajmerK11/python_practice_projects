from flask import Flask, request, render_template_string
import requests
import json  # For pretty printing JSON (if needed)

app = Flask(__name__)

API_Key = 'd9292be1d2525ece0a43d6c97bb98d75'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Data</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 500px;
            text-align: center;
        }

        h1 {
            color: #4CAF50;
            margin-bottom: 20px;
        }

        form {
            margin-bottom: 20px;
        }

        input[type="text"] {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            width: 85%;
        }

        button:hover {
            background-color: #45a049;
        }

        .weather-info {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        .weather-info h2 {
            color: #333;
            margin-bottom: 15px;
        }

        .weather-info p {
            font-size: 18px;
            color: #555;
            margin: 8px 0;
        }

        .weather-info p span {
            font-weight: bold;
            color: #4CAF50;
        }

        .error-message {
            color: red;
            font-size: 18px;
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Weather Information</h1>
    <form method="POST">
        <input type="text" name="city" placeholder="Enter a city" required>
        <button type="submit">Get Weather</button>
    </form>

    {% if weather %}
    <div class="weather-info">
        <h2>Weather Details</h2>
        <p><span>City:</span> {{ weather['city'] }}</p>
        <p><span>Country:</span> {{ weather['country'] }}</p>
        <p><span>Temperature:</span> {{ weather['temperature'] }} °C</p>
        <p><span>Weather Type:</span> {{ weather['weather'] }}</p>
    </div>
    {% endif %}

    {% if error %}
    <div class="error-message">{{ error }}</div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather = None
    error = None  # Initialize error message as None
    if request.method == 'POST':
        city = request.form.get('city')
        base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}&units=metric"
        weather_data = requests.get(base_url).json()

        if weather_data.get("cod") == "404":
            # If the city is not found, set an error message
            error = "Invalid city name"
        else:
            # If the city is found, extract weather data
            weather = {
                'city': weather_data['name'],
                'country': weather_data['sys']['country'],
                'temperature': weather_data['main']['temp'],
                'weather': weather_data['weather'][0]['description']
            }

    return render_template_string(HTML_TEMPLATE, weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
