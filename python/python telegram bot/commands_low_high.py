import API


def initialize_request(callfrom:str, food_number:str, food_type:str, max_kcal:str) -> list[dict] or None:
    """
    Функция делает API request и возврощяет отсортированые клочь и словарь
    :param callfrom: сепарирует вызов с команды low и high
    :param food_number: число блюд которых нужно искать
    :param food_type: тип еды
    :param max_kcal: максимальное количество калорий
    :return: список из отсортированых клочей и словарь в одном списке
    """
    try:
        request_result = API.recipe_search(number=food_number, food_type=food_type, max_calories=max_kcal)
        if request_result is None:
            return None

        special = {}
        for i in request_result['results']:
            special[f'{i["calories"]}'] = i

        if callfrom == 'low':
            sorted_keys = list(special.keys())
            sorted_keys.sort(key=int)
            sorted_keys.append(special)
            return sorted_keys
        else:
            sorted_keys = list(special.keys())
            sorted_keys.sort(key=int, reverse=True)
            sorted_keys.append(special)
            return sorted_keys

    except TypeError:
        return None
