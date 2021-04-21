class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None



try:
    array = [int(i) for i in input("Введите числа через пробел").split()]
    n = int(input("Введите число"))
except TypeError:
    print("Введенные числа должны быть целыми")
