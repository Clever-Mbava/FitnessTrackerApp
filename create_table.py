import sqlite3

# Function to create the database and table
def create_table():
    """
    Function to create the database tables for the fitness tracker app.

    This function creates or opens a SQLite3 database file named 'fitness_tracker_app.db'.
    It then creates four tables: 'exercises', 'workout_routines', 'fitness_goals', and 'completed_exercises'.
    The 'exercises' table stores details of exercises, including ID, name, category, number of reps, and number of sets.
    The 'workout_routines' table stores workout routines, consisting of a routine name and a list of exercises.
    The 'fitness_goals' table stores fitness goals, including goal name, category, and target (e.g., number of reps).
    The 'completed_exercises' table stores records of completed exercises, including exercise name, category, and sets completed.

    Args:
        None

    Returns:
        None
    """
    try:
        # Creates or opens a file called fitness_tracker_app with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Creating the exercise table
        c.execute('''CREATE TABLE IF NOT EXISTS exercises
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    reps INTEGER,
                    sets INTEGER
                  )''')
        
        # Creating workout routines table
        c.execute('''CREATE TABLE IF NOT EXISTS workout_routines
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    exercises TEXT
                  )''')
        
        # Creating fitness goals table
        c.execute('''CREATE TABLE IF NOT EXISTS fitness_goals
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    target INTEGER
                  )''')
        

        # Creating completed exercises table
        c.execute('''CREATE TABLE IF NOT EXISTS completed_exercises
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    sets INTEGER
                  )''')
        
        # Commit the changes
        db_conn.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        db_conn.rollback()
        raise e
    finally:
        # Close the db connection
        db_conn.close()
