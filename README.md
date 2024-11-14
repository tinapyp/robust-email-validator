# Robust Email Validator

RobustEmailValidator is a flexible and powerful Python library for validating email addresses. It verifies email syntax, checks for disposable domains, and validates domain MX records to ensure email deliverability.

## Features

- **Email Syntax Validation**: Checks if an email address follows proper syntax.
- **Bulk Email Validation**: Validate multiple emails at once.
- **Disposable Email Detection**: Identifies if an email address belongs to a disposable service.
- **MX Record Verification**: Checks if the email domain has valid MX (Mail Exchange) records.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- `pip` for dependency management

### Installing via pip

You can install RobustEmailValidator directly from PyPI:

```bash
pip install robust_email_validator
```

### Installing Manually

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tinapyp/robust-email-validator.git
   cd robust-email-validator
   ```

2. Install the library and its dependencies:

   ```bash
   pip install .
   ```

## Usage

The library is easy to integrate into any Python project.

### Validating a Single Email

```python
from robust_email_validator import validated_email

email = "test@example.com"
result = validated_email(email)
print(f"Is {email} valid? {result.is_valid}")
```

### Checking if Email Domain is Disposable

```python
from robust_email_validator import check_email_disposable

email = "test@tempmail.com"
result = check_email_disposable(email)
print(f"Is {email} disposable? {'Yes' if not result.is_valid else 'No'}")
```

### Checking if Email Domain Has MX Records

```python
from robust_email_validator import check_email_mx

email = "test@example.com"
result = check_email_mx(email)
print(f"Does {email} have MX records? {'Yes' if result.is_valid else 'No'}")
```

## Configuration

The library allows configuration of the disposable domain list source. In `config.py`, set the URL to fetch a disposable domain list as needed:

```python
# config.py
DISPOSABLE_URL = "https://someapi.com/disposable-domains"
```

## Development

To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-branch`.
3. Implement your changes and write tests.
4. Run tests to ensure functionality: `pytest`.
5. Submit a pull request with a summary of your changes.

### Running Tests

To run tests, install `pytest` if needed:

```bash
pip install pytest
```

Then run:

```bash
pytest test/test_email_validator.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [dnspython](https://www.dnspython.org/) for DNS query handling.
- [requests](https://requests.readthedocs.io/en/latest/) for HTTP requests to retrieve disposable domains.

---

Contributions and feedback are welcome! Open an issue or submit a pull request if you’d like to get involved.
