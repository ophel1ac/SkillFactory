# %%
# Сортировка выбором O(n^2)
def selection_sort(array: list) -> list:
    count = 0  # считаем количество проходов
    for i in range(len(array)):
        min_indx = i
        for j in range(i, len(array)):
            count += 1
            if array[j] < array[min_indx]:
                min_indx = j
        if i != min_indx:  # если индекс не совпадает с мин, меняем
            array[i], array[min_indx] = array[min_indx], array[i]
    return array, count


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(selection_sort(array))
# %%
# Cортировка выбором по убываыанию


def reverse_selection_sort(array: list) -> list:
    for i in range(len(array)):
        max_indx = i
        for j in range(i, len(array)):
            if array[j] > array[max_indx]:
                max_indx = j
        if i != max_indx:  # если индекс не совпадает с мин, меняем
            array[i], array[max_indx] = array[max_indx], array[i]
    return array


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(reverse_selection_sort(array))
# %%
# Сортировка пузырьком


def bubble_sort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(bubble_sort(array))
# %%
# Сортировка вставкой


def insert_sort(array: list) -> list:
    count = 0  # счетчик проходов
    for i in range(len(array)):
        current = array[i]
        indx = i
        while indx > 0 and array[indx - 1] > current:
            count += 1
            array[indx] = array[indx - 1]
            indx -= 1
        array[indx] = current
    return array, count


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(insert_sort(array))
# %%
# Сортировка слиянием O(n * log(n))


def merge_sort(array: list):  # разделяй
    if len(array) < 2:
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # рекурсивно делим правую часть
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # властвуй
    result = []
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(merge_sort(array))
# %%
# Быстрая сортировка


def qsort(array, left, right):
    middle = (left+right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

    return array
