def dijkstra(graph, start_vertex):
    dist = {v: float('infinity') for v in graph}
    dist[start_vertex] = 0

    unvisited = list(graph.keys())
    while unvisited:
        curr_vertex = min(unvisited, key=dist.get)
        for neighbour, distance in graph[curr_vertex].items():
            old_distance = dist[neighbour]
            new_distance = dist[curr_vertex] + distance
            dist[neighbour] = min(old_distance, new_distance)

        unvisited.remove(curr_vertex)

    return dist


graph = {
    '0': {'1': 16, '4': 15, '5': 15},
    '1': {'4': 13, '5': 13, '6': 14},
    '2': {'6': 15},
    '3': {},
    '4': {'3': 10},
    '5': {'2': 15, '7': 14},
    '6': {'0': 12, '3': 15, '4': 19, '7': 11},
    '7': {'1': 19, '4': 19}
}

list_vertex = list('01234567')

for vert in list_vertex:
    print("Vertex:", vert)
    print(dijkstra(graph, vert))

