from collections import deque
def dfs(graph, start):
    visited = set()
    components = []
    # обход соседей вершины
    def explore(vertex):
        visited.add(vertex) # добавляем текущую вершину в множество
        components[-1].append(vertex) # добавляем текущую вершину в последнюю компоненту связности
        for neighbour in range(len(graph[vertex])): # проходимся по соседям
            if graph[vertex][neighbour] == 1 and neighbour not in visited: # проверка соседа на непосещенную вершину
                explore(neighbour)
    for vertex in range(len(graph)):
        if vertex not in visited:
            components.append([]) # добавляем новую компаненту
            explore(vertex) 
    return components 
# чтение матрицы смежности
def read_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix
graph = read_adjacency_matrix('graph.txt')
components = dfs(graph, 0)
with open('output.txt', 'w') as f:
    for idx, component in enumerate(components):
        f.write(f'Component {idx + 1}: {component}\n')
