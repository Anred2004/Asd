def gorner_scheme(text): #вычисление полинома по схеме горнера (строка как полином)
    result = ord(text[0]) #символ
    base = 31 #x = 31
    for i in range(len(text) - 1):#идем по каждому символу строки
        result = result * base + ord(text[i + 1])# то что было до этого * 31 + код символа который стоит на след позиции
    return result

def calculate_hash(text): # вычисление хеш кода
    q = 2147483647
    return gorner_scheme(text) % q #вычисляю остаток от деления на q

def search_text(text, sub_text):
    base = 31
    q = 2147483647
    sub_hash = calculate_hash(sub_text) # вычисляем хеш код подстроки
    m = len(sub_text) #длина подстроки
    current_hash = calculate_hash(text[0:m])#вычисляем хеш код той части строки длина которой равна длине подстроки
    i = 0 #начинаем с нулевого индекса
    while True:
        if sub_hash == current_hash: #сравниваем хещ кода строки и подстроки
            if sub_text == text[i:i+m]: #сравниваем их по символьно
                return i
        if i + m >= len(text): #дошли до конца строки и ничего не нашли :( - выходим (None)
            break
        current_hash = ((current_hash - ord(text[i]) * base ** (m-1)) * base + ord(text[i + m])) % q
        i += 1  # увеличиваем индекс
    return None


pattern = input("Введите шаблон для поиска: ")


try:
    with open('input.txt', 'r') as f:
        text = f.readline()

    positions = search_text(text, pattern)
    if positions:
        print(f"Шаблон найден на позициях: {positions}")
    else:
        print("Шаблон не найден.")
except FileNotFoundError:
    print("Файл не найден. Пожалуйста, проверьте путь к файлу.")
