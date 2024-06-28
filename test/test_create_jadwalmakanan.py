import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller.controller import *
from models.jadwalmakanan import JadwalMakanan

def test_create_jadwal_makanan():
    controller = Controller("./src/database/nomnom.db")

    today =  datetime.now().strftime("%Y-%m-%d")
    jadwal_makanan1 = JadwalMakanan(

        id_jadwal_makanan= 1,
        date_jadwal_makanan= today,
        category_jadwal_makanan="breakfast",
    )
    # jadwal_makanan2 = JadwalMakanan(

    #     category_jadwal_makanan="lunch"
    # )
    # jadwal_makanan3 = JadwalMakanan(

    #     category_jadwal_makanan="dinner"
    # )

    jadwal_data1 = {
        "id_jadwal_makanan": jadwal_makanan1.id_jadwal_makanan,
        "date_jadwal_makanan": jadwal_makanan1.date_jadwal_makanan,
        "category_jadwal_makanan": jadwal_makanan1.category_jadwal_makanan,
    }
    # jadwal_data2 = {
    #     "category_jadwal_makanan": jadwal_makanan2.category_jadwal_makanan,
    # }
    # jadwal_data3 = {
    #     "category_jadwal_makanan": jadwal_makanan3.category_jadwal_makanan,
    # }

    controller.create_jadwalmakanan(jadwal_data1)
    find_meal= controller.get_all_jadwalmakanan()
    assert find_meal is not None #and len(find_meal) == 3