import sqlite3

# Function to add new exercises category
def add_exercise_category():
    """
    Function to add a new exercise category to the database.

    This function prompts the user to enter details of a new exercise category,
    including exercise name, category, number of reps, and number of sets.
    It then inserts the exercise details into the 'exercises' table in the database.

    Args:
        None

    Returns:
        None
    """
    try:
        # Opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        c = db_conn.cursor()

        # Adding the new exercise to the table
        name = input('Enter exercise name: ')
        category = input('Enter exercise category: ')
        
        # This is to avoid program crashing from invalid number entries
        while True:
            try:
                reps = int(input('Enter number of reps: '))
                break
            except ValueError:
                print("You have NOT entered a number. Please enter a number for reps.")
                print("")
                continue
                       
        # This is to avoid program crashing from invalid number entries
        while True:
            try:
                sets = int(input('Enter number of sets: '))
                break
            except ValueError:
                print("You have NOT entered a number. Please enter a number for sets") 
                print("")
                continue
       
        # Inserting exercises into table
        c.execute('INSERT INTO exercises (name, category, reps, sets) VALUES (?, ?, ?, ?)', (name, category, reps, sets))
        print()
        print("Exercise added successfully")
        db_conn.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        db_conn.rollback()
        raise e
    finally:
        # Close the db connection
        db_conn.close()

