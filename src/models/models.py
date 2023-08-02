from typing import Optional

from pydantic import BaseModel


class LoginForm(BaseModel):
    email: str
    password: str


class RegisterForm(BaseModel):
    email: str
    password: str
    name: str
    remember: Optional[int] = 1


class TitleTodoModel(BaseModel):
    title: str


class CompletedTodoModel(BaseModel):
    completed: bool
