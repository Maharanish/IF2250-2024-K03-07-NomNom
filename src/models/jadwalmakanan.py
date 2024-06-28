import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.model import *
class JadwalMakanan(Model):
    def __init__(self, id_jadwal_makanan, date_jadwal_makanan, category_jadwal_makanan):
        self.id_jadwal_makanan= id_jadwal_makanan
        self.date_jadwal_makanan= date_jadwal_makanan
        self.category_jadwal_makanan= category_jadwal_makanan