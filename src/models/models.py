from fastapi import HTTPException
from pydantic import BaseModel


class LoginForm(BaseModel):
    email: str
    password: str


class CustomHttpException(HTTPException):
    def __init__(self, status_code: int, error_message: str):
        super().__init__(status_code=status_code, detail={"error": error_message})
