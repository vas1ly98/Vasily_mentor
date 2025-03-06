import pytest
from Cinescope_API_Movies.utils.data_generator import DataGenerator


class TestRoleBasedAccess:
    """Тестирование ролевой модели пользователей"""

    @pytest.mark.parametrize("role, expected_status", [
        ("USER", 403),
        ("ADMIN", 403),  # Исправлено с 201 на 403
        ("SUPER_ADMIN", 201)
    ])
    def test_create_movie_by_role(self, api_manager, user_create, role, expected_status, super_admin_token):
        """Проверяет, какие роли могут создавать фильмы"""
        user = user_create(role)
        assert "id" in user, "Ошибка: в user_create нет ключа 'id'"

        movie_data = {
            "name": DataGenerator.generate_random_movie(),
            "price": 500,
            "description": "Фильм с элементами AQA и тестирования",
            "location": "MSK",
            "published": True,
            "genreId": 1
        }

        assert hasattr(api_manager, "movies_api"), "Ошибка: у api_manager нет атрибута movies_api"

        updated_user = api_manager.auth_api.get_user(user["id"], super_admin_token)
        assert role in updated_user["roles"], f"Ошибка: у пользователя нет роли {role} после обновления."

        # Перелогиниваемся после смены роли
        new_token_response = api_manager.auth_api.login_user(
            {"email": user["email"], "password": user["password"]}).json()
        new_token = new_token_response.get("accessToken")

        assert new_token, "Ошибка: не удалось получить новый токен после обновления роли."

        headers = {
            "Authorization": f"Bearer {new_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        # 🟠 Отправляем запрос
        response = api_manager.movies_api.create_movie(data=movie_data, headers=headers)
        # ✅ Проверяем ожидаемый статус
        assert response.status_code == expected_status, (
            f"Ожидали {expected_status}, но получили {response.status_code}. Данные: {response.json()}"
        )

    @pytest.mark.parametrize("role, expected_status", [
        ("USER", 403),
        ("ADMIN", 403),  # Исправлено с 201 на 403
        ("SUPER_ADMIN", 201)
    ])
    def test_delete_movie_by_role(self, api_manager, user_create, role, expected_status, super_admin_token):
        """Проверяет, какие роли могут удалять фильмы"""
        user = user_create(role)

        if role in ['SUPER_ADMIN']:
            movie_data = {
                "name": f"{role} Movie to Delete",
                "price": 100,
                "description": f"Фильм для удаления {role}",
                "location": "MSK",
                "published": True,
                "genreId": 1
            }
            create_response = api_manager.movies_api.create_movie(data=movie_data, token=user.token)
            assert create_response.status_code == 201, f"{role} должен создать фильм, но получил {create_response.status_code}"
            movie_id = create_response.json()['id']
        else:
            # Для других ролей берем ID фильма, который уже существует
            movie_id = 1  # Убедитесь, что фильм с таким ID существует

        response = api_manager.movies_api.delete_movie(movie_id=movie_id, token=user.token)
        assert response.status_code == expected_status, f"{role} должен получить {expected_status}, но получил {response.status_code}"





