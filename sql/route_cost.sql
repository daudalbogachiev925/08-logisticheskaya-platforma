SELECT r.id, v.plate, w.name AS warehouse,
       r.total_km, r.cost,
       (SELECT COUNT(*) FROM route_points rp WHERE rp.route_id = r.id) AS points
FROM routes r
JOIN vehicles v ON v.id = r.vehicle_id
JOIN warehouses w ON w.id = r.warehouse_id
ORDER BY r.created DESC;
