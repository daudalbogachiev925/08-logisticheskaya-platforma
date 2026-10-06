import math
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def build_distance_matrix(points):
    n = len(points)
    return [[int(distance(points[i], points[j]) * 1000) for j in range(n)] for i in range(n)]

def solve_vrp(points, demands, vehicle_capacity, num_vehicles):
    """points[0] — склад. Возвращает маршруты."""
    manager = pywrapcp.RoutingIndexManager(len(points), num_vehicles, 0)
    routing = pywrapcp.RoutingModel(manager)

    dist = build_distance_matrix(points)
    def dist_cb(i, j): return dist[manager.IndexToNode(i)][manager.IndexToNode(j)]
    cb = routing.RegisterTransitCallback(dist_cb)
    routing.SetArcCostEvaluatorOfAllVehicles(cb)

    def demand_cb(i): return demands[manager.IndexToNode(i)]
    d_cb = routing.RegisterUnaryTransitCallback(demand_cb)
    routing.AddDimensionWithVehicleCapacity(d_cb, 0, [vehicle_capacity]*num_vehicles, True, 'Capacity')

    params = pywrapcp.DefaultRoutingSearchParameters()
    params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    params.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    params.time_limit.seconds = 10

    solution = routing.SolveWithParameters(params)
    if not solution: return None

    result = []
    for v in range(num_vehicles):
        idx = routing.Start(v)
        route = []
        while not routing.IsEnd(idx):
            route.append(manager.IndexToNode(idx))
            idx = solution.Value(routing.NextVar(idx))
        route.append(manager.IndexToNode(idx))
        result.append(route)
    return result
