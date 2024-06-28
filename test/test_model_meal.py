import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.meal import Meal

def test_model_meal():
    id = 35
    name = "Hot Sauce"
    description = "Spicyyyy"
    recipe = "Made with jalapeno"

    meal = Meal(id, name, description, recipe, )

    assert meal.id_meal == id
    assert meal.name_meal == name
    assert meal.description_meal == description
    assert meal.recipe_meal == recipe
