from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_date
from src.processing import filter_by_state
from src.processing import sort_by_date
import pytest

def test_mask_card():
    assert get_mask_card_number('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'


def test_mask_acc():
    assert get_mask_account('Счет 64686473678894779589') == 'Счет **9589'


def test_mask_acc_card():
    assert mask_account_card('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'


def test_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'


def test_filter(filter_card):
    assert filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], state = 'CANCELED') == filter_card

def test_sort(sort_card):
    assert sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], sort_order = False) == sort_card