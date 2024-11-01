def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты выдает засекреченный номер карты(маску)"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и выдает его маску"""
    return f"**{card_account[-4:]}"
