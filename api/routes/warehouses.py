from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class WIn(BaseModel):
    name: str
    address: str | None = None
    lat: float
    lon: float

@router.post("/")
def create(data: WIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO warehouses (name, address, lat, lon) VALUES (:name,:address,:lat,:lon)
        RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM warehouses")).fetchall()]
