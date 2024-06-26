import pytest

from utils.db_utils import validate_email, validate_email_with_warning

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


import pytest


@pytest.mark.parametrize("email, is_valid", [
    pytest.param("valid@example.com", True, id="Valid email"),
    pytest.param("another.valid@example.co.uk", True, id="Valid email with .co.uk"),
    pytest.param("invalidemail", False, id="Missing @ symbol and domain"),
    pytest.param("noatsign.com", False, id="No @ symbol"),
])
def test_validate_email(email, is_valid):
    if is_valid:
        # For proper email addresses, the function should return True
        assert validate_email(email) is True
    else:
        # For invalid email addresses, the function should raise a ValueError
        with pytest.raises(ValueError) as excinfo:
            validate_email(email)
        assert "Invalid email address" in str(excinfo.value)


@pytest.mark.parametrize("email", [
    "user@companydigital",
])
@pytest.mark.xfail(reason="Known issue with new domain not being recognized")
def test_validate_email_with_new_tld(email):
    assert validate_email(email)


# def test_validate_email():
#     email = "adam@gmail.com"
#     assert validate_email(email) is True


def test_generate_insert_query():
    table = "users"
    data = {"name": "John", "email": "john@example.com"}
    expected_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    query, values = generate_insert_query(table, data)

    assert query == expected_query
    assert values == ["John", "john@example.com"]


@pytest.mark.error
def test_operation_that_fails():
    with pytest.raises(ValueError) as exc_info:
        operation_that_fails()
    assert "This operation failed" in str(exc_info.value)


@pytest.mark.slow
def test_time_consuming_operation():
    print("Running a slow test...")
    assert time_consuming_operation() is True

@pytest.mark.parametrize("email", [
    "user@deprecateddomain.com",
    "valid@example.com"
])
def test_validate_email_with_warning(email, recwarn):
    validate_email_with_warning(email)
    if email.endswith("@example.com"):
        assert len(recwarn) == 1
        assert recwarn[0].category == DeprecationWarning
        assert "Domain example.com is deprecated" in str(recwarn[0].message)
    else:
        assert len(recwarn) == 0