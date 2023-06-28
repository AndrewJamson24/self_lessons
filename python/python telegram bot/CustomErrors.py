class Error_Length(BaseException):
    def __str__(self):
        return "Error длина должна быть больше"


class Double_Commands(BaseException):

    def __str__(self):
        return 'Error expected input with products an kcal got command'