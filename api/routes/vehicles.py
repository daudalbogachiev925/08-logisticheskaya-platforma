from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class VIn(BaseModel):
    plate: str
    capacity: float
    cost_per_km: float
    base_fee: float
    driver: str | None = None

@router.post("/")
def create(data: VIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO vehicles (plate, capacity, cost_per_km, base_fee, driver)
        VALUES (:plate,:capacity,:cost_per_km,:base_fee,:driver) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM vehicles WHERE active")).fetchall()]
