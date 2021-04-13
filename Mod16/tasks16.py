# %%
# 16.9.1
class Rectangle:
    def __init__(self, a, b, width, height):
        self.a = a
        self.b = b
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle{self.a, self.b, self.width, self.height}"

r = Rectangle(5, 10, 50, 100)
print(r)

# %%
#16.9.3
class Payment:
    def __init__(self, name:str, balance:int=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Клиент \"{self.name}\". Баланс: {self.balance}"

    def __add__(self, other):
        self.balance += other
    
    def __sub__(self, other):
        self.balance -= other


# %%
# 16.9.4
class Volunteer:
    def __init__(self, name:str, post:str="Волонтер"):
        self.name = name
        self.post = post

    def __str__(self):
        return f"Volunteer {self.name, self.post}"


class Event(Volunteer):
    participants = []

    def __init__(self, name:str, location:str, post:str="Волонтер"):
        super().__init__(name, post)
        self.location = location

    def __str__(self):
        return f"{self.name}, г.{self.location}, статус {self.post}"
    
    def go_to_event(self):
        Event.participants.append(self.__str__())


r1 = Event("Петя", "Москва", "Наставник")
r2 = Event("Ваня", "Москва", "Наставник")
r3 = Event("Маша", "Москва", "Наставник")


r1.go_to_event()
r2.go_to_event()
r3.go_to_event()

print(Event.participants)


# %%
# 16.10.5 Exceptions
class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException("Введенная сторона меньше или равна нулю")
        else:
            self.a = a
