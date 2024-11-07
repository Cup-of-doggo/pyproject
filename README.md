#Homework 04.11.2024
##Цели проекта:
1.маскировка входящих данных банковских карт и счетов
2.сортировка входящих списков 
##Установка 
клонируйте репозиторий
```
git clone https://github.com/Cup-of-doggo/pyproject.git
```
###Пример работы
```
get_mask_card_number('Visa Gold 5999414228426353')
get_mask_account('Счет 64686473678894779589')
mask_account_card('Visa Gold 5999414228426353')
mask_account_card('Счет 64686473678894779589')
get_date('2024-03-11T02:26:18.671407')
filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state = 'CANCELED')
sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], sort_order = False)
```
