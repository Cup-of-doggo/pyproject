def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты выдает засекреченный номер карты(маску)"""
    if 'Maestro' in card_number:
        return f"{card_number[:12]} {card_number[12:14]}** **** {card_number[20:]}"
    if 'MasterCard' in card_number:
        return f"{card_number[:15]} {card_number[15:17]}** **** {card_number[23:]}"
    if 'Visa Classic' in card_number:
        return f"{card_number[:17]} {card_number[17:19]}** **** {card_number[25:]}"
    if 'Visa Platinum' in card_number:
        return f"{card_number[:18]} {card_number[18:20]}** **** {card_number[26:]}"
    if 'Visa Gold' in card_number:
        return f"{card_number[:14]} {card_number[14:16]}** **** {card_number[22:]}"


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и выдает его маску"""
    return f"{card_account[0:4]} **{card_account[-4:]}"


def mask_account_card(some_card_number: str) -> str:
    '''функция принимает счет или номер карты и возвращает его маску'''
    if 'Счет' in some_card_number:
        return get_mask_account(some_card_number)
    else:
        return get_mask_card_number(some_card_number)


def get_date(date: str) -> str:
     '''функция принимает дату и возвращает в читабельном формате'''
     return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


print(get_mask_card_number('Visa Gold 5999414228426353'))
print(get_mask_account('Счет 64686473678894779589'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 64686473678894779589'))
print(get_date('2024-03-11T02:26:18.671407'))