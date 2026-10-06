from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class CIn(BaseModel):
    name: str
    address: str | None = None
    lat: float
    lon: float
    demand: float = 0

@router.post("/")
def create(data: CIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO clients (name, address, lat, lon, demand)
        VALUES (:name,:address,:lat,:lon,:demand) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM clients")).fetchall()]
