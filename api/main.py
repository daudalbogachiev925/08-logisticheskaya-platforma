from fastapi import FastAPI
from routes import warehouses, clients, vehicles, routes, optimize

app = FastAPI(title="Logistics API")
app.include_router(warehouses.router, prefix="/warehouses", tags=["warehouses"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
app.include_router(routes.router, prefix="/routes", tags=["routes"])
app.include_router(optimize.router, prefix="/optimize", tags=["optimize"])

@app.get("/health")
def health(): return {"status": "ok"}
