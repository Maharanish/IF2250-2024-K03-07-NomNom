import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.controller import Controller

if __name__ == "__main__":
    if not os.path.exists("src/database/nomnom.db"):
        conn = sqlite3.connect("src/database/nomnom.db")
        c = conn.cursor()
        
        # Create tables
        c.execute("""
        CREATE TABLE IF NOT EXISTS ingredient (
            id_ingredient integer PRIMARY KEY AUTOINCREMENT,
            name_ingredient text,
            status_ingredient text DEFAULT "default",
            status_cart text DEFAULT "none"
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS meal (
            id_meal integer PRIMARY KEY AUTOINCREMENT,
            name_meal text,
            description_meal text,
            recipe_meal text,
            status_meal int DEFAULT 0
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS jadwalmakanan (
            id_jadwal_makanan integer PRIMARY KEY AUTOINCREMENT,
            date_jadwal_makanan date,
            category_jadwal_makanan text
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS mealhistory (
            id_meal_history integer PRIMARY KEY AUTOINCREMENT,
            notes_meal_history text
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS jadwal_makanan_has_meal (
            id_jadwal_makanan integer,
            id_meal integer,
            FOREIGN KEY (id_jadwal_makanan) REFERENCES jadwalmakanan(id_jadwal_makanan),
            FOREIGN KEY (id_meal) REFERENCES meal(id_meal)
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS meal_has_ingredient (
            id_meal integer,
            id_ingredient integer,
            FOREIGN KEY (id_meal) REFERENCES meal(id_meal),
            FOREIGN KEY (id_ingredient) REFERENCES ingredient(id_ingredient)
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS meal_history_has_jadwal_makanan (
            id_meal_history integer,
            id_jadwal_makanan integer,
            FOREIGN KEY (id_meal_history) REFERENCES mealhistory(id_meal_history),
            FOREIGN KEY (id_jadwal_makanan) REFERENCES jadwalmakanan(id_jadwal_makanan)
        )
        """)
        
        conn.commit()
        conn.close()

    ingredient_seeder=[
          {
            "id_ingredient": 1,
            "name_ingredient": "Rice",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 2,
            "name_ingredient": "Carrot",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 3,
            "name_ingredient": "Pea",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 4,
            "name_ingredient": "Soy Sauce",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 5,
            "name_ingredient": "Salt",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 6,
            "name_ingredient": "Pepper",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 7,
            "name_ingredient": "Egg",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 8,
            "name_ingredient": "Chicken",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 9,
            "name_ingredient": "Bread",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 10,
            "name_ingredient": "Mayonnaise",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 11,
            "name_ingredient": "Mustard",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 12,
            "name_ingredient": "Cheese",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 13,
            "name_ingredient": "Lettuce",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 14,
            "name_ingredient": "Tomato",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 15,
            "name_ingredient": "Oil",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 16,
            "name_ingredient": "Bell Pepper",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 17,
            "name_ingredient": "Cereal",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 18,
            "name_ingredient": "Milk",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 19,
            "name_ingredient": "Sugar",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 20,
            "name_ingredient": "Honey",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 21,
            "name_ingredient": "Butter",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 22,
            "name_ingredient": "Jam",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 23,
            "name_ingredient": "Noodle",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 24,
            "name_ingredient": "Cabbage",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 25,
            "name_ingredient": "Oyster Sauce",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 26,
            "name_ingredient": "Beef",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 27,
            "name_ingredient": "Fish",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 28,
            "name_ingredient": "Flour",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 29,
            "name_ingredient": "Water",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 30,
            "name_ingredient": "Potato",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 31,
            "name_ingredient": "Ginger",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 32,
            "name_ingredient": "Sesame Seeds",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 33,
            "name_ingredient": "Green Onion",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 34,
            "name_ingredient": "Kombu",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 35,
            "name_ingredient": "Mushroom",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 36,
            "name_ingredient": "Tofu",
            "status_ingredient": "default",
            "status_cart": "none",
          },
          {
            "id_ingredient": 37,
            "name_ingredient": "Dumpling Wrapper",
            "status_ingredient": "default",
            "status_cart": "none",
          }
    ]
    
    jadwalmakanan_seeder = [
          {
            "id_jadwal_makanan": 1,
            "category_jadwal_makanan": "breakfast"
          },
          {
            "id_jadwal_makanan": 2,
            "category_jadwal_makanan": "breakfast"
          },
          {
            "id_jadwal_makanan": 3,
            "category_jadwal_makanan": "breakfast"
          },
          {
            "id_jadwal_makanan": 4,
            "category_jadwal_makanan": "lunch"
          },
          {
            "id_jadwal_makanan": 5,
            "category_jadwal_makanan": "lunch"
          },
          {
            "id_jadwal_makanan": 6,
            "category_jadwal_makanan": "lunch"
          },
          {
            "id_jadwal_makanan": 7,
            "category_jadwal_makanan": "lunch"
          },
          {
            "id_jadwal_makanan": 8,
            "category_jadwal_makanan": "dinner"
          },
          {
            "id_jadwal_makanan": 9,
            "category_jadwal_makanan": "dinner"
          },
          {
            "id_jadwal_makanan": 10,
            "category_jadwal_makanan": "dinner"
          },
    ]

    meal_seeder = [
        {
            # "id_meal": 1,
            "name_meal": "Omelette",
            "description_meal":"A classic egg dish filled with your choice of vegetables, cheese, or meat, cooked until golden and fluffy.",
            "recipe_meal":"1. Beat eggs in a bowl and season with salt and pepper.\n2. Heat oil in a pan and pour in the beaten eggs.\n3. Add desired fillings like diced vegetables, cheese, or cooked meat.\n4. Cook until the edges are set, then flip and cook the other side until fully cooked.\n6. Serve and enjoy!"
        },
        {
            # "id_meal": 2,
            "name_meal": "Cereal",
            "description_meal":"A quick and easy breakfast staple, simply pour milk over your favorite cereal and enjoy.",
            "recipe_meal":"1. Pour cereal into a bowl.\n2. Add milk to cover the cereal.\n3. Optionally, add sweeteners like sugar or honey.\n4. Mix and enjoy!"
        },
        {
            # "id_meal": 3,
            "name_meal": "Bread Toast",
            "description_meal":"Golden brown toasted bread slices, perfect with a spread of butter or jam.",
            "recipe_meal":"1. Toast bread slices in a toaster until golden brown.\n2. Spread butter or jam on the toasted bread, if desired."
        },
        {
            # "id_meal": 4,
            "name_meal": "Sandwich",
            "description_meal":"A versatile meal made with your choice of bread, condiments, and fillings like meat, cheese, and veggies.",
            "recipe_meal":"1. Choose your bread and spread condiments like mayonnaise or mustard.\n2. Add your choice of fillings like sliced meat, cheese, lettuce, and tomatoes.\n3. Top with another slice of bread and press gently to make it stick together.\n4. Optionally, grill or toast the sandwich for a warm, crispy texture.\n5. Serve and enjoy!"
        },
        {
            # "id_meal": 5,
            "name_meal": "Fried Noodle",
            "description_meal":"Stir-fried noodles with a mix of vegetables, seasoned with soy sauce and a hint of sweetness.",
            "recipe_meal":"1. Cook noodles according to package instructions.\n2. Heat oil in a pan and stir-fry diced vegetables like carrots, cabbage, and bell peppers.\n3. Grill the shrimp for 2-3 minutes per side, until pink and slightly charred.\n4. Warm tortillas on the grill for 30 seconds per side.\n5. Assemble tacos by filling each tortilla with shrimp, avocado, red onion, jalapeno, and cilantro.\n6. Serve and enjoy!"
        },
        {
            # "id_meal": 6,
            "name_meal": "Beef Yakiniku",
            "description_meal":"Grilled beef slices seasoned with soy-based sauce, served with vegetables.",
            "recipe_meal":"1. Preheat grill pan over medium-high heat.\n2. In a mixing bowl, toss the shrimp with olive oil and taco seasoning.\n3. Add cooked noodles to the pan and stir-fry with vegetables.\n4. Season with soy sauce, oyster sauce, and a pinch of sugar.\n6. Serve and enjoy!"
        },
        {
            # "id_meal": 7,
            "name_meal": "Fish and Chips",
            "description_meal":"Crispy battered fish fillets paired with golden, thick-cut fries.",
            "recipe_meal":"1. Coat fish fillets in a batter made of flour, salt, pepper, and water.\n2. Deep-fry battered fish until golden brown and crispy.\n3. Serve with thick-cut potato fries, salted and fried until golden brown.\n6. Serve and enjoy!"
        },
        {
            # "id_meal": 8,
            "name_meal": "Fried Rice",
            "description_meal":"Savory stir-fried rice with vegetables, seasoned with soy sauce, and optionally mixed with scrambled eggs or chicken.",
            "recipe_meal":"1. Cook rice until it's slightly firm.\n2. Heat oil in a pan and add diced vegetables like carrots, peas, and onions.\n3. Add cooked rice to the pan and stir-fry with vegetables.\n4. Season with soy sauce, salt, and pepper.\n5. Optionally, add scrambled eggs or cooked chicken for protein.\n6. Serve and enjoy!"
        },
        {
            # "id_meal": 9,
            "name_meal": "Tofu Hotpot",
            "description_meal":"A comforting broth filled with tender tofu and assorted vegetables, seasoned with soy sauce.",
            "recipe_meal":"1. Prepare a broth by boiling water with kombu (dried kelp) and dried shiitake mushrooms.\n2. Add sliced tofu, vegetables like napa cabbage, mushrooms, and tofu pockets (if available) to the broth.\n3. Season with soy sauce and salt to taste.\n4. Simmer until the vegetables are tender and the tofu is heated through.\n5. Serve and enjoy!"
        },
        {
            # "id_meal": 10,
            "name_meal": "Steamed Dumplings",
            "description_meal":"Delicate dumplings filled with a savory mix of ground meat and vegetables, steamed to perfection.",
            "recipe_meal":"1. Prepare a filling by mixing ground meat (such as pork or chicken), finely chopped vegetables, soy sauce, sesame oil, and ginger.\n2. Place a spoonful of filling onto dumpling wrappers and fold to seal.\n3. Arrange dumplings in a steamer basket and steam for about 10-15 minutes until cooked through.\n4. Serve and enjoy!"
        },
    ]

    mealhistory_seeder = [
          {
            # "id_meal_history": 1,
            "notes_meal_history": "this is my jam",
          },
          {
            # "id_meal_history": 2,
            "notes_meal_history": "this is also my jam",
          },
          {
            # "id_meal_history": 1,
            "notes_meal_history": "",
          },
          {
            # "id_meal_history": 2,
            "notes_meal_history": "",
          },
    ]


    controller = Controller("src/database/nomnom.db")

    for ingredient in ingredient_seeder:
         controller.create_ingredient(ingredient)

    # for jadwalmakanan in jadwalmakanan_seeder:
    #      controller.create_jadwalmakanan(jadwalmakanan)
    
    for meal in meal_seeder:
         controller.create_meal(meal)

    # for mealhistory in mealhistory_seeder:
    #      controller.create_mealhistory(mealhistory)

    controller.generate_random_schedule(50)

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d")
    controller.get_jadwalmakanan_by_date(now)

    # create a connection to the database
    conn = sqlite3.connect("src/database/nomnom.db")

    # create a cursor object
    c = conn.cursor()




    c.execute("SELECT * FROM meal")

    # # fetch all the rows from the result set
    rows = c.fetchall()
    for row in rows:
        print(row)

    # # execute a SELECT statement to retrieve data from the meal table
    c.execute("SELECT * FROM jadwal_makanan_has_meal")

    # # fetch all the rows from the result set
    rows = c.fetchall()
    for row in rows:
        print(row)
    

    c.execute("SELECT * FROM jadwalmakanan")

    # # fetch all the rows from the result set
    rows = c.fetchall()
    for row in rows:
        print(row)


    c.execute("SELECT * FROM meal_history_has_jadwal_makanan")

    # # fetch all the rows from the result set
    rows = c.fetchall()
    for row in rows:
        print(row)
  
    c.execute("SELECT * FROM mealhistory")

    # # fetch all the rows from the result set
    rows = c.fetchall()
    for row in rows:
        print(row)