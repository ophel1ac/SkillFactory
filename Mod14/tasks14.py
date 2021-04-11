# %%
def common_divisor(a, n) -> bool:
    return(a % n == 0)


print(common_divisor(9, 3))
print(common_divisor(9, 2))

# %%
def back_lader(n: int) -> str:
    return "\n".join(['*' * i for i in range(n + 1)][::-1])


print(back_lader(4))
print(back_lader(3))

# %%
def number_of_divisors(a: int) -> int:
    return sum([1 for i in range(1, a // 2 + 1) if a % i == 0]) + 1


print(number_of_divisors(5))
print(number_of_divisors(9))
print(number_of_divisors(12))

# %%
def check_palindrome(_str: str) -> bool:
    _str = _str.replace(" ", "").lower()
    return _str == _str[::-1]


print(check_palindrome("test"))  # False
print(check_palindrome("Кит на море не романтик"))  # True

# %%
def multiply(*nums: tuple):
    mult = 1
    for i in nums:
        mult *= i
    return mult

# %%
def recurvise_sum(n):
    if n == 1:
        return 1
    return n + recurvise_sum(n - 1)

print(recurvise_sum(6))
# %%
def rec_str_reverse(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + rec_str_reverse(string[:-1])


print(rec_str_reverse("test"))
# %%
def sum_of_num(n: int) -> int: 
    if n < 10:
        return n
    return n % 10 + sum_of_num(n // 10)

print(sum_of_num(123))
print(sum_of_num(673))
# %%
def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

# for count in fib():
#     print(count)

# %%
def natural_numbers(start=1, step=1):
    while True:
        yield start
        start += step

# for i in natural_numbers():
#     print(i)
# %%
def array_generator(array: list):
    while True:
        yield array

for i in array_generator([1, 2, 3]):
   print(i)
# %%
def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value

for i in repeat_list([1, 2, 3]):
   print(i)


# %%
import time

# Декоратор
def decorator_time(fn):
    def wrapper():
        t0 = time.time()
        result = fn()
        return time.time() - t0  # задекорированная функция будет возвращать время работы
    return wrapper


@decorator_time
def pow_2():
    return 10000000 ** 2


@decorator_time
def in_build_pow():
    return pow(10000000, 2)


N = 100
mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")


# %%
# 14.4.2
def number_of_calls(fn):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        fn(*args, **kwargs)
        count += 1
        print(f"Функция {fn} была вызвана {count} раз")
    return wrapper 


@number_of_calls
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз

# %%
# 14.4.3
def cache(fn):
    cache = {}
    def wrapper(num):
        nonlocal cache
        if num not in cache:
            result = fn(num)
            cache[num] = result
            print(f"Добавление результата в кэш: {cache[num]}")
        else:
            print(f"Возвращение результата из кэша: {cache[num]}")
        print(f"Кэш {cache}")
        return cache[num]
    return wrapper

@cache
def f(n):
   return n * 123456789

f(13)
f(13)
f(10)

# %%
# 14.5.9
def min_list(lis: list):
    if len(lis) == 1:
        return lis[0]
    return lis[0] if lis[0] < min_list(lis[1:]) else min_list(lis[1:])
# %%
# 14.5.10
def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res 

# %%
# 14.5.11
def equal(n, s):
    if s < 0:
        return False
    if n < 10:
        return n == s
    else:
        equal(n // 10, s - n % 10)

print(equal(123, 6))
print(equal(6, 123))
print(equal(123, 5))

# %%
def e():
    n = 1

    while True:
        yield (1 + 1 / n) ** n
        n += 1

        
# %%
# C помощью map перевести все элеметы списка в нижний регистр
L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))
# %%
nums = [-2, -1, 0, 1, -3, 2, -3] 
print(list(filter(lambda x: x % 2 == 0, nums)))


# %%
# сортировка словаря по значениям
d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

print(d.items())
print(dict(sorted(d.items(), key=lambda x: x[1]))) 
# x[1] указывает на второй элемент в кортеже d.items()
# %%
# 14.6.3
#  Задача — отсортировать по индексу массы тела

# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

print(sorted(data, key=lambda x: x[0] / x[1] ** 2))  # не важно что рост в см

# %%
# 14.6.4
# вывести кортеж с минимальнм bmi

print(sorted(data, key=lambda x: x[0] / x[1] ** 2)[0])

# %%
a = ["asd", "bbd", "ddfa", "mcsa"]

print(*list(map(lambda x: len(x), a)))
print(list(map(len, a)))
# %%
a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))
