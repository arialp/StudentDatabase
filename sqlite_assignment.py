import sqlite3  # Import the sqlite3 module


def add_student(name, age, email):  # Add a student to the database
    conn = sqlite3.connect("myDatabase.db")  # Create a connection object to the database file
    cur = conn.cursor()  # Create a cursor object to execute SQL commands
    cur.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    print("Student added successfully.\n")
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the connection


def update_age(id, age):  # Update the age of a student
    conn = sqlite3.connect("myDatabase.db")
    cur = conn.cursor()
    # Update the age of the student with the given id
    cur.execute("UPDATE students SET age = ? WHERE id = ?", (age, id))
    print("Student's age updated successfully.\n")
    conn.commit()
    conn.close()


def delete_student(id):  # Delete a student from the database
    conn = sqlite3.connect("myDatabase.db")
    cur = conn.cursor()
    # Delete the student with the given id
    cur.execute("DELETE FROM students WHERE id = ?", (id,))
    print("Student deleted successfully.\n")
    conn.commit()
    conn.close()


def get_all_students():  # List all students in the database as a dictionary
    try:
        conn = sqlite3.connect("myDatabase.db")
        conn.row_factory = sqlite3.Row  # Set the row_factory attribute to sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")  # Get all the students from the table
        rows = cur.fetchall()  # Fetch all the rows from the result set
        data = {}
        for row in rows:
            key = row["id"]
            # Get the other columns as a sub-dictionary
            value = {"name": row["name"], "age": row["age"], "email": row["email"]}
            data[key] = value
        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def get_student(id):  # Get a student from the database as a dictionary
    try:
        conn = sqlite3.connect("myDatabase.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", (id,))  # Get the student with the given id
        row = cur.fetchone()  # Fetch one row from the result set
        conn.close()
        if row is None:
            return None
        else:
            return {"name": row["name"], "age": row["age"], "email": row["email"]}  # Return the student as a dictionary
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def average_age():  # Get the average age of all students
    try:
        conn = sqlite3.connect("myDatabase.db")
        cur = conn.cursor()
        cur.execute("SELECT AVG(age) FROM students")  # Get the average age from the table
        row = cur.fetchone()
        conn.close()
        return row[0]  # Return the average age as a float
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def number_of_students():  # Get the number of students
    try:
        conn = sqlite3.connect("myDatabase.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM students")  # Get the number of students from the table
        row = cur.fetchone()
        conn.close()
        return row[0]  # Return the number of students as an integer
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def select_option(options):  # Ask the user to select an option from a list
    for i, option in enumerate(options):
        print(f"[{i}] {option}")
    index = int(input("Enter the index of your choice: "))
    return index


# Create a table called "students" with four columns, only if it does not exist
conn = sqlite3.connect("myDatabase.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)")


# Ask the user to select an option
options = ["Add a student", "Update the age of a student", "Delete a student", "List all students", "Get a student", "Get the average age of all students", "Get the number of students", "Exit"]
index = select_option(options)

while index != 7:
    # Call the appropriate function based on the user's choice
    if index == 0:
        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")
        add_student(name, age, email)
    elif index == 1:
        id = int(input("ID: "))
        age = int(input("Age: "))
        update_age(id, age)
    elif index == 2:
        id = int(input("ID: "))
        delete_student(id)
    elif index == 3:
        print(get_all_students(), "\n")
    elif index == 4:
        id = int(input("ID: "))
        print(get_student(id), "\n")
    elif index == 5:
        print("Average age is:", average_age(), "\n")
    elif index == 6:
        print("Total number of students:", number_of_students(), "\n")
    elif index == 7:
        conn.commit()
        conn.close()
        exit()
    index = select_option(options)  # Ask the user to select another option

conn.commit()
conn.close()
