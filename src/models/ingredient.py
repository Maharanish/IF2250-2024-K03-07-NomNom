import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.model import *
class Ingredient(Model):
    def __init__(self, id_ingredient, name_ingredient, status_ingredient, status_cart):
        self.id_ingredient = id_ingredient
        self.name_ingredient = name_ingredient
        self.status_ingredient = status_ingredient
        self.status_cart = status_cart