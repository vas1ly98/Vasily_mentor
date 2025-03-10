from sqlalchemy import create_engine, Column, String, Boolean, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker

# Подключение к базе данных
host = "92.255.111.76"
port = 31200
database_name = "db_movies"
username = "postgres"
password = "AmwFrtnR2"

#формируем урл для подключения к базе
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}"
#обьект для подключения к базе данных
engine = create_engine(connection_string)

def sdl_alchemy_SQL():
    query = """
        SELECT id, email, full_name, "password", created_at, updated_at, verified, banned, roles
        FROM public.users
        WHERE id = :user_id;
        """
    user_id = 'ff11de2e-6cd2-40bb-a56d-03aa008e8144'
# Выполняем запрос
    with engine.connect() as connection:  # выполняем соединенеи с базой данных и автоматически закрываем его по завершени выполнения
        result = connection.execute(text(query), {"user_id": user_id})
        rows = result.fetchall()  # Получаем все строки
        if not rows:
            print("Нет данных для данного ID")
        for row in rows:
            print(row)

sdl_alchemy_SQL()

def sdl_alchemy_ORM():
    # Базовый класс для моделей
    Base = declarative_base()

    # Модель таблицы users
    class User(Base):
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

    # Создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()

    user_id = 'ff11de2e-6cd2-40bb-a56d-03aa008e8144'

    # Выполняем запрос
    user = session.query(User).filter(User.id == user_id).first()

    # Выводим результат (у нас в руках уже не строка а обьект!)
    if user:
        print(f"ID: {user.id}")
        print(f"Email: {user.email}")
        print(f"Full Name: {user.full_name}")
        print(f"Password: {user.password}")
        print(f"Created At: {user.created_at}")
        print(f"Updated At: {user.updated_at}")
        print(f"Verified: {user.verified}")
        print(f"Banned: {user.banned}")
        print(f"Roles: {user.roles}")
    else:
        print("Пользователь не найден.")

sdl_alchemy_ORM()