SELECT v.plate, v.capacity,
       COALESCE(SUM(c.demand),0) AS total_demand,
       ROUND(100.0 * COALESCE(SUM(c.demand),0) / v.capacity, 1) AS load_pct
FROM vehicles v
LEFT JOIN routes r ON r.vehicle_id = v.id
LEFT JOIN route_points rp ON rp.route_id = r.id
LEFT JOIN clients c ON c.id = rp.client_id
GROUP BY v.id
ORDER BY load_pct DESC;
