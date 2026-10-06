from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session
from algorithms.vrp import solve_vrp

router = APIRouter()

@router.post("/{warehouse_id}")
def optimize(warehouse_id: int, num_vehicles: int = 2, db: Session = Depends(get_session)):
    wh = db.execute(text("SELECT lat, lon FROM warehouses WHERE id=:i"), {"i": warehouse_id}).fetchone()
    clients = db.execute(text("SELECT id, lat, lon, demand FROM clients")).fetchall()

    points = [(float(wh[0]), float(wh[1]))]
    demands = [0]
    for c in clients:
        points.append((float(c[1]), float(c[2])))
        demands.append(int(c[3]))

    route = solve_vrp(points, demands, vehicle_capacity=500, num_vehicles=num_vehicles)
    return {"routes": route}
