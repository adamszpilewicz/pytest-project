import pytest

from app.utils.db_utils import validate_email


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
