import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.widget import get_date
from src.widget import mask_account_card
from generators import filter_by_currency
from generators import transaction_descriptions
from generators import card_number_generator

@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 5999414228426353", "Maestro 5999 41** **** 6353"),
    ("MasterCard 5999414228426353", "MasterCard 5999 41** **** 6353"),
    ("Visa Classic 5999414228426353", "Visa Classic 5999 41** **** 6353"),
    ("Visa Platinum 5999414228426353", "Visa Platinum 5999 41** **** 6353"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
])
def test_mask_card(string, expected_result):
    assert get_mask_card_number(string) == expected_result


def test_mask_acc():
    assert get_mask_account('Счет 64686473678894779589') == 'Счет **9589'


def test_mask_acc_card():
    assert mask_account_card('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'


def test_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'


def test_filter(test_filter_card):
    assert filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], state='CANCELED') == test_filter_card


def test_sort(test_sort_card):
    assert sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], sort_order=False) == test_sort_card

def test_filter_by_currency(test_filter_by_currency_list):
    assert list(filter_by_currency ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ], 'USD')) == [test_filter_by_currency_list]


def test_transaction_descriptions():
    assert list(transaction_descriptions([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])) ==['Перевод организации',
 'Перевод со счета на счет',
 'Перевод со счета на счет',
 'Перевод с карты на карту',
 'Перевод организации']


def test_card_number_generator():
    for card_number in card_number_generator(9999999999999998, 9999999999999999):
        assert card_number == '9999 9999 9999 9998'



