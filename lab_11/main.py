# Функция для создания конечного автомата из строки поиска
def create_automaton(pattern):
    # Алфавит символов в строке поиска
    alphabet = list(set(pattern))
    # Длина строки поиска
    m = len(pattern)
    # Количество состояний автомата
    n = m + 1
    # Словарь для хранения переходов автомата
    transitions = {}
    # Цикл по всем состояниям
    for i in range(n):
        # Цикл по всем символам алфавита
        for a in alphabet:
            # Вычисление следующего состояния с помощью функции next
            k = next((j for j in range(min(m, i + 1), 0, -1) if pattern[j - 1] == a), 0)
            # Добавление перехода в словарь
            transitions[(i, a)] = k
        # Добавление перехода для любого другого символа в нулевое состояние
        transitions[(i, None)] = 0
    # Возвращение конечного автомата
    return transitions

# Функция для поиска всех вхождений строки поиска в исходной строке с помощью конечного автомата
def search(pattern, text):
    # Создание конечного автомата из строки поиска
    automaton = create_automaton(pattern)
    # Длина строки поиска
    m = len(pattern)
    # Текущее состояние автомата
    state = 0
    # Список для хранения индексов вхождений
    matches = []
    # Цикл по всем символам исходной строки
    for i in range(len(text)):
        # Обновление состояния автомата с учетом текущего символа
        state = automaton.get((state, text[i]), automaton[(state, None)])
        # Проверка, достигнуто ли конечное состояние
        if state == m:
            # Добавление индекса вхождения в список
            matches.append(i - m + 1)
    # Возвращение списка индексов вхождений
    return matches

with open("input.txt", "r") as file:
    # Чтение исходной строки из файла
    text = file.read()
pattern = input("Введите строку поиска: ")
# Проверка, не пустая ли строка поиска
if pattern:
    # Поиск всех вхождений строки поиска в исходной строке с помощью конечного автомата
    matches = search(pattern, text)
    if matches:
        print("Строка поиска найдена в исходной строке на следующих позициях:")
        print(*matches) # Использование распаковки списка для вывода каждого индекса на отдельной строке
    else:
        print("Строка поиска не найдена в исходной строке.")
else:
    print("Строка поиска не может быть пустой.")
