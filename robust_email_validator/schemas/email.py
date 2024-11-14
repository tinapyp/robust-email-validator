from pydantic import BaseModel


class EmailResponse(BaseModel):
    email: str
    is_valid: bool