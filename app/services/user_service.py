from utils.db_utils import validate_email


class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, user_data):
        if validate_email(user_data['email']):
            self.db.create('users', user_data)
        else:
            raise ValueError("Invalid email address.")

    def update_email(self, user_id, new_email):
        if validate_email(new_email):
            self.db.update("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
        else:
            raise ValueError("Invalid email address.")
