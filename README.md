## WeatherApp

A simple Django-based weather application that allows users to search for real-time weather information by city.

### Features

- Search weather details by city name.
- Display current temperature, weather condition, and humidity.
- Fetch real-time data using the OpenWeatherMap API.
  
### Tech Stack

- Backend: Django
- API Integration: OpenWeatherMap API

## Setup Instructions

1. Clone the Repository


```
git clone https://github.com/your-username/weatherapp.git
cd weatherapp

```

2. Create a Virtual Environment


```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

```
3. Install Dependencies


```
pip install -r requirements.txt

```
4. Set Up Environment Variables
 
- Create a .env file in the project root:
  

```
API_KEY=your_openweather_api_key

```
- Replace your_openweather_api_key with your OpenWeatherMap API key.
  
5. Run Migrations


```
python manage.py makemigrations
python manage.py migrate

```
6. Run the Development Server

```
python manage.py runserver

```
7. Access the Application

Open your browser and visit: `http://127.0.0.1:8000/weather/`