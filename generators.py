def filter_by_currency(transactions: list[dict], currency: str ) -> list[dict]:
    filtered_result = []
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            filtered_result.append(i)
    return filtered_result


def transaction_descriptions(transactions:list[dict]) ->str:
    try:
        for i in transactions:
            yield i["description"]
    except StopIteration:
        pass


def card_number_generator(a:int, b:int)-> str:
    for number in range(a, b):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        generated_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield generated_card_number


