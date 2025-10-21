# 🌦 Advanced Weather Application

An **Advanced Weather Web Application** built with **Django** and **Bootstrap** that allows users to search for cities and view **real-time weather information** and a **5-day forecast** using the OpenWeatherMap API.

---

## 🖼️ Overview

This project provides current weather details such as temperature, humidity, wind speed, and atmospheric pressure.  
It also includes a responsive user interface powered by **Bootstrap 5**, with dynamic weather icons and forecast cards.

---

## 🚀 Features

✅ Search for any city worldwide  
✅ Real-time temperature, humidity, and pressure readings  
✅ 5-day weather forecast display  
✅ Dynamic background and icons based on weather conditions  
✅ Responsive Bootstrap 5 design  
✅ Easy-to-extend Django backend structure

---

## 🧰 Tech Stack

| Layer        | Technology                                           |
| ------------ | ---------------------------------------------------- |
| Backend      | Django 5.x                                           |
| Frontend     | HTML5, CSS3, Bootstrap 5                             |
| API          | [OpenWeatherMap API](https://openweathermap.org/api) |
| Environment  | Python 3.11+                                         |
| Dependencies | `requests`, `python-decouple`                        |

---

## 📁 Project Structure

weather_app/
├── manage.py
├── weather/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── main/
│ ├── init.py
│ ├── views.py
│ ├── urls.py
│ ├── utils.py
│ ├── templates/
│ │ └── main/
│ │ └── index.html
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ └── ...
│
└── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/advanced-weather-app.git
cd advanced-weather-app

2️⃣ Create and activate a virtual environment
python3 -m venv myvenv
source myvenv/bin/activate   # On Windows: myvenv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Get an OpenWeatherMap API key

Create a free account at https://openweathermap.org/api
 and get your API key.

Create a .env file in the project root:

OPENWEATHER_API_KEY=your_api_key_here in your .env file

5️⃣ Run migrations
python manage.py migrate

6️⃣ Run the development server
python manage.py runserver
```
