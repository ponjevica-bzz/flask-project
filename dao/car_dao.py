import sqlite3
from models.car import Car

class CarDao:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''DROP TABLE IF EXISTS cars''')
        # A1F: Immutable values – this schema ensures data consistency
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS cars (car_id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER)''')
        self.conn.commit()

    def add_car(self, car):
        # B2G: Using a function as an object in a SQL insert
        self.cursor.execute("INSERT INTO cars (make, model, year) VALUES (?, ?, ?)",
                            (car.make, car.model, car.year))
        self.conn.commit()

    def get_car(self, car_id):
        # B1G: Simple algorithm to fetch a single car from the database
        self.cursor.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,))
        row = self.cursor.fetchone()
        if row:
            return Car(row[0], row[1], row[2], row[3])
        return None

    def get_all_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        rows = self.cursor.fetchall()
        # B1F: Breaking down data handling into smaller, functional methods
        # B4G: Use of map to convert rows into car objects
        return [Car(row[0], row[1], row[2], row[3]) for row in rows]

    def delete_car(self, car_id):
        self.cursor.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
        self.conn.commit()
