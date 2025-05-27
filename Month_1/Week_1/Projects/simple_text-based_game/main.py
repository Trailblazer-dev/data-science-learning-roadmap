# text-based-game 

# text-based-game

def main():
    player_name = input("Welcome adventurer! What is your name? ")
    print(f"Hello, {player_name}! Your adventure begins now.")
    
    inventory = []
    health = 100
    
    # Start the adventure
    forest_entrance(player_name, inventory, health)
    
def forest_entrance(player_name, inventory, health):
    print("\nYou stand at the entrance of a dark forest.")
    print("There's a path going left and another going right.")
    print("Which way do you want to go?")
    
    choice = input("Left or Right? ").lower()
    
    if choice == "left":
        print("\nYou chose the left path.")
        print("The path leads deeper into the forest.")
        print("You hear strange noises coming from ahead.")
        
        second_choice = input("Do you want to continue forward or go back? (forward/back) ").lower()
        if second_choice == "forward":
            encounter_wolf(player_name, inventory, health)
        else:
            forest_entrance(player_name, inventory, health)
            
    elif choice == "right":
        print("\nYou chose the right path.")
        print("You come across a small cottage.")
        
        second_choice = input("Do you want to enter the cottage or continue on the path? (enter/continue) ").lower()
        if second_choice == "enter":
            enter_cottage(player_name, inventory, health)
        else:
            river_crossing(player_name, inventory, health)
            
    else:
        print("Invalid choice. Please choose Left or Right.")
        forest_entrance(player_name, inventory, health)

def encounter_wolf(player_name, inventory, health):
    print("\nYou encounter a large wolf blocking your path!")
    if "sword" in inventory:
        print("You draw your sword and the wolf runs away.")
        print("The path ahead leads to a treasure chest.")
        inventory.append("treasure")
        print("You found treasure! It's been added to your inventory.")
    else:
        print("The wolf attacks you!")
        health -= 30
        print(f"You take damage and run away. Health: {health}")
    
    # Return to the entrance
    forest_entrance(player_name, inventory, health)

def enter_cottage(player_name, inventory, health):
    print("\nInside the cottage, you find an old woman.")
    print("'Hello traveler,' she says. 'Take this sword. You'll need it.'")
    inventory.append("sword")
    print("Sword added to inventory!")
    
    # Return to the entrance
    forest_entrance(player_name, inventory, health)

def river_crossing(player_name, inventory, health):
    print("\nYou reach a river with a broken bridge.")
    print("You need to find another way to cross.")
    
    # Game continues...
    print("To be continued...")

if __name__ == "__main__":
    main()
    print("\nGame over.")
    print("Thanks for playing!")