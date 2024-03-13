import sqlite3

# Function to delete exercise the database
def delete_exercise_by_category(): 
    """
    Function to delete exercises from the 'exercises' table by category.

    This function prompts the user to enter a category and an exercise name to delete.
    It then deletes the exercise with the provided name and category from the 'exercises' table.

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
        
        category = input('Enter category to delete: ')
        exercise_to_delete = input('Enter exercise to delete: ')
        
        c.execute('DELETE FROM exercises WHERE category=? AND name=?',(category, exercise_to_delete,))
        if c.rowcount > 0:
            print("Exercise deleted successfully")
            print("")
        else:
            print("No exercise found matching the category")
            print("")     
    except sqlite3.OperationalError as e:
        print("Error: ", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    except Exception as e:
        # Roll back any change if something goes wrong
        db_conn.rollback()
        raise e
    finally:
        # Close the db connection
        db_conn.close()


