import pytest


@pytest.mark.parametrize("class_param", ["c1", "c2"])
class TestCombinedParametrization:

    @pytest.mark.parametrize("method_param", ["m1", "m2", "m3"])
    def test_combination(self, class_param, method_param):
        # Этот тест запустится 6 раз (2 параметра класса × 3 параметра метода)
        print(f"Тест 1 с параметризацией класса={class_param} и метода={method_param}")
        assert True

    def test_only_class_param(self, class_param):
        # Этот тест запустится 2 раза (только с параметрами класса)
        print(f"Тест 2 с параметризацией только класса={class_param}")
        assert True