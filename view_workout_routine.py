import sqlite3

# Function to view workout routines
def view_workout_routine():
    """
    Function to view workout routines from the database.

    This function prompts the user to enter the name of the workout routine they want to view.
    It retrieves the workout routine from the 'workout_routines' table based on the provided name,
    and prints the name of the routine along with its exercises.

    Args:
        None

    Returns:
        None
    """
    
    # Fetching workout routine names and IDs from the database
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching workout routine names and IDs from the 'workout_routines' table
        c.execute('SELECT id, name FROM workout_routines')
        routines = c.fetchall()
        fetched_routines = [(routine[0], routine[1]) for routine in routines]

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()
    
    try:     
        # Prompting the user to enter the workout routine to view
        print("Available workout routines:")
        for index, (routine_id, routine_name) in enumerate(fetched_routines, 1):
            print(f"{index}. {routine_name}")
        
        routine_choice = int(input("Enter your choice number corresponding to the workout routine you want to view: "))
        if routine_choice > 0 and routine_choice <= len(fetched_routines):
            selected_routine_id, selected_routine_name = fetched_routines[routine_choice - 1]
            # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
            db_conn = sqlite3.connect('fitness_tracker_app.db')
            # Get a cursor object
            c = db_conn.cursor()

            c.execute('SELECT * FROM workout_routines WHERE id = ?', (selected_routine_id,))
            workout_routine = c.fetchone()

            if workout_routine:
                print(f"Workout Routine: {selected_routine_name}")
                print(f"Exercises: {workout_routine[2]}")
                print("")
            else:
                print("Workout routine not found.")
        else:
            print("Invalid choice. Please enter a valid number corresponding to the workout routine.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()

