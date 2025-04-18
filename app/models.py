from datetime import datetime
from sqlalchemy import DateTime  # Правильный импорт

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    phone = Column(String)
    price_multiplier = Column(Float, default=1.0)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    description = Column(String)
    city_id = Column(Integer, nullable=False)
    # created_at = Column(DateTime, default=datetime.utcnow)



