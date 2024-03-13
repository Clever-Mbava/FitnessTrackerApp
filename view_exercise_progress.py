import sqlite3

def fetch_exercise_names():
    """
    Function to fetch exercise names from the 'exercises' table in the database.

    Returns:
        list: A list of exercise names.
    """
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching exercise names from the 'exercises' table
        c.execute('SELECT name FROM exercises')
        exercises = c.fetchall()
        return [exercise[0] for exercise in exercises]

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()

# Function to view exercise progress
def view_exercise_progress():
    """
    Function to view exercise progress from the database.

    This function prompts the user to enter the exercise they want to view progress for.
    It retrieves the exercise details from the 'exercises' table and completed sets from the 'completed_exercises' table.
    It then calculates the progress based on the completed sets and total sets required for the exercise,
    and prints the progress percentage along with the exercise details.

    Args:
        None

    Returns:
        None
    """
    
    # Fetching exercise names from the database
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching exercises from the 'exercises' table
        c.execute('SELECT id, name FROM completed_exercises')
        exercises = c.fetchall()
        fetched_exercises = [(exercise[0], exercise[1]) for exercise in exercises]

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()
    
    try:
        # Prompting the user to enter the exercise to view
        print("Available completed exercises:")
        for i, (exercise_id, exercise_name) in enumerate(fetched_exercises, 1):
            print(f"{i}. {exercise_name}")
        
        exercise_choice = int(input("Enter your choice number corresponding to the exercise you want to view progress for: "))
        if exercise_choice > 0 and exercise_choice <= len(fetched_exercises):
            selected_exercise_id, selected_exercise_name = fetched_exercises[exercise_choice - 1]
            # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
            db_conn = sqlite3.connect('fitness_tracker_app.db')
            # Get a cursor object
            c = db_conn.cursor()

            c.execute('SELECT * FROM exercises WHERE id = ?', (selected_exercise_id,))
            exercise = c.fetchone()

            if exercise:
                sets_count = exercise[4]
                c.execute('SELECT * FROM completed_exercises WHERE name = ?', (selected_exercise_name,))
                completed_sets = c.fetchone()

                if completed_sets:
                    completed_sets_count = completed_sets[3]
                    progress = (completed_sets_count / sets_count) * 100
                    print(f"Exercise: {selected_exercise_name}")
                    print(f"Progress: {progress:.2f}% (Completed Sets: {completed_sets_count}/{sets_count})")
                    print("")
                else:
                    print("No completed sets found for this exercise. Please first log completed sets for this exercise")
                    print("")
            else:
                print("Exercise not found.")
        else:
            print("Invalid choice. Please enter a valid number corresponding to the exercise.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()
