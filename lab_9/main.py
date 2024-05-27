# алгоритм Беллмана-Форда  Функция для чтения графа из файла
def read_graph(filename):
    # Открываем файл для чтения
    with open(filename, "r") as f:
        # Читаем количество вершин
        n = int(f.readline())
        # Создаем пустой список смежности
        adj = [[] for _ in range(n)]
        # Читаем матрицу смежности построчно
        for i in range(n):
            # Преобразуем строку в список целых чисел
            row = list(map(int, f.readline().split()))
            # Для каждого элемента строки
            for j in range(n):
                # Если элемент не равен нулю
                if row[j] != 0:
                    # Добавляем ребро (i, j) с весом row[j]
                    adj[i].append((j, row[j]))
    # Возвращаем граф в виде списка смежности
    return adj

# Функция для реализации алгоритма Беллмана-Форда
def bellman_ford(adj, s):
    # Получаем количество вершин графа
    n = len(adj)
    # Инициализируем массив расстояний до бесконечности
    dist = [float("inf")] * n
    # Инициализируем массив предков пустыми значениями
    prev = [None] * n
    # Устанавливаем расстояние от начальной вершины до себя равным нулю
    dist[s] = 0
    # Повторяем n - 1 раз
    for _ in range(n - 1):
        # Для каждого ребра (u, v) с весом w в графе
        for u in range(n):
            for v, w in adj[u]:
                # Если расстояние до u + вес ребра меньше текущего расстояния до v
                if dist[u] + w < dist[v]:
                    # Обновляем расстояние до v и предка v
                    dist[v] = dist[u] + w
                    prev[v] = u
    # Проверяем наличие отрицательных циклов
    for u in range(n):
        for v, w in adj[u]:
            # Если расстояние до u + вес ребра меньше текущего расстояния до v
            if dist[u] + w < dist[v]:
                # Возвращаем False и сообщение об ошибке
                return False, "Граф содержит отрицательный цикл"
    # Возвращаем True и массивы расстояний и предков
    return True, dist, prev

# Функция для вывода кратчайших путей из начальной вершины в файл
def print_paths(filename, s, dist, prev):
    # Открываем файл для записи
    with open(filename, "w") as f:
        # Для каждой вершины графа
        for v in range(len(dist)):
            # Если вершина не является начальной
            if v != s:
                # Если расстояние до нее конечно
                if dist[v] != float("inf"):
                    # Выводим расстояние и путь до нее в файл без индексов (нумерация с единицы)
                    f.write(f"Расстояние от {s + 1} до {v + 1} равно {dist[v]}\n")
                    f.write(f"Путь от {s + 1} до {v + 1}: ")
                    path = []
                    cur = v
                    while cur is not None:
                        path.append(cur + 1)
                        cur = prev[cur]
                    path.reverse()
                    f.write(" -> ".join(map(str, path)) + "\n")
                else:
                    # Выводим сообщение о недостижимости вершины в файл без индексов (нумерация с единицы)
                    f.write(f"Вершина {v + 1} недостижима из {s + 1}\n")

# Главная функция программы
def main():
    # Читаем граф из файла input.txt
    adj = read_graph("input.txt")
    # Задаем начальную вершину s (нумерация с нуля)
    s = 0
    # Выполняем алгоритм Беллмана-Форда для графа и начальной вершины s
    result = bellman_ford(adj, s)
    # Если алгоритм успешно завершился
    if result[0]:
        # Выводим кратчайшие пути в файл output.txt без индексов (нумерация с единицы)
        print_paths("output.txt", s, result[1], result[2])
        print("Кратчайшие пути успешно выведены в файл output.txt")
    else:
        # Выводим сообщение об ошибке в консоль
        print(result[1])

# Вызываем главную функцию программы
if __name__ == "__main__":
    main()
