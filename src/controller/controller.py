import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from models.ingredient import *
from models.jadwalmakanan import *
from models.meal import *
from models.mealhistory import *


class Controller:
    def __init__(self, db_name):
        """Controller class constructor, connects instance to specified db_name"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = 1")

    # ## INGREDIENT CONTROLLERS ##
    def get_ingredient_by_name(self, name_ingredient):
        self.cursor.execute("SELECT * FROM ingredient WHERE name_ingredient = ?", (name_ingredient,))
        ingredient = self.cursor.fetchone()
        return Ingredient.from_row(ingredient) if ingredient else None
    
    def get_all_meal(self):
        """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
        self.cursor.execute("SELECT id_meal, name_meal, description_meal, recipe_meal FROM meal")
        meals = self.cursor.fetchall()
        return [Meal.from_row(row) for row in meals]
    
    def get_all_ingredient(self):
        """Retrieve all ingredients"""
        self.cursor.execute("SELECT id_ingredient, name_ingredient, status_ingredient, status_cart FROM ingredient")
        ingredients = self.cursor.fetchall()
        return [Ingredient.from_row(row) for row in ingredients]

    def get_all_shopping_cart(self):
        """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
        self.cursor.execute("SELECT * FROM ingredient WHERE status_ingredient = 'cart' AND status_cart = 'queued'")
        ingredients = self.cursor.fetchall()
        return [Ingredient.from_row(row) for row in ingredients]

    def update_status_ingredients_to_shoppinghistory(self, name_ingredient):
        """Update ingredients with status_ingredient='cart' and status_cart='queued' to status_ingredient='default' and status_cart='bought'"""
        self.cursor.execute("UPDATE ingredient SET status_ingredient='default', status_cart='bought' WHERE name_ingredient = ?",(name_ingredient,))
        self.commit()

    def update_status_ingredients_to_shoppingcart(self,name_ingredient):
            """Update ingredients with status_ingredient='default' and status_cart='none' to status_ingredient='cart' and status_cart='queued'"""
            self.cursor.execute("UPDATE ingredient SET status_cart='queued', status_ingredient='cart' WHERE name_ingredient = ?",(name_ingredient,))
            self.commit()

    def get_all_shopping_history(self):
        """Retrieve all ingredients with status_ingredient='default' and status_cart='bought'"""
        self.cursor.execute("SELECT * FROM ingredient WHERE status_ingredient = 'default' AND status_cart = 'bought'")
        ingredients = self.cursor.fetchall()
        return [Ingredient.from_row(row) for row in ingredients]

    def update_status_shoppinghistory_to_default(self, name_ingredient): 
        """Update ingredients with status_ingredient='default' and status_cart='bought' to status_ingredient='default' and status_cart='none'""" 
        self.cursor.execute("UPDATE ingredient SET status_cart='none' WHERE name_ingredient = ?", (name_ingredient,)) 
        self.commit()

    # ## JADWALMAKANAN CONTROLLERS ##
    def get_all_jadwalmakanan(self):
        """Retrieve all jadwal makanan"""
        self.cursor.execute("SELECT id_jadwal_makanan, date_jadwal_makanan, category_jadwal_makanan FROM jadwalmakanan")
        jadwalmakanan = self.cursor.fetchall()
        return [JadwalMakanan.from_row(row) for row in jadwalmakanan]
    
    def get_jadwalmakanan_by_category(self, category_jadwal_makanan):
        dates = self.get_current_week_dates()
        jadwals = []
        schedule = []
        for date in dates:
            """Retrieve all jadwalmakanan with a specific category"""
            self.cursor.execute("""
                SELECT meal.id_meal,name_meal,description_meal,recipe_meal FROM jadwalmakanan
                JOIN jadwal_makanan_has_meal ON jadwalmakanan.id_jadwal_makanan = jadwal_makanan_has_meal.id_jadwal_makanan
                JOIN meal ON meal.id_meal = jadwal_makanan_has_meal.id_meal
                WHERE category_jadwal_makanan=? AND date_jadwal_makanan = ?
            """, (category_jadwal_makanan,date,))
            jadwals.append(self.cursor.fetchall())
        for hari_jadwal in jadwals:
            # print("jadwal_h: " +str(hari_jadwal))
            schedule_day = []
            for jadwal in hari_jadwal:
                # print("jadwal : " +str(jadwal))
                temp = Meal.from_row(jadwal)
                schedule_day.append(temp)
            schedule.append(schedule_day)
        return schedule
    
    def get_all_selected_meal(self):
            """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
            self.cursor.execute("SELECT * FROM meal WHERE status_meal = 1")
            meal = self.cursor.fetchone()
            return Meal.from_row((meal[0],meal[1],meal[2],meal[3])) if meal else None

    def update_meal_in_jadwal_makanan(self, id_meal1, id_meal2):
        """Replace meal1 with meal2 in jadwalmakanan"""
        self.cursor.execute("UPDATE jadwal_makanan_has_meal SET id_meal=? WHERE id_meal=?", (id_meal2, id_meal1))
        self.commit()

    def delete_meal_from_jadwalmakanan(self, id_meal):
        """Delete a meal from jadwalmakanan by meal ID"""
        self.cursor.execute("DELETE FROM jadwal_makanan_has_meal WHERE id_meal=?", (id_meal,))
        self.commit()

    def add_meal_to_jadwalmakanan(self, date,category):
        """Add a new meal to jadwalmakanan"""
        query = "INSERT INTO jadwalmakanan (date_jadwal_makanan, category_jadwal_makanan) VALUES (?, ?)"
        self.cursor.execute(query, (date, category,))
        self.commit()

    def update_selected_meal(self,name_meal):
            self.cursor.execute("UPDATE meal SET status_meal=1 WHERE name_meal = ?",(name_meal,))
            self.commit()
        
    
    def save_meal(self,meal_name,meal_desc,meal_recipe,ingredients_text): 
        """MEAL CONTROLLER: insert a new meal, auto increment id_meal"""
    
        query = "INSERT INTO meal (name_meal, description_meal, recipe_meal) VALUES (?, ?, ?)"
        self.cursor.execute(query, (meal_name, meal_desc,meal_recipe))
        id_meal = self.cursor.lastrowid
        ing_list = ingredients_text.split(",")
        id_ing = []
        for ing in ing_list:
            query2 = "INSERT INTO ingredient (name_ingredient) VALUES (?)"
            self.cursor.execute(query2, (ing,))
            id_ing.append(self.cursor.lastrowid)
        for id in id_ing:
            query3 = "INSERT INTO meal_has_ingredient (id_meal,id_ingredient) VALUES (?,?)"
            self.cursor.execute(query3, (id_meal,id,))
        query_jm = "SELECT id_jadwal_makanan FROM jadwalmakanan order by id_jadwal_makanan desc LIMIT 1"
        id_jadwal_makanan = self.cursor.execute(query_jm,).fetchall()
        id = id
        print("id_jadwal"+str(id_jadwal_makanan))
        query4 = "INSERT INTO jadwal_makanan_has_meal (id_jadwal_makanan, id_meal) VALUES (?, ?)"
        self.cursor.execute(query4, (id_jadwal_makanan[0][0],id_meal,))
        self.commit()
        
    
    # def new_meal_jadwal_data(self, meal_name):
    #     """Move all jadwalmakanan past the current date to mealhistory"""
    #     self.cursor.execute("SELECT * FROM jadwalmakanan WHERE date_jadwal_makanan < ?", (date_jadwal_makanan,))
    #     jadwals = self.cursor.fetchall()
    #     for jadwal in jadwals:
    #         self.cursor.execute("INSERT INTO mealhistory (notes_meal_history) VALUES (?)", ('',))
    #         meal_history_id = self.cursor.lastrowid
    #         self.cursor.execute("INSERT INTO meal_history_has_jadwal_makanan (id_meal_history, id_jadwal_makanan) VALUES (?, ?)", (meal_history_id, jadwal[0]))
    #     self.commit()
    
    def display_ingredient(self, id_meal):
        """Retrieve all ingredients for a specific meal by meal ID"""
        self.cursor.execute("""
            SELECT ingredient.* FROM ingredient
            JOIN meal_has_ingredient ON ingredient.id_ingredient = meal_has_ingredient.id_ingredient
            WHERE meal_has_ingredient.id_meal = ?
        """, (id_meal,))
        ingredients = self.cursor.fetchall()
        return [Ingredient.from_row(row) for row in ingredients]

    # ## MEALHISTORY CONTROLLERS ##
    def get_jadwalmakanan_by_date(self, date_jadwal_makanan):
        """Move all jadwalmakanan past the current date to mealhistory"""
        self.cursor.execute("SELECT * FROM jadwalmakanan WHERE date_jadwal_makanan < ?", (date_jadwal_makanan,))
        jadwals = self.cursor.fetchall()
        for jadwal in jadwals:
            self.cursor.execute("INSERT INTO mealhistory (notes_meal_history) VALUES (?)", ('',))
            meal_history_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO meal_history_has_jadwal_makanan (id_meal_history, id_jadwal_makanan) VALUES (?, ?)", (meal_history_id, jadwal[0]))
        self.commit()

    def get_all_meal_history(self):
            self.cursor.execute("Select * FROM mealhistory")
            meal_hist = self.cursor.fetchall()
            return meal_hist

    def get_notes_mealhistory_by_id(self, id_meal_history):
        """Retrieve notes from mealhistory for a specific meal by meal ID"""
        self.cursor.execute("""
            SELECT notes_meal_history FROM mealhistory
            WHERE mealhistory.id_meal_history = ?
        """, (id_meal_history,))
        note = self.cursor.fetchone()
        return note[0] if note else None

    def get_mealhistory_by_date(self,mh_date):
        """Retrieve meal_history from mealhistory for a specific date by mh_date"""
        self.cursor.execute("""
            SELECT mealhistory.id_meal_history,name_meal,category_jadwal_makanan,notes_meal_history FROM mealhistory
            JOIN meal_history_has_jadwal_makanan ON mealhistory.id_meal_history = meal_history_has_jadwal_makanan.id_meal_history
            JOIN jadwalmakanan ON meal_history_has_jadwal_makanan.id_jadwal_makanan = jadwalmakanan.id_jadwal_makanan
            JOIN jadwal_makanan_has_meal ON meal_history_has_jadwal_makanan.id_jadwal_makanan = jadwal_makanan_has_meal.id_jadwal_makanan
            JOIN meal ON jadwal_makanan_has_meal.id_meal = meal.id_meal
            WHERE jadwalmakanan.date_jadwal_makanan = ?
        """, (mh_date,))
        mh = self.cursor.fetchall()
        return mh

    def add_notes_mealhistory(self, id_meal_history, notes):
        """Add notes to mealhistory for a specific mealhistory ID"""
        self.cursor.execute("UPDATE mealhistory SET notes_meal_history=? WHERE id_meal_history=?", (notes, id_meal_history))
        self.commit()

    def get_all_meal_history(self):
        self.cursor.execute("Select * FROM mealhistory")
        meal_hist = self.cursor.fetchall()
        return meal_hist

    # Creators for seeders
    def create_ingredient(self,ingredient):
        """ARTICLE CONTROLLER: insert a new article, auto increment article_id"""
        query = "INSERT INTO ingredient (name_ingredient, status_ingredient, status_cart) VALUES (?, ?, ?)"
        self.cursor.execute(query, (ingredient['name_ingredient'], ingredient['status_ingredient'],ingredient['status_cart']))
        self.commit()
        return self.cursor.lastrowid
    
    def create_meal(self,meal):
        """MEAL CONTROLLER: insert a new meal, auto increment id_meal"""
        query = "INSERT INTO meal (name_meal, description_meal, recipe_meal) VALUES (?, ?, ?)"
        self.cursor.execute(query, (meal['name_meal'], meal['description_meal'],meal['recipe_meal']))
        self.commit()
        return self.cursor.lastrowid
    
    def create_mealhistory(self,mealhistory):
        """ARTICLE CONTROLLER: insert a new mealhistory, auto increment id_mealhistory"""
        query = "INSERT INTO mealhistory (notes_meal_history) VALUES (?)"
        self.cursor.execute(query, (mealhistory['notes_meal_history'],))
        self.commit()
        return self.cursor.lastrowid
    
    def create_jadwalmakanan(self,jadwalmakanan):
        """ARTICLE CONTROLLER: insert a new jadwalmakanan, auto increment id_jadwalmakanan"""
        now = datetime.now().strftime("%Y-%m-%d")
        query = "INSERT INTO jadwalmakanan (date_jadwal_makanan, category_jadwal_makanan) VALUES (?, ?)"
        self.cursor.execute(query, (now, jadwalmakanan['category_jadwal_makanan']))
        self.commit()
        return self.cursor.lastrowid
    
    
    
    def generate_random_schedule(self,n):
        for i in range (n):
            meal = self.get_random_meal()
            date = self.generate_random_date("2024-05-13","2024-05-19")
            category = self.generate_random_category()
            """ARTICLE CONTROLLER: insert a new jadwalmakanan, auto increment id_jadwalmakanan"""
            query = "INSERT INTO jadwalmakanan (date_jadwal_makanan, category_jadwal_makanan) VALUES (?, ?)"
            self.cursor.execute(query, (date, category))
            jadwalmakanan_id = self.cursor.lastrowid
            query = "INSERT INTO jadwal_makanan_has_meal (id_jadwal_makanan, id_meal) VALUES (?, ?)"
            self.cursor.execute(query, (jadwalmakanan_id, meal[0]))
            self.commit()
            



    # ## UTILITY ##
    def __del__(self):
        """Instance deletion: close DB connection"""
        self.conn.close()

    def commit(self):
        """Commit DB modification"""
        self.conn.commit()
    

    # Randomizers #

    def get_random_meal(self):
        query = "SELECT * FROM meal ORDER BY RANDOM() LIMIT 1"
        self.cursor.execute(query)
        meal = self.cursor.fetchone()
        return meal
    
    def generate_random_category(self):
        import random
        category = ["breakfast","lunch","dinner"]
        return random.choice(category)
    

    def generate_random_date(self,start_date_str, end_date_str):
        import random
        from datetime import datetime, timedelta
        """
        Generate a random date within the specified range and format it.
        
        Args:
        start_date_str (str): The start date in 'YYYY-MM-DD' format.
        end_date_str (str): The end date in 'YYYY-MM-DD' format.
        date_format (str): The format for the output date (default is 'DD-MM-YYYY').

        Returns:
        str: The randomly generated date in the specified format.
        """
        # Parse the input date strings into datetime objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        # Calculate the difference between the end and start dates
        date_range = end_date - start_date

        # Generate a random number of days within the range
        random_days = random.randint(0, date_range.days)

        # Add the random number of days to the start date
        random_date = start_date + timedelta(days=random_days)

        # Format the random date in the specified format
        random_date_formatted = random_date.strftime("%Y-%m-%d")

        return random_date_formatted

    def get_current_week_dates(self):
        from datetime import datetime,timedelta
        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
        dates_of_week = [start_of_week + timedelta(days=i) for i in range(7)]  # List of all days in the current week
        return dates_of_week
    


    # MODIFY BFAST, LUNCH, DINNER
    def get_all_meal(self):
        """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
        self.cursor.execute("SELECT id_meal, name_meal, description_meal, recipe_meal FROM meal")
        meals = self.cursor.fetchall()
        return [Meal.from_row(row) for row in meals]
    
    
    def send_modify_meal(self,id_meal):
        self.cursor.execute("UPDATE meal SET status_meal = 2 WHERE id_meal = ?", (int(id_meal),))
        self.commit()
    
    def get_all_modify_meal(self):
        """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
        self.cursor.execute("SELECT * FROM meal WHERE status_meal = 2")
        meal = self.cursor.fetchone()
        return Meal.from_row((meal[0],meal[1],meal[2],meal[3])) if meal else None
    
    def get_meal_by_name(self, meal_name):
        self.cursor.execute("SELECT * FROM meal WHERE name_meal = ?", (meal_name,))
        meal = self.cursor.fetchone()
        return Meal.from_row((meal[0],meal[1],meal[2],meal[3])) if meal else None
    
    def revert_modify_meal(self):
        """Retrieve all ingredients with status_ingredient='cart' and status_cart='queued'"""
        self.cursor.execute("UPDATE meal SET status_meal = 0 WHERE status_meal = 2")
        self.commit

    def update_status_meal_to_default(self,name_meal):
        self.cursor.execute("UPDATE meal SET status_meal = 0 WHERE name_meal = ?", (name_meal,))
        self.commit()