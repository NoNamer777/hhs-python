from sqlite3 import *
from ..models import Student


class DatabaseConnection:
    def __init__(self):
        self._connection = connect(':memory:')

        self.prepare_db()

    def prepare_db(self):
        # Create Student table
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR(24) NOT NULL,
                lastname VARCHAR(24) NOT NULL,
                UNIQUE (firstname, lastname)
            );""")
        self.connection.commit()

        # Provide some data
        self.connection.execute("""
            INSERT INTO student (firstname, lastname) VALUES
                ('Ted', 'Anthony'),
                ('Alice', 'Woodward'),
                ('Venessa', 'Chambers'),
                ('Scoot', 'Booth'),
                ('Lester', 'Burris'),
                ('Mark', 'Griffin');
        """)
        self.connection.commit()

    def get_students(self):
        students = []
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM student""")

        rows = cursor.fetchall()

        for row in rows:
            students.append(Student({'firstname': row[1], 'lastname': row[2]}))

        return students

    @property
    def connection(self):
        return self._connection
