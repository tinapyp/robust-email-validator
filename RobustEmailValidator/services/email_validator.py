from RobustEmailValidator.utils.dns_checker import is_domain_valid
from RobustEmailValidator.utils.disposable_checker import is_disposable
from RobustEmailValidator.schemas.email import EmailResponse


def validate_email(email: str) -> bool:
    """Perform various checks to validate an email."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return True


def validate_single_email(email: str) -> EmailResponse:
    """Validate a single email."""
    is_valid = validate_email(email)
    return EmailResponse(email=email, is_valid=is_valid)


def validate_bulk_emails(emails: list) -> list[EmailResponse]:
    """Validate a list of emails."""
    return [validate_single_email(email) for email in emails]


def check_email_disposable(email: str) -> EmailResponse:
    """Check if the email domain is disposable."""
    domain = email.split("@")[-1]
    disposable = is_disposable(domain)
    return EmailResponse(email=email, is_valid=not disposable)


def check_email_mx(email: str) -> EmailResponse:
    """Check if the email domain has valid MX records."""
    domain = email.split("@")[-1]
    has_mx = is_domain_valid(domain)
    return EmailResponse(email=email, is_valid=has_mx)
