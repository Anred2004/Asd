# Считываем матрицу смежности из файла
def read_adjacency_matrix(file_name):
    adjacency_matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            adjacency_matrix.append(row)
    return adjacency_matrix

# Алгоритм Дейкстры
def dijkstra(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start_vertex] = 0
    
    for _ in range(n):
        min_distance = float('inf')
        min_vertex = -1
        for v in range(n):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
        
        visited[min_vertex] = True
        for v in range(n):
            if graph[min_vertex][v] > 0 and distance[min_vertex] + graph[min_vertex][v] < distance[v]:
                distance[v] = distance[min_vertex] + graph[min_vertex][v]
    
    return distance

# Пример использования
file_name = 'input.txt'
graph = read_adjacency_matrix(file_name)
start_vertex = 0
shortest_paths = dijkstra(graph, start_vertex)
print("Кратчайшие пути из вершины", start_vertex)
for i, dist in enumerate(shortest_paths):
    print("До вершины", i, "расстояние:", dist)
