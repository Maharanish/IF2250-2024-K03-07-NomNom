import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.mealhistory import *

def test_model_mealhistory():
    id = 28
    notes = "kureng"

    mealhistory = MealHistory(id, notes)

    assert mealhistory.id_meal_history == id
    assert mealhistory.notes_meal_history == notes