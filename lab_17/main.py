def best_fit():

    objects = input("Введите размеры объектов, разделенные пробелом: ").split()
    objects = [int(obj) for obj in objects]
    box_size = int(input("Введите размер ящика: "))

    boxes = []  # Список для хранения заполненности каждого ящика
    box_contents = []  # Список для хранения содержимого каждого ящика

    # Цикл для перебора объектов в списке objects
    for obj in objects:

        # Индекс лучшей коробки приравнивается к -1, чтобы в случае отсутствия подходящей коробки его можно было найти
        best_box_index = -1
        # Минимальное оставшееся место в коробке устанавливается как бесконечность
        min_space_left = float('inf')

        # Цикл для перебора коробок с индексами
        for i, space_used in enumerate(boxes):
            # Вычисление оставшегося места в коробке
            space_left = box_size - space_used
            # Если объект помещается в коробку и оставшееся место меньше чем минимальное, то обновляем лучшую коробку и минимальное оставшееся место
            if obj <= space_left < min_space_left:
                best_box_index = i
                min_space_left = space_left


        # Если была найдена подходящая коробка, то добавляем объект в неё
        if best_box_index != -1:
            boxes[best_box_index] += obj
            box_contents[best_box_index].append(obj)
        # Иначе создаем новую коробку и добавляем в неё объект
        else:
            boxes.append(obj)
            box_contents.append([obj])

    print("\nРезультат распределения объектов по ящикам:")
    for i, contents in enumerate(box_contents):
        print(f"Ящик {i + 1}: {contents} (Заполнено {boxes[i]} из {box_size})")
    print(f"Общее количество использованных ящиков: {len(boxes)}")


best_fit()
