CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6)
);

CREATE TABLE clients (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6),
    demand NUMERIC(10,2) DEFAULT 0
);

CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    plate TEXT UNIQUE,
    capacity NUMERIC(10,2),
    cost_per_km NUMERIC(10,2),
    base_fee NUMERIC(10,2),
    driver TEXT,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE routes (
    id BIGSERIAL PRIMARY KEY,
    vehicle_id INT REFERENCES vehicles(id),
    warehouse_id INT REFERENCES warehouses(id),
    created TIMESTAMP DEFAULT NOW(),
    total_km NUMERIC(10,2),
    cost NUMERIC(10,2),
    status TEXT DEFAULT 'planned'
);

CREATE TABLE route_points (
    route_id BIGINT REFERENCES routes(id) ON DELETE CASCADE,
    seq INT NOT NULL,
    client_id BIGINT REFERENCES clients(id),
    arrived_at TIMESTAMP,
    PRIMARY KEY (route_id, seq)
);

CREATE INDEX idx_clients_latlon ON clients(lat, lon);
CREATE INDEX idx_routes_vehicle ON routes(vehicle_id);
