def incidence_to_adjacency(incidence_matrix):
    num_vertices = len(incidence_matrix)
    num_edges = len(incidence_matrix[0])

    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for edge_idx in range(num_edges):
        start_vertex = None
        end_vertex = None
        for vertex_idx in range(num_vertices):
            if incidence_matrix[vertex_idx][edge_idx] == 1:
                start_vertex = vertex_idx
            elif incidence_matrix[vertex_idx][edge_idx] == -1:
                end_vertex = vertex_idx

        if start_vertex is not None and end_vertex is not None:
                adjacency_matrix[start_vertex][end_vertex] = 1


    return adjacency_matrix


# матрица инцидентности
incidence_matrix = [[1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
                    [-1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
                    [0, -1, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, -1, 0],
                    [0, 0, -1, 0, 0, -1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, -1],
                    [0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 1, 1]]

print("Матрица инцидентности:")
for row in incidence_matrix:
    print(row)

# перевод матрицы инцидентности в матрицу смежности
adjacency_matrix = incidence_to_adjacency(incidence_matrix)

# вывод
print("\nМатрица смежности:")
for row in adjacency_matrix:
    print(row)
