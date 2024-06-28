import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *

def test_getAll_ingredient():
    controller = Controller("./src/database/nomnom.db")
    ingredients = controller.get_all_ingredient()
    assert ingredients is not None