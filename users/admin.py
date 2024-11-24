from users.base_user import AccountUser


class Admin(AccountUser):
    def __init__(self, username, admin_level, user_id=None):
        super().__init__(user_id, username)
        self.__admin_level = admin_level  # Private attribute

    def get_user_details(self):
        return {"UserID": self._user_id, "Username": self.get_username(), "Admin Level": self.__admin_level}

    def manage_exchange(self):
        print(f"Admin {self.get_username()} is managing the exchange.")
