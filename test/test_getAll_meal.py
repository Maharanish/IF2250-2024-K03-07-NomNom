import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *

def test_getAll_meal():
    controller = Controller("./src/database/nomnom.db")
    meals = controller.get_all_meal()
    assert meals is not None