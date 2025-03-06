from typing import Optional
import datetime
from typing import List
from pydantic import BaseModel, Field, field_validator
from Cinescope_API_Movies.enums.roles import Roles
from enum import Enum

class TestUser(BaseModel):
    email: str
    fullName: str
    password: str = Field(..., min_length=6, max_length=18, description="password может быть от 6 до 18  символов")
    passwordRepeat: str = Field(..., min_length=6, max_length=18, description="passwordRepeat должен вполностью совпадать с полем password")
    roles: list[Roles] = [Roles.USER]
    verified: Optional[bool] = None
    banned: Optional[bool] = None
    id: Optional[int] = None
    createdAt: Optional[str] = None

    @field_validator("passwordRepeat")
    def check_password_repeat(cls, value: str, info) -> str:
        # Проверяем, совпадение паролей
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Пароли не совпадают")
        return value

    # Добавляем кастомный JSON-сериализатор для Enum
    class Config:
        json_encoders = {
            Roles: lambda v: v.value  # Преобразуем Enum в строку
        }
class LoginData(BaseModel):
    email: str = Field(..., description="Email супер-админа")
    password: str = Field(..., min_length=6, max_length=18, description="Пароль пользователя")
    passwordRepeat: Optional[str] = None
    role: Roles = Roles.USER
    @field_validator('passwordRepeat')
    def check_password_repeat(cls, value:str, info) -> str:
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Пароли не совпадают")
        return value



class RegisterUserResponse(BaseModel):
    id: str
    email: str = Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", description="Email пользователя")
    fullName: str = Field(min_length=1, max_length=100, description="Полное имя пользователя")
    verified: bool
    banned: bool
    roles: List[Roles]
    createdAt: str = Field(description="Дата и время создания пользователя в формате ISO 8601")

    @field_validator("createdAt")
    def validate_created_at(cls, value: str) -> str:
        # Валидатор для проверки формата даты и времени (ISO 8601).
        try:
            datetime.datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("Некорректный формат даты и времени. Ожидается формат ISO 8601.")
        return value

