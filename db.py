from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///weather.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Weather_data(Base):
    __tablename__ = 'Weather'

    id = Column(Integer, primary_key=True)
    city_name = Column(String(50), nullable=False)
    temperature = Column(Float, nullable=False)
    description = Column(String(100), nullable=False)
    weather_condition = Column(String(50), nullable=False)
    wind_speed = Column(Float, nullable=False)
    wind_direction = Column(Float, nullable=False)
    current_day = Column(Date, default=datetime.now().date()) 

    def __init__(self, city_name, temperature, description, weather_condition, wind_speed, wind_direction):
        self.city_name = city_name
        self.temperature = temperature
        self.description = description
        self.weather_condition = weather_condition
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.current_day = datetime.now().date() 

Base.metadata.create_all(engine)
