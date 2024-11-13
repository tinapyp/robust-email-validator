from RobustEmailValidator import validate_single_email, validate_bulk_emails

# Validate single email
result = validate_single_email("user@example.com")
print(result)

# Validate bulk emails
results = validate_bulk_emails(["user1@example.com", "user2@invalid.com"])
print(results)
