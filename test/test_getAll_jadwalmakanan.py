import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *

def test_getAll_jadwal_makanan():
    controller = Controller("./src/database/nomnom.db")
    jadwal_makanan = controller.get_all_jadwalmakanan()
    assert jadwal_makanan is not None