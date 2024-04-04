import pytest

from app.utils.db_utils import validate_email

from utils.db_utils import generate_insert_query, operation_that_fails, time_consuming_operation


# Test cases are separated into valid and invalid to handle the ValueError exception for invalid emails
@pytest.mark.skip(reason='skip this test for now')
@pytest.mark.parametrize("email", [
    pytest.param("valid@example.com", id="Valid email with .com"),
    pytest.param("another.valid@example.co.uk", id="Valid email with .co.uk")
])
def test_validate_email_valid(email):
    # For valid emails, the function should return True and not raise an exception
    assert validate_email(email) is True


@pytest.mark.parametrize("email", [
    pytest.param("invalidemail", id="Missing @ symbol"),
    pytest.param("noatsign.com", id="No TLD")
])
def test_validate_email_invalid(email):
    # For invalid emails, the function is expected to raise a ValueError
    with pytest.raises(ValueError) as excinfo:
        validate_email(email)
    assert "Invalid email address" in str(excinfo.value)


@pytest.mark.parametrize("email", [
    "user@company.digital",
])
@pytest.mark.xfail(reason="Known issue with new domain not being recognized")
def test_validate_email_with_new_tld(email):
    assert validate_email(email)

def test_validate_email():
    email = "adam@gmail.com"
    assert validate_email(email) is True


def test_generate_insert_query():
    table = "users"
    data = {"name": "John", "email": "john@example.com"}
    expected_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    query, values = generate_insert_query(table, data)

    assert query == expected_query
    assert values == ["John", "john@example.com"]


def test_operation_that_fails():
    with pytest.raises(ValueError) as exc_info:
        operation_that_fails()
    assert "This operation failed a" in str(exc_info.value)


@pytest.mark.slow
def test_time_consuming_operation():
    print("Running a slow test...")
    assert time_consuming_operation() is True
