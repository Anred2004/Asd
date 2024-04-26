from collections import deque
# Функция для обхода графа в ширину 
def bfs(graph, start):
    # Множество посещенных вершин
    visited = set()
    # Словарь расстояний до каждой вершины
    distance = {vertex: float('inf') for vertex in range(len(graph))}
    # Расстояние до стартовой вершины равно 0
    distance[start] = 0
    # Очередь для обхода вершин в BFS
    queue = deque([start])
    # Добавляем стартовую вершину в множество посещенных
    visited.add(start)

    # Цикл выполняется, пока очередь не пуста
    while queue:
        # Извлекаем вершину из начала очереди
        vertex = queue.popleft()

        # Проверяем всех соседей текущей вершины
        for neighbour in range(len(graph)):
            # Если есть ребро между текущей вершиной и соседом и сосед еще не посещен
            if graph[vertex][neighbour] == 1 and distance[neighbour] == float('inf'):
                # Добавляем соседа в множество посещенных
                visited.add(neighbour)
                # Расстояние до соседа равно расстоянию до текущей вершины плюс 1
                distance[neighbour] = distance[vertex] + 1
                # Добавляем соседа в очередь для дальнейшего обхода
                queue.append(neighbour)
    # Возвращаем словарь с кратчайшими расстояниями до каждой вершины от стартовой вершины
    return distance

# Функция для чтения матрицы смежности из файла
def read_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

graph = read_adjacency_matrix('graph.txt')
with open('output.txt', 'w') as f:
    for vertex, dist in bfs(graph, 0).items():
        f.write(f'{vertex}: {dist}\n')
