def filter_by_state(dict_list, state ='EXECUTED') -> list[any]:
    """Функция принимает список словарей, фильтрует по ключевому слову и возвращает новый список"""
    new_dict_list = []
    for list__ in dict_list:
        if list__['state'] == state:
            new_dict_list.append(list__)
    return new_dict_list