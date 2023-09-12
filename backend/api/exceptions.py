from rest_framework.exceptions import APIException
from rest_framework.response import Response


class ExceptionWithMessage(APIException):

    def __init__(self, message: str = '', code: int = 400):
        self.default_code = code
        self.default_detail = message
        super(ExceptionWithMessage, self).__init__()
        