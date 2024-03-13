import sqlite3

# Function to view exercises by category from database
def view_exercise_by_category():
    """
    Function to view exercises by category from the database.

    This function prompts the user to enter the category of exercises they want to view. The  
    function first fetch categories from the 'exercises' table in the database.
    It retrieves exercises from the 'exercises' table that belong to the specified category.
    It then prints the exercises along with their reps and sets in a formatted table.

    Args:
        None

    Returns:
        None
    """
    # Fetching categories from the database
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching distinct categories from the 'exercises' table
        c.execute('SELECT DISTINCT category FROM exercises')
        categories = c.fetchall()
        
        fetched_categories = [category[0] for category in categories]

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()
    
    
    try:               
        # Prompting the user to enter the category to view
        print("Your exercise categories:")
        for i, category in enumerate(fetched_categories, 1):
            print(f"{i}. {category}")
        
        category_choice = int(input("Enter your choice number corresponding to the category you want to view: "))
        if category_choice > 0 and category_choice <= len(fetched_categories):
            selected_category = fetched_categories[category_choice - 1]
            # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
            db_conn = sqlite3.connect('fitness_tracker_app.db')
            # Get a cursor object
            c = db_conn.cursor()

            c.execute('SELECT * FROM exercises WHERE category = ?', (selected_category,))
            exercises = c.fetchall()

            if exercises:
                print(f"Exercises for {selected_category}:")
                print("{:<20} {:<20} {:<10} {:<10}".format("Exercise ID", "Exercise", "Reps", "Sets"))
                for exercise in exercises:
                    print("{:<20} {:<20} {:<10} {:<10}".format(exercise[0], exercise[1], exercise[3], exercise[4]))
 
            else:
                print("No exercises found for the category. Please enter a correct fitness category.")
                print("")
        else:
            print("Invalid choice. Please enter a valid number corresponding to the category.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()

