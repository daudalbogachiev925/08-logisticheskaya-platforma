SELECT
    COUNT(DISTINCT r.id) AS routes,
    COUNT(DISTINCT r.vehicle_id) AS vehicles_used,
    SUM(r.total_km) AS km,
    SUM(r.cost) AS total_cost,
    AVG(r.cost) AS avg_cost
FROM routes r
WHERE r.created >= NOW() - INTERVAL '30 days';
