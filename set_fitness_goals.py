import sqlite3

# Function to set fitness goals
def set_fitness_goals():
    """
    Function to set fitness goals by adding them to the 'fitness_goals' table in the fitness tracker database.

    This function prompts the user to enter the name, category, and target for the fitness goal.
    It then inserts the goal into the 'fitness_goals' table with the provided name, category, and target.
    After successfully adding the goal, it prints a success message.

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
        
        # Adding the new goal to the table
        name = input('Enter goal name-Example upperbody-1000: ')
        category = input('Enter goal category: ')
        
        while True:
            try:
                target = int(input('Enter goal target: '))
                break
            except ValueError:
                print("You have NOT entered a valid number. Please enter a number for the target.")
                print("")
                continue
        
        c.execute('INSERT INTO fitness_goals (name, category, target) VALUES (?, ?, ?)', (name, category, target))
        print("Fitness goal added successfully")
        print("")
        
        db_conn.commit()
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()

