def filter_by_state(dict_list, state ='EXECUTED') -> list[any]:
    """Функция принимает список словарей, фильтрует по ключевому слову и возвращает новый список"""
    new_dict_list = []
    for string in dict_list:
        if string['state'] == state:
            new_dict_list.append(string)
    return new_dict_list


def sort_by_date(new_dict_list, sort_order = True) -> list[any]:
    """Функция принимает список словарей и сортирует его(по умолчанию по убыванию) """
    if sort_order == True:
        sorted_list = sorted(new_dict_list, key = lambda index: index['date'], reverse = True)
    else:
        sorted_list = sorted(new_dict_list, key = lambda index: index['date'], reverse = False)
    return sorted_list