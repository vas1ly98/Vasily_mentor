from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserDBModel(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    email = Column(String)
    full_name = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    verified = Column(Boolean)
    banned = Column(Boolean)
    roles = Column(String)

class MovieDBModel(Base):
    """
    Модель для таблицы movies.
    """
    __tablename__ = 'movies'  # Имя таблицы в базе данных

    # Поля таблицы
    id = Column(String, primary_key=True)  # Уникальный идентификатор фильма
    name = Column(String, nullable=False)  # Название фильма
    description = Column(String)  # Описание фильма
    price = Column(Integer, nullable=False)  # Цена фильма
    genre_id = Column(String, ForeignKey('genres.id'), nullable=False)  # Ссылка на жанр
    image_url = Column(String)  # Ссылка на изображение
    location = Column(String)  # Локация фильма (например, "MSK")
    rating = Column(Integer)  # Рейтинг фильма
    published = Column(Boolean)  # Опубликован ли фильм
    created_at = Column(DateTime)  # Дата создания записи