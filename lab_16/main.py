# Задача о рюкзаке: дано N предметов с весами w[i] и ценностями v[i], и максимальная вместимость рюкзака W. Найти подмножество предметов, которые можно уложить в рюкзак так, чтобы суммарная ценность была максимальной.

# Инициализация таблицы динамического программирования
    # Создаём таблицу с размерами (n+1) x (capacity+1), заполненную нулями.
    # +1 в размерах таблицы, чтобы учесть случай с нулевыми индексами (без предметов и без вместимости).

# Функция для нахождения максимальной ценности и элементов в рюкзаке
def knapsack(W, w, v, n):
  # Создаем двумерный массив K размером (n+1) x (W+1) для хранения оптимальных значений
  K = [[0 for x in range(W + 1)] for x in range(n + 1)]

  # Заполняем массив K по строкам и столбцам
  for i in range(n + 1):
    for j in range(W + 1):
      # Если i-й предмет не входит в рюкзак или его нет, то значение равно предыдущему
      if i == 0 or j == 0:
        K[i][j] = 0
      elif w[i - 1] <= j:
        # Если i-й предмет входит в рюкзак, то выбираем максимум из двух вариантов: взять его или не взять
        K[i][j] = max( K[i - 1][j], v[i - 1] + K[i - 1][j - w[i - 1]])# берем, то добавляем его к ценность к макс ценности набора на незанятый вес
      else:
        # Если i-й предмет не входит в рюкзак, то значение равно предыдущему
        K[i][j] = K[i - 1][j]

  # Возвращаем максимальную ценность и элементы в рюкзаке
  value = K[n][W] # Максимальная ценность
  items = [] # Список элементов в рюкзаке
  i = n # Индекс последнего предмета
  j = W # Оставшаяся вместимость рюкзака
  while i > 0 and j > 0:
    # Если значение в текущей ячейке отличается от предыдущего по строке, то i-й предмет был добавлен в рюкзак
    if K[i][j] != K[i - 1][j]:
      items.append(i) # Добавляем индекс предмета в список
      j = j - w[i - 1] # Уменьшаем оставшуюся вместимость на вес предмета
    i = i - 1 # Переходим к предыдущему предмету

  return value, items

# Пример использования функции
w = [10, 20, 30, 15, 20] # Веса предметов
v = [60, 100, 120, 150, 99999999999999] # Ценности предметов
W = 50 # Вместимость рюкзака
n = len(w) # Количество предметов
value, items = knapsack(W, w, v, n)
print("Максимальная ценность, которую можно уложить в рюкзак:", value)
print("Элементы в рюкзаке:", items)
