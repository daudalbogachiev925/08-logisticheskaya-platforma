from algorithms.nearest_neighbor import nearest_neighbor

def test_nn_returns_single_route():
    points = [(0,0),(1,0),(1,1),(0,1)]
    route = nearest_neighbor(points)
    assert route[0] == 0
    assert set(route) == {0,1,2,3}
