from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ovo = Ingredient("ovo")
    assert ovo.name == "ovo"
    assert ovo.restrictions == {Restriction.ANIMAL_DERIVED}
    assert repr(ovo) == "Ingredient('ovo')"

    segundo_ovo = Ingredient("ovo")
    assert ovo.__hash__() == segundo_ovo.__hash__()
    assert ovo == segundo_ovo

    frango = Ingredient("frango")
    assert ovo.__hash__() != frango.__hash__()
    assert ovo != frango
