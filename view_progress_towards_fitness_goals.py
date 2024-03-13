import sqlite3

# Function to view progress towards fitness goals
def view_progress_towards_fitness_goals():
    """
    Function to view progress towards fitness goals from the database.

    This function prompts the user to enter the fitness goal they want to view progress for.
    It retrieves the goal category and target from the 'fitness_goals' table.
    Then, it retrieves completed sets for the corresponding category from the 'completed_exercises' table,
    calculates the progress based on the completed sets and the target, and prints the progress percentage.

    Args:
        None

    Returns:
        None
    """
    # Fetching fitness goal names and IDs from the database
    try:
        # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
        db_conn = sqlite3.connect('fitness_tracker_app.db')
        # Get a cursor object
        c = db_conn.cursor()

        # Fetching fitness goal names and IDs from the 'fitness_goals' table
        c.execute('SELECT id, name FROM fitness_goals')
        goals = c.fetchall()
        fetched_goals = [(goal[0], goal[1]) for goal in goals]

    except Exception as e:
        print("An error occurred:", e)
        raise e
    finally:
        # Close the db connection
        db_conn.close()
    
    try:
        # Prompting the user to enter the fitness goal to view
        print("Available fitness goals:")
        for i, (goal_id, goal_name) in enumerate(fetched_goals, 1):
            print(f"{i}. {goal_name}")
        
        goal_choice = int(input("Enter your choice number corresponding to the fitness goal you want to view progress for: "))
        if goal_choice > 0 and goal_choice <= len(fetched_goals):
            selected_goal_id, selected_goal_name = fetched_goals[goal_choice - 1]
            # Creates or opens a file called fitness_tracker_app_db with a SQLite3 DB
            db_conn = sqlite3.connect('fitness_tracker_app.db')
            # Get a cursor object
            c = db_conn.cursor()

            c.execute('SELECT category, target FROM fitness_goals WHERE id = ?', (selected_goal_id,))
            goal = c.fetchone()

            if goal:
                category = goal[0]
                target = goal[1]

                c.execute('SELECT SUM(sets) FROM completed_exercises WHERE category = ?', (category,))
                total_completed_sets = c.fetchone()[0]

                if total_completed_sets is not None:
                    progress_percentage = (total_completed_sets / target) * 100
                    print(f"Progress towards {selected_goal_name}: {progress_percentage:.2f}% (Completed Sets: {(total_completed_sets / target)})")
                else:
                    print("No completed sets found for this category.")
            else:
                print("Fitness goal not found.")
        else:
            print("Invalid choice. Please enter a valid number corresponding to the fitness goal.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
        # Roll back any change if something goes wrong
        db_conn.rollback()
    finally:
        # Close the db connection
        db_conn.close()

