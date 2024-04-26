from collections import deque
def bfs(graph, start, component_count): #Объявляем функцию которая принимает граф, стартовую вершину и счетчик компонент
    visited = set()#Создаем множество visited для отслеживания посещенных вершин.
    components = [] #список для хранения компонент связности
    for v in range(len(graph)):
        if v not in visited:
            component = set() #множество для хранения вершин текущей компоненты
            queue = deque([v]) #очередь queue с начальной вершиной v
            visited.add(v)
            component.add(v)#Добавляем вершину в текущую компоненту
            while queue:
                vertex = queue.popleft() #Извлекаем вершину из очереди
                for neighbour in range(len(graph)): #проходимся по соседям текущей вершины
                    if graph[vertex][neighbour] == 1 and neighbour not in visited:
                        visited.add(neighbour)
                        component.add(neighbour)#добавляем соседа в текущую компоненту
                        queue.append(neighbour) #добавляем соседа в очередь для дальнейшего обхода
            components.append(component)#Добавляем текущую компоненту в список компонент
            component_count += 1
    return components, component_count

def read_adjacency_matrix(file_path): #чтение матрицы смежности
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

graph = read_adjacency_matrix('graph.txt')
component_count = 0
components, component_count = bfs(graph, 0, component_count)

with open('output.txt', 'w') as f:
    f.write(f'Number of connected components: {component_count}\n')
    for idx, component in enumerate(components):
        f.write(f'Component {idx + 1}: {component}\n')
