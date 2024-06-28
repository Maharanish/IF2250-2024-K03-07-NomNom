import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *

def test_getAll_meal_history():
    controller = Controller("./src/database/nomnom.db")
    meal_hists = controller.get_all_meal_history()
    assert meal_hists is not None