from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" course added successfully.")
    except sqlite3.IntegrityError:
        print(" unit must be unique.")
    conn.close()


def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def advance_search_user(user_id, name):
    conn = create_connection()
    cursor = conn.cursor()   
    cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", (user_id, '%' + name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',) )
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
