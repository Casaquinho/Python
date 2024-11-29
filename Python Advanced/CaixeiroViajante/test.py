def euclidean_nearest_neighbor_heuristic(n: int):
    unvisited = []
    tour = []
    xy = []
    for i in range(n):
        xy.append((random.randint(0,1000),random.randint(0,1000)))
        unvisited.append(i+1)
    
    while(unvisited):
        next = min(unvisited, key= lambda candidate: (xy[tour[-1]][0] - xy[candidate][0])**2 + (xy[tour[-1]][1] - xy[candidate][1])**2)
        tour.append(next)
        unvisited.remove(next)
    
    return tour