from datetime import datetime, timedelta
from Cinescope_API_Movies.utils.data_generator import DataGenerator
from Cinescope_API_Movies.db_requester.models import MovieDBModel
from pytz import timezone
from sqlalchemy.orm import Session
import pytest
import allure
from Cinescope_API_Movies.db_requester.models  import AccountTransactionTemplate
import random

class TestOtherAPI:

    def test_create_delete_movie(self, api_manager, super_admin_token, create_movie, db_session: Session):
        # Используем данные фильма, который создали через фикстуру
        movie_name = create_movie["name"]
        movie_id = create_movie["id"]

        # Проверяем, что фильм был добавлен в базу данных
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 1, "Фильм не был добавлен в базу данных"

        movie_from_db = movies_from_db.first()
        assert movie_from_db.name == movie_name, "Названия фильма не совпадают"

        # Проверяем, что время создания фильма в базе совпадает с ожидаемым (с погрешностью в 5 минут)
        assert movie_from_db.created_at >= (
            datetime.now(timezone('UTC')).replace(tzinfo=None) - timedelta(minutes=5)
        ), "Время создания фильма не соответствует ожиданиям"

        # Удаляем фильм
        delete_response = api_manager.movies_api.delete_movie(movie_id, super_admin_token)
        assert delete_response.status_code == 200, "Фильм не был удален"

        # Проверяем, что фильм был удален из базы данных
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 0, "Фильм не был удален из базы данных"

# class TestAccountTransactionTemplate:
#
#     def test_accounts_transaction_template(self, db_session: Session):
#         # ====================================================================== Подготовка к тесту
#         # Создаем новые записи в базе данных (чтоб точно быть уверенными что в базе присутствуют данные для тестирования)
#
#         stan = AccountTransactionTemplate.create(user=f"Stan_{DataGenerator.generate_random_int(10)}", balance=1000)
#         bob = AccountTransactionTemplate.create(user=f"Bob_{DataGenerator.generate_random_int(10)}", balance=500)
#
#         # Добавляем записи в сессию
#         db_session.add_all([stan, bob])
#         # Фиксируем изменения в базе данных
#         db_session.commit()
#
#         def transfer_money(session, from_account, to_account, amount):
#             # пример функции выполняющей транзакцию
#             # представим что она написана на стороне тестируемого сервиса
#             # и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
#             """
#             Переводит деньги с одного счета на другой.
#             :param session: Сессия SQLAlchemy.
#             :param from_account_id: ID счета, с которого списываются деньги.
#             :param to_account_id: ID счета, на который зачисляются деньги.
#             :param amount: Сумма перевода.
#             """
#             # Получаем счета
#             from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
#             to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()
#
#             # Проверяем, что на счете достаточно средств
#             if from_account.balance < amount:
#                 raise ValueError("Недостаточно средств на счете")
#
#             # Выполняем перевод
#             from_account.balance -= amount
#             to_account.balance += amount
#             print(f"Переведено {amount} единиц.")
#
#             # Сохраняем изменения
#             session.commit()
#             print("Изменения сохранены в базе данных.")
#
#         # ====================================================================== Тест
#         # Проверяем начальные балансы
#         print("Проверяем начальные балансы.")
#         assert stan.balance == 1000
#         assert bob.balance == 500
#         print(f"Баланс {stan.user}: {stan.balance}, Баланс {bob.user}: {bob.balance}")
#
#         try:
#             # Выполняем перевод 200 единиц от stan к bob
#             transfer_money(db_session, from_account=stan.user, to_account=bob.user, amount=200)
#
#             # Проверяем, что балансы изменились
#             print("Проверяем, что балансы изменились после перевода.")
#             assert stan.balance == 800
#             assert bob.balance == 700
#             print(f"Баланс {stan.user}: {stan.balance}, Баланс {bob.user}: {bob.balance}")
#
#         except Exception as e:
#             # Если произошла ошибка, откатываем транзакцию
#             db_session.rollback()  # откат всех введеных нами изменений
#             pytest.fail(f"Ошибка при переводе денег: {e}")
#
#         finally:
#             # Удаляем данные для тестирования из базы
#             db_session.delete(stan)
#             db_session.delete(bob)
#             # Фиксируем изменения в базе данных
#             db_session.commit()
#             print("Данные удалены и изменения сохранены.")
#


@allure.epic("Тестирование транзакций")
@allure.feature("Тестирование транзакций между счетами")
class TestAccountTransactionTemplate:

    @allure.story("Корректность перевода денег между двумя счетами")
    @allure.description("""
    Этот тест проверяет корректность перевода денег между двумя счетами.
    Шаги:
    1. Создание двух счетов: Stan и Bob.
    2. Перевод 200 единиц от Stan к Bob.
    3. Проверка изменения балансов.
    4. Очистка тестовых данных.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("qa_name", "Ivan Petrovich")
    @allure.title("Тест перевода денег между счетами 200 рублей")
    def test_accounts_transaction_template(self, db_session: Session):
        # ====================================================================== Подготовка к тесту
        with allure.step("Создание тестовых данных в базе данных: счета Stan и Bob"):
            stan = AccountTransactionTemplate(user=f"Stan_{DataGenerator.generate_random_int(10)}", balance=1000)
            bob = AccountTransactionTemplate(user=f"Bob_{DataGenerator.generate_random_int(10)}", balance=500)
            db_session.add_all([stan, bob])
            db_session.commit()
            print(f"Созданы аккаунты: Stan с балансом {stan.balance} и Bob с балансом {bob.balance}")

        @allure.step("Функция перевода денег: transfer_money")
        @allure.description( """
            Функция выполняющая транзакцию, имитация вызова функции на стороне тестируемого сервиса
            и вызывая метод transfer_money, мы какбудто делаем запрос в api_manager.movies_api.transfer_money
            """)
        def transfer_money(session, from_account, to_account, amount):
            with allure.step("Получаем счета"):
                from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
                to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

            with allure.step("Проверяем, что на счете достаточно средств"):
                if from_account.balance < amount:
                    raise ValueError("Недостаточно средств на счете")
                print(f"На счете {from_account.user} достаточно средств для перевода.")

            with allure.step("Выполняем перевод"):
                from_account.balance -= amount
                to_account.balance += amount
                print(f"Переведено {amount} единиц с {from_account.user} на {to_account.user}.")

            with allure.step("Сохраняем изменения"):
                session.commit()
                print("Изменения сохранены в базе данных.")

        # ====================================================================== Тест
        with allure.step("Проверяем начальные балансы"):
            assert stan.balance == 1000
            assert bob.balance == 500
            print(f"Начальные балансы: Stan = {stan.balance}, Bob = {bob.balance}")

        try:
            with allure.step("Выполняем перевод 200 единиц от Stan к Bob"):
                transfer_money(db_session, from_account=stan.user, to_account=bob.user, amount=200)

            with allure.step("Проверяем, что балансы изменились"):
                assert stan.balance == 800
                assert bob.balance == 700
                print(f"После перевода: Stan = {stan.balance}, Bob = {bob.balance}")

        except Exception as e:
            with allure.step("ОШИБКА откаты транзакции"):
                db_session.rollback()
                print("Произошла ошибка, транзакция откатана.")
            pytest.fail(f"Ошибка при переводе денег: {e}")

        finally:
            with allure.step("Удаляем данные для тестирования из базы"):
                db_session.delete(stan)
                db_session.delete(bob)
                db_session.commit()
                print("Данные удалены из базы и изменения сохранены.")

@allure.title("Тест с перезапусками")
@pytest.mark.flaky(reruns=3)
def test_with_retries(delay_between_retries):
    with allure.step("Шаг 1: Проверка случайного значения"):
        result = random.choice([True, False])
        assert result, "Тест упал, потому что результат False"