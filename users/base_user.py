from abc import ABC, abstractmethod
import random


class AccountUser(ABC):
    def __init__(self, username, user_id=None):
        self._user_id = user_id if user_id else self._generate_user_id()
        self.__username = username

    @abstractmethod
    def get_user_details(self):
        pass

    @staticmethod
    def _generate_user_id():
        return random.randint(1000, 9999)

    # def _validate_user_id(user_id):
    #     if not isinstance(user_id, int) or user_id <= 0:
    #         raise ValueError("user_id must be a positive integer.")
    #     return user_id

    def get_username(self):
        return self.__username
