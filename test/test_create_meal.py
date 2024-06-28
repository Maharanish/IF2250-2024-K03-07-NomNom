import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *
from models.meal import Meal

def test_create_meal():
    controller = Controller("./src/database/nomnom.db")

    new_meal_name = "Hainan Beef Rice"
    meal = Meal(
        id_meal=3,
        name_meal="Hainan Chicken Rice",
        description_meal="With butter rice",
        recipe_meal="Cook in low heat"
    )

    meal_data = {
        "id_meal": meal.id_meal,
        "name_meal": new_meal_name,
        "description_meal": meal.description_meal,
        "recipe_meal": meal.recipe_meal
    }

    controller.create_meal(meal_data)
    find_meal = controller.get_meal_by_name(new_meal_name)
    assert find_meal is not None