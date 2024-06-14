# Import 'time' library
import time


# Display banner
print("\nWelcome to Treasure Island. Your mission is to find the treasure.")


# Store code for first stage in 'first()' (Function)
def first():
    while True:
        crossroad = input("\nYou are at a crossroad. Do you want to go left or right (left/right)?\n")
        crossroad = crossroad.lower()
        if crossroad == "left":
            print("\nYou walk down a path that leads you to a river.")
            second()
            break
        elif crossroad == "right":
            print("\nYou walk down a path that leads you into a dense forest. Unbeknownst to you, there was a mountain lion in the bushes. Out of a sudden, it lunges at you and attacks you. The mountain lion kills you. Game over.")
            break
        else:
            print("\nInvalid input. Only the listed options are accepted.")


# Store code for second stage in 'second()' (Function)
def second():
    while True:
        river = input("\nDo you want to swim across the river or use a wooden boat to cross the river (swim/boat)?\n")
        river = river.lower()
        if river == "swim":
            print("\nYou tried to swim across the river but got swept away by the strong current. You drowned. Game over.")
            break
        elif river == "boat":
            print("\nYou managed to cross the river using the boat.")
            third()
            break
        else:
            print("\nInvalid input. Only the listed options are accepted.")


# Store code for third stage in 'third()' (Function)
def third():
    while True:
        door = input("\nYou come across a building in the middle of the forest. The building has 3 doors. The first, the second and the third. Which door do you want to open (first/second/third)?\n")
        door = door.lower()
        if door == "first":
            print("\nYou open the door and a tiger lunges at you. The tiger kills you. Game over.")
            break
        elif door == "second":
            print("\nYou open the door and find a room full of gold. You win!")
            break
        elif door == "third":
            print("\nYou open the door and accidentally trigger a trap. An arrow is fired at you and it strikes you in your forehead. The shot kills you. Game over.")
            break
        else:
            print("\nInvalid input. Only the listed options are accepted.")


# Run 'first()'
first()


# Exit program
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)
