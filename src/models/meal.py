import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.model import *
class Meal(Model):
    def __init__(self, id_meal, name_meal, description_meal, recipe_meal):
        self.id_meal = id_meal
        self.name_meal = name_meal
        self.description_meal = description_meal
        self.recipe_meal = recipe_meal