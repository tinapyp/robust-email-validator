from email_validator.services.email_validator import (
    validate_single_email,
    validate_bulk_emails,
    check_email_disposable,
    check_email_mx,
)


def test_validate_single_email():
    email = "test@example.com"
    result = validate_single_email(email)
    assert result.email == email
    assert result.is_valid is True


def test_validate_bulk_emails():
    emails = ["valid@example.com", "invalid-email"]
    result = validate_bulk_emails(emails)
    assert len(result) == 2
    assert result[0].is_valid is True
    assert result[1].is_valid is False


def test_check_email_disposable():
    email = "test@disposable.com"
    result = check_email_disposable(email)
    assert result.email == email
    assert result.is_valid is False


def test_check_email_mx():
    email = "test@example.com"
    result = check_email_mx(email)
    assert result.email == email
    assert result.is_valid is True
