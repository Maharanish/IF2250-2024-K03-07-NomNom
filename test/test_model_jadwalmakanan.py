import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.jadwalmakanan import *

def test_model_jadwalmakanan():
    id = 20
    date = '2024-05-19'
    category = "Breakfast"

    jadwalmakanan = JadwalMakanan(id, date, category)

    assert jadwalmakanan.id_jadwal_makanan == id
    assert jadwalmakanan.date_jadwal_makanan == date
    assert jadwalmakanan.category_jadwal_makanan == category