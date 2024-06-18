# Import 'time' library
import time


# Display welcome message
print("\nWelcome to Treasure Island. Your mission is to find the treasure.")


# Store code for first stage in 'first()' (Function)
def first():
    while True:


        # Get user's path selection and store it in 'crossroad' (String)
        crossroad = input("\nYou are at a crossroad. Do you want to go left or right (left/right)?\n").lower()


        # Execute code based on path selected
        if crossroad == "left":


            # Display message
            print("\nYou walk down a path that leads you to a river.")


            # Call 'second()'
            second()


            # Exit loop
            break
        elif crossroad == "right":


            # Display message
            print("\nYou walk down a path that leads you into a dense forest. Unbeknownst to you, there was a mountain lion in the bushes. Out of a sudden, it lunges at you and attacks you. The mountain lion kills you. Game over.")


            # Exit loop
            break
        else:


            # Display message
            print("\nInvalid input. Only the listed options are accepted.")


# Store code for second stage in 'second()' (Function)
def second():
    while True:


        # Get user's method selection and store it in 'river' (String)
        river = input("\nDo you want to swim across the river or use a wooden boat to cross the river (swim/boat)?\n").lower()


        # Execute code based on method selected
        if river == "swim":


            # Display message
            print("\nYou tried to swim across the river but got swept away by the strong current. You drowned. Game over.")


            # Exit loop
            break
        elif river == "boat":


            # Display message
            print("\nYou managed to cross the river using the boat.")


            # Call 'third()'
            third()


            # Exit loop
            break
        else:


            # Display message
            print("\nInvalid input. Only the listed options are accepted.")


# Store code for third stage in 'third()' (Function)
def third():
    while True:


        # Get user's door selection and store it in 'door' (String)
        door = input("\nYou come across a building in the middle of the forest. The building has 3 doors. The first, the second and the third. Which door do you want to open (first/second/third)?\n").lower()


        # Execute code based on door selected
        if door == "first":


            # Display message
            print("\nYou open the door and a tiger lunges at you. The tiger kills you. Game over.")


            # Exit loop
            break
        elif door == "second":


            # Display message
            print("\nYou open the door and find a room full of gold. You win!")


            # Exit loop
            break
        elif door == "third":


            # Display message
            print("\nYou open the door and accidentally trigger a trap. An arrow is fired at you and it strikes you in your forehead. The shot kills you. Game over.")


            # Exit loop
            break
        else:


            # Display message
            print("\nInvalid input. Only the listed options are accepted.")


# Call 'first()'
first()


# Display exit message
print("\nProgram exiting...")


# Exit program after 5 second delay
for delay in range(5):
    time.sleep(1)
