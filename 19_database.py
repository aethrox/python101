# Database Programming

import sqlite3

# connection = sqlite3.connect("mydata.db")

# cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#   first_name TEXT,
#   last_name TEXT,
#   age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
# ('Paul', 'Smith', 24),
# ('Mark', 'Johnson', 42),
# ('Anna', 'Smith', 34)
# """)

# cursor.execute("""
# SELECT * FROM persons
# WHERE last_name = 'Smith'
# """)

# rows = cursor.fetchall()
# print(rows)

# connection.commit()

# connection.close()


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('persons.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
          first_name TEXT,
          last_name TEXT,
          age INTEGER
        )
        """)

    def load_persons(self):
        self.cursor.execute("""
        SELECT * FROM persons
        """)

        result = self.cursor.fetchall()

        return result

    def add_person(self, first_name, last_name, age):
        self.cursor.execute("INSERT INTO persons VALUES ('{}', '{}', {})".format(first_name, last_name, age))
        self.connection.commit()

    def connectionStop(self):
        self.connection.close()
        print("Connection stopped.")

person_name = input("Person name: ")
person_lastname = input("Person last name: ")
person_age = input("Person age: ")

db = Database()
db.add_person(person_name, person_lastname, person_age)
print(db.load_persons())
db.connectionStop()