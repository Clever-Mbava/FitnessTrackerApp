from create_table import create_table
from add_exercise_category import add_exercise_category
from view_exercise_by_category import view_exercise_by_category
from delete_exercise_by_category import delete_exercise_by_category
from log_exercises import log_exercises
from create_workout_routine import create_workout_routine
from view_workout_routine import view_workout_routine
from view_exercise_progress import view_exercise_progress
from set_fitness_goals import set_fitness_goals
from view_progress_towards_fitness_goals import view_progress_towards_fitness_goals

def fitness_tracker_app():
    """
    Function to run the fitness tracker app.

    This function allows the user to interact with the fitness tracker app.
    The menu displayed allows the user to choose functions for adding exercise categories, viewing
    exercises by category, deleting exercises by category, logging completed exercises, creating workout routines,
    viewing workout routines, viewing exercise progress, setting fitness goals, viewing progress towards fitness goals,
    and quitting the program.

    Args:
        None

    Returns:
        None
    """
    try:
        # We call function to create tables in the database 
        create_table()  
        while True:
            print("=" * 40)
            print("         Fitness tracker app          ")
            print("=" * 40)
            print("1. Add exercise category")
            print("2. View exercises by category")
            print("3. Delete exercise by category")
            print("4. Log completed exercises")
            print("5. Create Workout Routine")
            print("6. View Workout Routine")
            print("7. View Exercise Progress")
            print("8. Set Fitness Goals")
            print("9. View Progress towards Fitness Goals")
            print("10. Quit")
            print("=" * 40)
            choice = input("Enter your choice: ")
            print()
            
            if choice == '1':
                add_exercise_category()
            
            elif choice == '2':
                view_exercise_by_category()

            elif choice == '3':            
                delete_exercise_by_category()
                
            elif choice == '4':
                log_exercises()
            
            elif choice == '5':
                create_workout_routine()

            elif choice == '6':
                view_workout_routine()
            
            elif choice == '7':
                view_exercise_progress()

            elif choice == '8':
                set_fitness_goals()

            elif choice == '9':
                view_progress_towards_fitness_goals()
                
            elif choice == '10':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")
                print("")
    except Exception as e:
        print("An error occurred:", e)
        print("Exiting program.")
