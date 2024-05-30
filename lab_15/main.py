# Функция для нахождения степени каждой вершины
def degree(G):
    n = len(G) # количество вершин
    deg = [0] * n # список для хранения степеней
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1: # если есть ребро между i и j
                deg[i] += 1 # увеличить степень i на 1
    print(deg)
    return deg

# Функция для сортировки вершин по убыванию степеней
def sort_by_degree(G):
    n = len(G) # количество вершин
    deg = degree(G) # список степеней
    order = list(range(n)) # список вершин
    # Сортировка пузырьком по убыванию степеней
    for i in range(n-1):
        for j in range(i+1, n):
            if deg[order[i]] < deg[order[j]]:
                order[i], order[j] = order[j], order[i]
    print(order)
    return order

# Функция для проверки, смежна ли вершина с букетом
def is_adjacent(G, v, B):
    for u in B:
        if G[v][u] == 1: # если есть ребро между v и u
            return True # вершина смежна с букетом
    return False # вершина не смежна с букетом

# Функция для жадной раскраски графа
def greedy_coloring(G):
    n = len(G) # количество вершин
    order = sort_by_degree(G) # порядок вершин по убыванию степеней
    color = [-1] * n # список для хранения цветов вершин
    k = 0 # счетчик цветов
    while -1 in color: # пока есть неокрашенные вершины
        k += 1 # увеличить счетчик на 1
        B = [] # создать пустой букет
        for v in order: # пройти по всем вершинам в порядке
            if color[v] == -1: # если вершина не окрашена
                if not is_adjacent(G, v, B): # если она не смежна с букетом
                    color[v] = k # окрасить ее в цвет k
                    B.append(v) # добавить ее в букет
    return color # вернуть список цветов

# Функция для чтения матрицы смежности из файла
def read_graph(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

# Чтение матрицы смежности из файла
file_name = "input.txt"
G = read_graph(file_name)

# Вызов функции жадной раскраски и вывод результата
color = greedy_coloring(G)
print("Цвета вершин:")
for i in range(len(color)):
    print(f"Вершина {i}: {color[i]}")
