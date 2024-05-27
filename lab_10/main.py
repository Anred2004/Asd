def is_eulerian_cycle(matrix):
    n = len(matrix)  # Количество вершин в графе
    for i in range(n):
        degree = sum(matrix[i][j] != 0 for j in range(n))
        if degree % 2 != 0:
            return False  # Найдена вершина с нечетной степенью

    # Проверка на связность графа
    visited = [False] * n
    dfs(matrix, 0, visited)
    if not all(visited):
        return False  # Граф несвязен

    return True  # Граф Эйлеров

# Функция для обхода графа в глубину
def dfs(matrix, vertex, visited):
    # Помечаем вершину как посещенную
    visited[vertex] = True
    # Перебираем соседние вершины
    for i in range(len(matrix)):
        if matrix[vertex][i] != 0 and not visited[i]:
            # Рекурсивно обходим соседнюю вершину
            dfs(matrix, i, visited)


def remove_edge(matrix, u, v):
    matrix[u][v] -= 1
    matrix[v][u] -= 1

# Функция для нахождения эйлерова цикла в графе
def find_eulerian_cycle(matrix):
    # Проверяем, является ли граф эйлеровым
    if not is_eulerian_cycle(matrix):
        return None
    # Количество вершин в графе
    n = len(matrix)
    # Список для хранения эйлерова цикла
    cycle = []
    # Стек для хранения текущего пути
    stack = [0]   # Начинаем с произвольной вершины (например, с нулевой)
    while stack:  # Пока стек не пуст
        u = stack[-1]  # Присваиваем переменной u значение последнего элемента в стеке
        has_edge = False  # Устанавливаем флаг наличия ребра в False
        for v in range(n):  # Перебираем все вершины графа
            if matrix[u][v] > 0:  # Если существует ребро между вершинами u и v
                stack.append(v)  # Добавляем вершину v в стек
                remove_edge(matrix, u, v)  # Удаляем ребро между вершинами u и v
                has_edge = True  # Устанавливаем флаг наличия ребра в True
                break  # Прерываем цикл
        if not has_edge:  # Если ребра не было найдено
            cycle.append(stack.pop())  # Удаляем вершину из стека и добавляем её в цикл

    return cycle  # Возвращаем цикл


def create_graph_from_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]
    return matrix


def write_eulerian_cycle_to_file(cycle, filename):
    with open(filename, 'w') as file:
        cycle_str = '->'.join(map(str, cycle))
        file.write("Эйлеров цикл:\n" + cycle_str + "\n")


input_filename = "input.txt"
output_filename = "output.txt"


matrix = create_graph_from_adjacency_matrix(input_filename)


eulerian_cycle = find_eulerian_cycle(matrix)


if eulerian_cycle is not None:
    print("Найден Эйлеров цикл:", eulerian_cycle)

    write_eulerian_cycle_to_file(eulerian_cycle, output_filename)
    print(f"Эйлеров цикл был записан в файл {output_filename}")
else:
    print("В данном графе Эйлеров цикл не найден.")
