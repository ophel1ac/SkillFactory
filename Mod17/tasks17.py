# %%
from math import log2

n = 10000
func = (n ** 2) / (n * log2(n))
print(round(func, 0))
print(log2(n))
# %%
# 17.4.5
# Функция проверки баланса скобок: круглых и квадратных.


def par_check(s: str) -> bool:
    bracket = {")": "(", "]": "["}
    stack = []
    for i in s:
        if i in "([":
            stack.append(i)
        elif i in ")]":
            if len(stack) > 0 and stack[-1] == bracket[i]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_check("(((())))[[[]]][()]"))

# %%
# Реализация очереди через массив


def is_empty() -> bool:
    return head == tail and queue[head] == 0


def size() -> int:
    if is_empty():
        return 0
    elif head == tail:  # Очередь не пуста, но указатели совпадают
        return n_max
    elif head > tail:  # Хвост очереди сместился в начало
        return n_max - head + tail
    else:  # Хвост правеее начала
        return tail - head


def add():
    global order, tail
    order += 1
    queue[tail] = order
    print(f"Задача №{queue[tail]} добавлена")
    tail = (tail + 1) % n_max


def show():
    print(f"Задача №{queue[head]} в приоритете")


def do():
    global head
    print(f"Задача №{queue[head]} выполнена")
    queue[head] = 0
    head = (head + 1) % n_max


n_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(n_max)]  # список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != n_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")


# %%
graph = {"Адмиралтейская":
            {"Садовая": 4},
         "Садовая":
            {"Сенная площадь": 3,
             "Спасская": 3,
             "Адмиралтейская": 4,
             "Звенигородская": 5},
         "Сенная площадь":
            {"Садовая": 3,
             "Спасская": 3},
         "Спасская":
            {"Садовая": 3,
             "Сенная площадь": 3,
             "Достоевская": 4},
         "Звенигородская":
            {"Пушкинская": 3,
             "Садовая": 5},
         "Пушкинская":
            {"Звенигородская": 3,
             "Владимирская": 4},
         "Владимирская":
            {"Достоевская": 3,
             "Пушкинская": 4},
         "Достоевская":
            {"Владимирская": 3,
             "Спасская": 4}}

# %%
# Алгоритм Дейкстры
# Нахождение кратчайшего пути
distance = {k: 100 for k in graph.keys()}  # словарь расстояний
distance["Адмиралтейская"] = 0  # стартовая вершина
check = {k: False for k in graph.keys()}  # bool, что вершина просмотрена

for _ in range(len(distance)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in check.keys() if not check[k]],
                key=lambda x: distance[x])

    for v in graph[min_k].keys():  # проходимся по всем смежным вершинам
        # минимум
        distance[v] = min(distance[v], distance[min_k] + graph[min_k][v])
    check[min_k] = True  # просмотренную вершину помечаем

print(distance)

# %%
# 17.5.3
# Нахождение вершин минимального пути

path = {k: None for k in graph.keys()}  # предки с минимальным расстоянием
distance = {k: 100 for k in graph.keys()}  # словарь расстояний
distance["Адмиралтейская"] = 0  # стартовая вершина
check = {k: False for k in graph.keys()}  # bool, что вершина просмотрена

for _ in range(len(distance)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in check.keys() if not check[k]],
                key=lambda x: distance[x])

    for v in graph[min_k].keys():  # проходимся по всем смежным вершинам
        # если расстояние от текущей вершины меньше
        if distance[v] > distance[min_k] + graph[min_k][v]:
            distance[v] = distance[min_k] + graph[min_k][v]  # фиксируем его
            path[v] = min_k  # записываем как предка
    check[min_k] = True  # просмотренную вершину помечаем

print(path)

# %%
# вывод пути, но в обратном порядке
pointer = "Владимирская"  # куда должны прийти
while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = path[pointer]


# %%
# Реализация бинарного дерева

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    # префиксный обход в глубину
    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:
            self.left_child.pre_order()  # рекурсивно вызываем функц

        if self.right_child is not None:
            self.right_child.pre_order()  # рекурсивно вызываем функц

    # постфиксный обход в глубину
    def post_order(self):
        if self.left_child is not None:
            self.left_child.post_order()

        if self.right_child is not None:
            self.right_child.post_order()

        print(self.value)

    # индексный обход
    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию
# %%
# 17.5.5


root_node = BinaryTree(2).insert_left(7).insert_right(5)
node_7 = root_node.left_child.insert_left(2).insert_right(6)
node_5 = root_node.right_child.insert_right(9)
node_6 = node_7.right_child.insert_left(5).insert_right(11)
node_9 = node_5.right_child.insert_left(4)


# %%
root_node.pre_order()
# %%
root_node.post_order()


# %%
# Реализация связного списка
class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def push_left(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def push_right(self, value):
        if self.last is None:
            self.last = Node(value)
            self.first = self.first
        else:
            new_node = Node(value, self.last)
            self.last = new_node

    def pop_left(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # в списке только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def pop_right(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # в списке только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель

            # пока не найдем предпоследний
            while pointer.next is not node and pointer.next is not None:
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный


# %%
LL = LinkedList()

LL.push_right(1)
LL.push_left(2)
LL.push_right(3)
LL.pop_right()
LL.push_left(4)
LL.push_right(5)
LL.pop_left()

print(LL)
