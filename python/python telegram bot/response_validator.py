import commands_low_high
import command_custom
import CustomErrors


def request_validator(message:str, call_from) -> list[dict] or None:
    """
    Функция для проверки инпута
    :param message: стринг от сообщения получено в телеботе
    :param call_from: параметр стринг от которой комманды идет колл
    :return: возврощяет саисок из отсортированых клочей и словоря
    """
    try:

        message = message.replace('\n',' ').replace(',', ' ').split()
        if call_from == 'custom':
            if len(message) != 4:
                return None
            else:
                return command_custom.initialize_request(
                    food_number=message[1],
                    food_type=message[0],
                    max_kcal=str(max(int(message[2]), int(message[3]))),
                    min_kcal=str(min(int(message[2]), int(message[3]))))
        else:
            if len(message) != 3:
                return None
            else:
                return commands_low_high.initialize_request(
                                                    callfrom=call_from,
                                                    food_number=message[1],
                                                    food_type=message[0],
                                                    max_kcal=message[2]
                )

    except ValueError:
        return None

    except CustomErrors.Error_Length:
        return None

    except IndexError:
        return None


