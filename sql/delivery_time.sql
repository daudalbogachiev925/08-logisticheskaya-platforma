SELECT r.id, rp.seq, c.name,
       rp.arrived_at,
       rp.arrived_at - LAG(rp.arrived_at) OVER (PARTITION BY r.id ORDER BY rp.seq) AS delta
FROM routes r
JOIN route_points rp ON rp.route_id = r.id
JOIN clients c ON c.id = rp.client_id
ORDER BY r.id, rp.seq;
