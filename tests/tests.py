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


print(get_mask_card_number('Visa Gold 5999414228426353'))
print(get_mask_account('Счет 64686473678894779589'))