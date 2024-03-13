import sqlite3

# Function to update book information
def log_exercises():
    """
    Function to log completed exercises.

    This function prompts the user to enter the name of the exercise they want to log. It retrieves
    the exercise information from the 'exercises' table based on the provided name, including the
    exercise ID, name, category, reps, and sets. It then prompts the user to enter the number of
    completed sets for the exercise and inserts this information into the 'completed_exercises' table.

    Args:
        None

    Returns:
        None
    """
    # Fetching exercise names and IDs from the database
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching exercises from the 'exercises' table
        c.execute('SELECT id, name FROM exercises')
        exercises = c.fetchall()
        fetched_exercises = {exercise[0]: exercise[1] for exercise in exercises}
        
        # Prompting the user to enter the exercise to view
        print("Available exercises:")
        for exercise_id, exercise_name in fetched_exercises.items():
            print(f"{exercise_id}. {exercise_name}")

        select_exercise_log_id = int(input("Please select exercise to log from your available list by entering its ID: "))

        if select_exercise_log_id not in fetched_exercises:
            print("You have entered invalid ID. Please select a valid ID from the exercise list shown")
            return

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()
    
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object    
        c = db_conn.cursor()
        
        exercise_name = fetched_exercises[select_exercise_log_id]
        c.execute('SELECT * FROM exercises WHERE name=?', (exercise_name,))
        exercise = c.fetchone()
        
        if exercise:
            print(f"You have chosen to log exercise {exercise[1]} with {exercise[3]} reps and {exercise[4]} sets to be completed")
            
            id = exercise[0]
            name = exercise[1]
            category = exercise[2]
           
            while True:
                try:
                    done_sets = int(input("Enter completed sets: "))
                    break
                except ValueError:
                    print("You have NOT entered a number. Please enter a number for sets")
                    print("")
                    continue
            
            c.execute('INSERT INTO completed_exercises (id, name, category, sets) VALUES (?, ?, ?, ?)', (id, name, category, done_sets))
            
            print("Exercise logged successfully")
            print("")
            db_conn.commit()
        else:
            print("Exercise not found")
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()
