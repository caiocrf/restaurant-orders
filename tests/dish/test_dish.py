import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


def test_dish():
    ovo = Ingredient("ovo")
    quantidade_ovo = 10
    pizza = "Pizza"
    pizza_price = 39.20
    hamburger = "Hamburger"
    hamburger_price = 20.20

    pizzaa_dish = Dish(pizza, pizza_price)
    assert pizzaa_dish.name == pizza
    assert repr(pizzaa_dish) == f"Dish('{pizza}', R${pizza_price:.2f})"

    pizzaa_dish.add_ingredient_dependency(ovo, quantidade_ovo)
    assert pizzaa_dish.recipe.get(ovo) == quantidade_ovo
    assert pizzaa_dish.get_ingredients() == {ovo}

    assert pizzaa_dish.get_restrictions() == ovo.restrictions

    pizzaa_second_dish = Dish(pizza, pizza_price)
    assert pizzaa_dish.__hash__() == pizzaa_second_dish.__hash__()
    assert pizzaa_dish == pizzaa_second_dish

    hamburger_dishh = Dish(hamburger, hamburger_price)
    assert pizzaa_dish.__hash__() != hamburger_dishh.__hash__()
    assert pizzaa_dish != hamburger_dishh

    with pytest.raises(TypeError):
        assert Dish(pizza, "")
    with pytest.raises(ValueError):
        assert Dish(pizza, 0)
