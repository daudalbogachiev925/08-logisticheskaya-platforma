from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/")
def list_routes(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/route_cost.sql').read())).fetchall()]

@router.get("/{route_id}/points")
def points(route_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT rp.seq, c.name, c.lat, c.lon, rp.arrived_at
        FROM route_points rp JOIN clients c ON c.id = rp.client_id
        WHERE rp.route_id = :r ORDER BY rp.seq
    """), {"r": route_id}).fetchall()]
