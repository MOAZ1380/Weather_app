from db import SessionLocal, Weather_data
from datetime import datetime

def add_weather_data_to_db(city, temperature, description, weather_condition, wind_speed, wind_direction):
    db = SessionLocal()
    try:
        weather_entry = Weather_data(
            city_name=city,
            temperature=temperature,
            description=description,
            weather_condition=weather_condition,
            wind_speed=wind_speed,
            wind_direction=wind_direction
        )
        db.add(weather_entry)
        db.commit()
    finally:
        db.close()

def get_weather_data_from_db(city):
    db = SessionLocal()
    try:
        today = datetime.now().date()
        return db.query(Weather_data).filter(
            Weather_data.city_name == city,
            Weather_data.current_day == today
        ).first()
    finally:
        db.close()
