
# 🌦️ Weather App Using API in Python

## 📌 Project Overview

This is a basic command-line Weather Application developed using Python. It uses the Open-Meteo API to fetch real-time weather information for a city entered by the user.

The application displays the city's temperature, humidity, and wind speed.

## 🎯 Objectives

- To understand the use of APIs in Python.
- To learn how to send HTTP requests using the `requests` library.
- To fetch and process JSON data.
- To display current weather information for a selected city.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Library:** Requests
- **API:** Open-Meteo Geocoding API
- **Weather API:** Open-Meteo Forecast API
- **Editor:** Visual Studio Code (VS Code)

## ⚙️ Features

- Accepts a city name from the user.
- Finds the city's latitude and longitude.
- Fetches current weather information.
- Displays:
  - Temperature in °C
  - Relative humidity in %
  - Wind speed in km/h
- Displays a message if the city is not found.

## 📂 Project Structure

```text
Weather-App/
│
├── weather.py
└── README.md
```

## 📋 Requirements

- Python 3 installed on your computer.
- An internet connection.
- The `requests` Python library.

## 📥 Installation

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

### Step 2: Install the Requests Library

Open the VS Code terminal or Command Prompt and run:

```bash
pip install requests
```

### Step 3: Download or Clone the Project

If you have uploaded the project to GitHub, run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, create a folder named `Weather-App` and save your Python code as `weather.py`.

## ▶️ How to Run

Open the project folder in VS Code and execute:

```bash
python weather.py
```

Enter a city name when prompted.

## 💻 Sample Output

```text
Enter city name: Patna

--- Weather Report ---
City: Patna
Temperature: 28.5 °C
Humidity: 65 %
Wind Speed: 12.4 km/h
```

*Note: The values above are examples. Actual weather data will vary.*

## 🔗 APIs Used

### 1. Open-Meteo Geocoding API

Endpoint:

https://geocoding-api.open-meteo.com/v1/search

**Purpose:** Finds the city's geographical coordinates using its name.

### 2. Open-Meteo Forecast API

Endpoint:

https://api.open-meteo.com/v1/forecast

**Purpose:** Retrieves current weather data using latitude and longitude.

## 🧠 How It Works

1. The user enters a city name.
2. The Geocoding API searches for the city.
3. The application extracts the latitude and longitude.
4. These coordinates are sent to the Forecast API.
5. The API returns weather data in JSON format.
6. Python extracts the temperature, humidity, and wind speed.
7. The application displays the weather report.

## 📚 Concepts Learned

- Python variables and input/output
- Dictionaries and lists
- Conditional statements (`if-else`)
- API requests using `requests.get()`
- URL parameters
- JSON data handling
- Accessing nested data using dictionary keys
- Working with external APIs

## 🚀 Future Improvements

- Add a graphical user interface using Tkinter.
- Display weather conditions and weather icons.
- Support multiple search results for cities with the same name.
- Add error handling for network failures and API errors.
- Show weather forecasts for upcoming days.
- Add a search history feature.

## 👨‍💻 Author

**Name:** Your Name

**Course:** Diploma in Computer Science and Engineering

**Project:** Weather App Using API in Python

## 📄 License

This project is intended for educational and learning purposes.
