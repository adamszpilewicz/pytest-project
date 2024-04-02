import pytest
from app.services.user_service import UserService


class TestUserService:
    # @pytest.fixture
    # def mock_db(self, mocker):
    #     # Use mocker.patch to return a MagicMock object for db operations
    #     return mocker.patch('app.db.mysqldb.MySQLDatabase')

    @pytest.fixture
    def user_service(self, mock_db):
        # Instantiate UserService with the mocked db
        return UserService(db=mock_db)

    def test_register_user_with_valid_email(self, user_service, mock_db):
        # Given valid user data
        user_data = {"email": "valid@example.com", "username": "validuser"}
        # Attempt to register user
        user_service.register_user(user_data)
        # Assert the db.create method was called once with correct user_data
        mock_db.create.assert_called_once_with('users', user_data)

    def test_register_user_with_invalid_email(self, user_service, mock_db):
        # Given invalid user data
        user_data = {"email": "invalidemail", "username": "invaliduser"}
        # Attempting to register a user with an invalid email should raise ValueError
        with pytest.raises(ValueError) as excinfo:
            user_service.register_user(user_data)
        assert "Invalid email address" in str(excinfo.value)
        # Assert the db.create method was not called due to invalid email
        mock_db.create.assert_not_called()

    def test_update_email_with_valid_email(self, user_service, mock_db):
        # Given a user ID and a new valid email
        user_id = 1
        new_email = "newvalid@example.com"
        # Attempt to update the user's email
        user_service.update_email(user_id, new_email)
        # Assert the db.update method was called with correct parameters
        mock_db.update.assert_called_once()

    def test_update_email_with_invalid_email(self, user_service, mock_db):
        # Given a user ID and a new invalid email
        user_id = 1
        new_email = "invalidemail"
        # Attempting to update to an invalid email should raise ValueError
        with pytest.raises(ValueError) as excinfo:
            user_service.update_email(user_id, new_email)
        assert "Invalid email address" in str(excinfo.value)
        # Assert the db.update method was not called due to invalid email
        mock_db.update.assert_not_called()
