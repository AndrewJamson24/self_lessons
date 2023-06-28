import requests
import json
from typing import Optional
import logging
import configparser


config = configparser.ConfigParser()
logger = logging.getLogger()

config.headers = {}


def api_request(url: str, querystring: dict) -> Optional[dict]:
    """
    Функция отправки запроса к API
    :param url: url запроса
    :param querystring: параметр запроса в формате словаря
    """
    try:
        response = requests.request("GET", url, headers=config.headers, params=querystring, timeout=20)
        if response.status_code == 200:
            result = json.loads(response.text)
        else:
            result = None
    except requests.Timeout as time_end:
        logger.exception(time_end)
        result = None
    except requests.RequestException as er:
        logger.exception(er)
        result = None

    return result

def recipe_search(number:str , food_type:str, max_calories:str, min_calories="0") -> Optional[dict]:
    """
    Функция для поиска города по названию
    :param min_calories: минимальное число калорий в блюде - стринг
    :param max_calories: максимальное число калорий в блюде - стринг
    :param food_type: блюда в формате стринг
    :param number: номер скольких блюд отоброжаеться (не больше 10) - стринг
    :return: данные в формате json либо None при отсутствии города в даных от API
    """
    if int(number) > 10:
        return None
    else:

        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex"
        querystring = {"limitLicense":"false","offset":"0","number":number, "query":food_type,
                       "maxCalories":max_calories, "minCalories": min_calories, "type": "main course"}
        return api_request(url=url, querystring=querystring)


