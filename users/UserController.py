from users.User import User
from abc import ABC, abstractmethod

class UserController(ABC):

    @abstractmethod
    def save_user(self, user):
        pass

    @abstractmethod
    def load_user(self, /, name = None, id = None):
        pass

    @abstractmethod
    def delete_user(self, /, name = None, id = None):
        pass

    @abstractmethod
    def update_user(self, user, /, name = None, id = None):
        pass

    @abstractmethod
    def _username_is_free(self, uname):
        pass


