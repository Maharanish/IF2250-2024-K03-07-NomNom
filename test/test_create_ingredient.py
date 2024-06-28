import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *
from models.ingredient import Ingredient

def test_create_ingredient():
    controller = Controller("./src/database/nomnom.db")

    new_ingredient_name = "Lime"
    ingredient = Ingredient(
        id_ingredient=2,
        name_ingredient="Thyme",
        status_ingredient="Default",
        status_cart="None"
    )

    ingredient_data = {
        "id_ingredient": ingredient.id_ingredient,
        "name_ingredient": new_ingredient_name,
        "status_ingredient": ingredient.status_ingredient,
        "status_cart": ingredient.status_cart
    }

    controller.create_ingredient(ingredient_data)
    find_ingredient = controller.get_ingredient_by_name(new_ingredient_name)
    assert find_ingredient is not None