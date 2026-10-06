import random

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

def route_length(points, route):
    return sum(distance(points[route[i]], points[route[i+1]]) for i in range(len(route)-1))

def mutate(route):
    a, b = sorted(random.sample(range(1, len(route)-1), 2))
    return route[:a] + route[a:b][::-1] + route[b:]

def genetic(points, generations=500, pop_size=100):
    n = len(points)
    pop = [ [0] + random.sample(range(1, n), n-1) + [0] for _ in range(pop_size)]
    for _ in range(generations):
        pop.sort(key=lambda r: route_length(points, r))
        pop = pop[:pop_size//2]
        new = []
        while len(new) < pop_size:
            child = mutate(random.choice(pop))
            new.append(child)
        pop = new
    pop.sort(key=lambda r: route_length(points, r))
    return pop[0]
