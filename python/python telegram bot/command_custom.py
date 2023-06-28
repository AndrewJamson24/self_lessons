import API

def initialize_request(food_number:str, food_type:str, max_kcal:str, min_kcal:str) -> list[dict] or None:
    """
    Функция делает API request и возврощяет dict
    :param min_kcal: минимальное количество калорий
    :param food_number: число блюд которых нужно искать
    :param food_type: тип еды
    :param max_kcal: максимальное количество калорий
    :return: список из dict
    """
    try:
        request_result = API.recipe_search(number=food_number, food_type=food_type, max_calories=max_kcal, min_calories=min_kcal)
        if request_result is None:
            return None

        special = {}
        for i in request_result['results']:
            special[f'{i["calories"]}'] = i

        sorted_keys = list(special.keys())
        sorted_keys.append(special)
        return sorted_keys

    except TypeError:
        return None


