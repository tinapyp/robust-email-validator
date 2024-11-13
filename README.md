# Email Validator Service

This is an email validation service built using FastAPI. It verifies email addresses based on format, checks for disposable domains, and verifies the presence of MX records for the email's domain.

## Features

- **Pattern validation**: Ensures the email matches a standard format.
- **Disposable domain check**: Identifies and filters out emails from disposable domains.
- **MX record verification**: Confirms the domain has MX records to validate its existence.

## Project Structure

```plaintext
email_validator_service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email_validator.py   # Email validation logic
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── dns_checker.py       # Checks MX records for domains
│   │   ├── disposable_checker.py # Loads and checks disposable domains
│   └── tests/
│       ├── __init__.py
│       ├── test_email_validator.py # Unit tests
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/email_validator_service.git
   cd email_validator_service
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Download the disposable domains list:
   The service uses an external list of disposable domains. By default, this list is fetched dynamically, but you can update `DISPOSABLE_URL` in `app/config.py` to customize the source.

### Running the Service

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The service will be available at `http://127.0.0.1:8000`, and you can test the API via the interactive documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

- `POST /validate-email`: Validate an email address.

#### Request Body

```json
{
  "email": "test@example.com"
}
```

#### Response

- **200 OK**: Email validation results

  ```json
  {
    "email": "test@example.com",
    "is_valid": true
  }
  ```

## Testing

Run tests with `pytest`:

```bash
pytest app/tests/test_email_validator.py
```

### Test Cases

- **Valid Email**: Verifies valid email formatting, non-disposable, and valid MX records.
- **Invalid Email Pattern**: Fails if email does not match the standard format.
- **Disposable Domain**: Filters out disposable domains based on a blacklist.
- **No MX Records**: Flags domains without MX records as invalid.

## Configuration

- **`BATCH_SIZE`**: Number of emails processed per batch (set in `app/config.py`).
- **`WORKERS`**: Number of parallel threads for DNS checking.
- **`DISPOSABLE_URL`**: URL for disposable domains list.

## Dependencies

- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `requests`: For fetching disposable domains list
- `dnspython`: For MX record verification
- `pandas` and `numpy`: Optional, for data handling if needed
