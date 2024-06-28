import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *
from models.mealhistory import MealHistory

def test_create_mealhistory():
    controller = Controller("./src/database/nomnom.db")

    meal_hist = MealHistory(
        id_meal_history=1,
        notes_meal_history=  ""
    )

    mh_data = {
        "id_meal_history" : meal_hist.id_meal_history,
        "notes_meal_history": meal_hist.notes_meal_history
    }

    controller.create_mealhistory(mh_data)
    find_meal_hist = controller.get_all_meal_history()
    assert find_meal_hist is not None