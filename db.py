import sqlite3
from datetime import datetime
# Since we are now closing connections we need a new cursor each time

# conn = sqlite3.connect() - Get your own connection
# cursor = conn.cursor() - Get your cursor
# CREATE TABLE IF NOT EXISTS - Make sure table exists
# Do your work
# conn.close() - Clean up

def getConnection():
    #API idea .connects (DB, how to handle dateime objects) 
    #detect_types=sqlite3.PARSE_DECLTYPES, SQLite will automatically convert the DATE column back to a Python 
    # date object when you retrieve it. So row[2] should already be a date object, not a string.
    conn = sqlite3.connect("todo.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    return conn


def databasecheck():
    conn = getConnection()
    cursor = conn.cursor()
    # ensuring that a db exist
    # PARSE_DECLTYPES, SQLite will automatically convert 0/1 back to False/True 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due DATE NOT NULL,
        description TEXT,
        isComplete BOOLEAN DEFAULT FALSE 
    )
    ''')
    conn.commit()  # Don't forget to commit!
    conn.close()   # Clean up


def addTask(task):
    #print(f"Adding task: {task.title}, {task.due}, {task.description}")
    conn = getConnection()
    cursor = conn.cursor() #create a cursor on the DB

    #add in task now
    cursor.execute('''
    INSERT INTO tasks (title, due, description)
    VALUES(?,?,?)
    ''', (task.title, task.due, task.description))
    
    task_id = cursor.lastrowid # Get the auto-generated ID
    conn.commit()
    conn.close()  # Clean up
    return task_id # return id to auto add into the memory

def get_all_task():
    databasecheck() #ensures db exist from getgo

    # Each function gets its own connection
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows


def updateCompletedTask(task_id):
    # no need to check if db exist
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET isComplete = ? WHERE id = ?", (True, task_id)) # task_id is param and it should now be True
    conn.commit()
    conn.close()
