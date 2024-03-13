import sqlite3

# Function to create workout_routines
def create_workout_routine():
    """
    Function to create a new workout routine and add it to the 'workout_routines' table in the fitness tracker database.

    This function prompts the user to enter the name of the new workout routine and select exercises from a list.
    It then inserts the new routine into the 'workout_routines' table with the provided name and exercises.
    After successfully adding the routine, it prints a success message.

    Args:
        None

    Returns:
        None
    """
    
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object    
        c = db_conn.cursor()
        
        # Fetching exercise names from the 'exercises' table
        c.execute('SELECT name FROM exercises')
        exercises = c.fetchall()
        exercise_names = [exercise[0] for exercise in exercises]
              
        # Adding the new routine to the table
        name = input('Enter routine name: ')
        
        # Showing exercise list to the user
        print("Available exercises:")
        for i, exercise_name in enumerate(exercise_names, 1):
            print(f"{i}. {exercise_name}")
        
                
        # Prompting the user to select exercises
        selected_exercise_ids = input('Enter the number choices of exercises separated by commas: ')
        selected_exercise_ids = [int(index.strip()) for index in selected_exercise_ids.split(',')]
        
        selected_exercises = [exercise_names[index - 1] for index in selected_exercise_ids]
                
        c.execute('INSERT INTO workout_routines (name, exercises) VALUES (?, ?)', (name, ', '.join(selected_exercises)))
        print("Workout routine added successfully")
        print("")
        
        db_conn.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        db_conn.rollback()
        raise e
    finally:
        # Close the db connection
        db_conn.close()

