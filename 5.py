def read_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix


def write_components_to_file(file_path, components, graph):
    components = [x for x in components if len(x) != 1]
    with open(file_path, 'w') as f:
        f.write(str('Количество сильно связных компонент: ' + str(len(components))))
        f.write("\n")
        for i in range(len(components)):
            components[i] = [l + 1 for l in components[i]]
            f.write(str(components[i]))


# Функция для обхода графа в глубину и добавления вершин в стек
def dfs(matrix, node, visited, stack):
    visited[node] = True  # Помечаем вершину как посещенную
    for neighbor in range(len(matrix)):  # Для каждого индекса в матрице
        if matrix[node][neighbor] == 1:  # Если есть ребро между вершинами
            if not visited[neighbor]:  # Если сосед не посещен
                dfs(matrix, neighbor, visited, stack)  # Рекурсивно обходим его
    stack.append(node)  # Добавляем вершину в стек


# Функция для транспонирования матрицы смежности (переворачивания направления ребер)
def transpose(matrix):
    transposed = []  # Создаем пустой список для транспонированной матрицы
    for i in range(len(matrix)):  # Для каждого индекса в матрице
        row = []  # Создаем пустой список для строки
        for j in range(len(matrix)):  # Для каждого индекса в матрице
            row.append(matrix[j][i])  # Добавляем элемент из транспонированной позиции
        transposed.append(row)  # Добавляем строку в транспонированную матрицу
    return transposed  # Возвращаем транспонированную матрицу


# Функция для нахождения сильно связных компонент в транспонированном графе
def scc(transposed, node, visited, component):
    visited[node] = True  # Помечаем вершину как посещенную
    component.append(node)  # Добавляем вершину в компоненту
    for neighbor in range(len(transposed)):  # Для каждого индекса в матрице
        if transposed[node][neighbor] == 1:  # Если есть ребро между вершинами
            if not visited[neighbor]:  # Если сосед не посещен
                scc(transposed, neighbor, visited, component)  # Рекурсивно обходим его


# Функция для реализации алгоритма Косарайю
def kosaraju(matrix):
    stack = []  # Создаем пустой стек для хранения порядка обхода вершин
    visited = [False] * len(matrix)  # Создаем список для хранения состояния посещения вершин и заполняем его False
    for node in range(len(matrix)):  # Для каждого индекса в матрице
        if not visited[node]:  # Если вершина не посещена
            dfs(matrix, node, visited, stack)  # Обходим ее в глубину и добавляем в стек
    transposed = transpose(matrix)  # Транспонируем матрицу смежности
    visited = [False] * len(transposed)  # Очищаем список посещения вершин и заполняем его False
    components = []  # Создаем пустой список для хранения сильно связных компонент
    while stack:  # Пока стек не пуст
        node = stack.pop()  # Извлекаем вершину из стека
        if not visited[node]:  # Если вершина не посещена
            component = []  # Создаем пустой список для хранения компоненты
            scc(transposed, node, visited, component)  # Находим компоненту в транспонированном графе
            components.append(component)  # Добавляем компоненту в список компонент
    return components  # Возвращаем список сильно связных компонент


# Читаем матрицу смежности из файла input.txt
matrix = read_adjacency_matrix("input.txt")
# Находим сильно связные компоненты графа
components = kosaraju(matrix)
# Записываем компоненты в файл output.txt
write_components_to_file("output.txt", components, matrix)
if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    adjacency_matrix = read_adjacency_matrix(input_file)
    # Получаем массив номеров компонент
    components = kosaraju(adjacency_matrix)
