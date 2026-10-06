# VRP (Vehicle Routing Problem)

Дано: N клиентов, K машин, ёмкости, координаты.
Цель: минимизировать суммарную длину маршрута.

Методы:
- Nearest Neighbor — быстро, ~20% от оптимума
- Genetic — точнее, минуты на 100 точек
- OR-Tools — оптимум, секунды, используется в проде

Схема: POST /optimize/{warehouse_id}?num_vehicles=3
