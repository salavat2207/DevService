from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas, telegram_bot
from pydantic import BaseModel, Field, validator
import re

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/Форма обратной свзяи")
async def send_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = models.Feedback(**feedback.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)


    message = f"Новая заявка:\nИмя: {feedback.name}\nТелефон: {feedback.phone}\nОписание: {feedback.description}\nГород ID: {feedback.city_id}"
    await telegram_bot.send_telegram_message(message)
    return {"message": "Заявка отправлена"}


@router.get("/Город")
async def get_cities(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    return cities




