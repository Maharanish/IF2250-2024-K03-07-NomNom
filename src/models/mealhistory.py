import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.model import *
class MealHistory(Model):
    def __init__(self, id_meal_history, notes_meal_history):
        self.id_meal_history = id_meal_history
        self.notes_meal_history = notes_meal_history