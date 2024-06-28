import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.ingredient import Ingredient

def test_model_ingredient():
    id = 50
    name = "Hot Sauce"
    status_i = "Default"
    status_c = "None"

    ingredient = Ingredient(id, name, status_i, status_c)

    assert ingredient.id_ingredient == id
    assert ingredient.name_ingredient == name
    assert ingredient.status_ingredient == status_i
    assert ingredient.status_cart == status_c