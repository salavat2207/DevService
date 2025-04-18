from database import SessionLocal
from models import City

db = SessionLocal()

db.add_all([
    City(name="Челябинск", phone="+7 495 000 00 00", price_multiplier=1.0),
    City(name="Екатеринбург", phone="+7 843 000 00 00", price_multiplier=0.9),
    City(name="Магнитогорск", phone="+7 351 000 00 00", price_multiplier=0.8),
])
db.commit()
db.close()