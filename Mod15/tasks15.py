# %%
"""
Напишите программу, которая получает от пользователя имя файла,
открывает этот файл в текущем каталоге, читает его и выводит два слова:
наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.

В файле ожидается смешанный текст на двух языках — русском и английском.
"""
import re 

def normolize_text(text: str) -> list:
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    return list(map(str.lower, text.split()))

def long_and_common_words(text: list) -> str:
    longest_word = ""
    most_common = ""
    appear = {}
    for word in data:
        if word.encode().isalpha() and len(word) > len(longest_word):
            longest_word = word
        if len(word) >= 4:
            if word not in appear:
                appear[word] = 1
            else:
                appear[word] += 1
    
    for key, value in appear.items():
        if value == max(appear.values()):
            most_common = key

    return longest_word, most_common


# filename = input()
filename = "testfile15_1.txt"

with open(filename, encoding="utf-8") as file:
    data = normolize_text(file.read())
    long, common = long_and_common_words(data)
    print(f"Самое длинное английское слово '{long}'\
        \nСамое частое слово с длиной более 3 символов '{common}'")


# %%
"""
Содержит все перечисленные в требованиях поля.
Не имеет других полей.
Поля:

timestamp: int
referer: string (url)
location: string (url)
remoteHost: string
partyId: string
sessionId: string
pageViewId: string
eventType: string (itemBuyEvent или itemViewEvent)
item_id: string
item_price: int
item_url: string (url)
basket_price: string
detectedDuplicate: bool
detectedCorruption: bool
firstInSession: bool
userAgentName: string

Все поля имеют именно тот тип, который указан в требованиях:

int — целое число;
string — произвольная строка;
string (url) — это строка с url. Проверяем, что url начинается c http:\\ или https:\\;
string (itemBuyEvent или itemViewEvent) — строка;
bool — булево значение.
"""
import json


def check_int(obj) -> bool:
    return isinstance(obj, int)

def check_str(obj) -> bool:
    return isinstance(obj, str)

def check_url(obj) -> bool:
    if check_str(obj):
        return obj.startswith("http://") or obj.startswith("https://")
    else:
        return False

def check_value(obj) -> bool:
    if check_str(obj):
        return obj in ["itemBuyEvent", "itemViewEvent"]
    else:
        return False

def check_bool(obj) -> bool:
    return isinstance(obj, bool)

def log_error(obj, value=None, string=None):
    error.append({obj: f'{value}, {string}'})

error = []

items_list = {'timestamp': 'int', 'item_url': 'int', 'refer': 'url', 'location': 'url', 
         'item_url': 'url', 'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 
         'pageViewId': 'str', 'item_id': 'str', 'item_price': 'int', 'basket_price': 'str', 'userAgentName': 'str',
         'eventType': 'val', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
         'firstInSession': 'bool', 'referer': 'url'}

filename = "test_values.json"
with open(filename, encoding="utf-8") as file:
    data = json.load(file)

for items in data:
    for item in items:
        if item in items_list:
            if items_list[item] == "int":
                if not check_int(items[item]):
                    log_error(item, items[item], f'Ожидаемый тип {items_list[item]}')
            elif items_list[item] == "str":
                if not check_str(items[item]):
                    log_error(item, items[item], f'Ожидаемый тип {items_list[item]}')
            elif items_list[item] == "bool":
                if not check_bool(items[item]):
                    log_error(item, items[item], f'Ожидаемый тип {items_list[item]}')
            elif items_list[item] == "url":
                if not check_url(items[item]):
                    log_error(item, items[item], f'Ожидаемый тип {items_list[item]}')
            elif items_list[item] == "val":
                if not check_value(items[item]):
                    log_error(item, items[item], 'Ожидаемый тип itemBuyEvent или itemViewEvent')
            else:
                log_error(item, items[item], "Неизвестное значение")
        else:
            log_error(item, string="Неизвестная переменная")

if len(error) == 0:
    print("Pass")
else:
    print("Fail")
    print(error) 

# %%
