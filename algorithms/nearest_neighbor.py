import math

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def nearest_neighbor(points, start=0):
    unvisited = set(range(len(points)))
    path = [start]
    unvisited.discard(start)
    while unvisited:
        last = points[path[-1]]
        nxt = min(unvisited, key=lambda i: distance(last, points[i]))
        path.append(nxt)
        unvisited.discard(nxt)
    return path
