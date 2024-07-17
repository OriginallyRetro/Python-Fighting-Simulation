import os, time  # Importing the os and time modules for system operations and time delays

class Fighter:
    def __init__(self, name: str, attack: int, defense: int, health: int):
        """
        Initialize a new Fighter instance.

        :param name: Name of the fighter
        :param attack: Attack power of the fighter
        :param defense: Defense power of the fighter
        :param health: Health points of the fighter
        """
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
    
    def perform_attack(self, target) -> None:
        """
        Perform an attack on the target fighter.

        :param target: The fighter being attacked
        """
        if target.defense >= 0:
            target.defense -= self.attack  # Reduce the target's defense by the attack value
            
            if target.defense <= 0:
                target.defense = 0  # Ensure defense does not go below 0
                target.health -= self.attack  # If defense is zero, reduce the target's health
                
            if self.defense >= 0:
                self.defense -= target.attack  # Reduce self defense by the target's attack
            
            if self.defense <= 0:
                self.defense = 0  # Ensure defense does not go below 0
                self.health -= target.attack  # If self defense is zero, reduce own health

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")

def loading():
    """
    Display a loading message with a progress animation.
    """
    print("Made by Myles Cooke")
    time.sleep(1)
    print("Github: OriginallyRetro/Retrx")
    time.sleep(1)
    print("Hope you enjoy this python program")
    time.sleep(1)
    print("This is fighting text-based battles using OOP and class methods")
    time.sleep(1)
    print("Have a good day")
    time.sleep(1)
    input()  # Wait for user input before proceeding
    clear_screen()
    
    # Display a simple loading animation
    for _ in range(3):
        print("loading" + "." * (_ + 1))
        time.sleep(0.7)
        clear_screen()

def start():
    """Start the game."""
    loading()  # Display the loading screen
    # Create two fighter instances
    karate_man = Fighter(name="Karate Guy", attack=30, defense=100, health=200)
    streetfighter_man = Fighter(name="Street Fighter Guy", attack=20, defense=150, health=300)
    
    while True:
        clear_screen()  # Clear the screen for the next round
        # Each fighter attacks the other
        karate_man.perform_attack(streetfighter_man)
        streetfighter_man.perform_attack(karate_man)
        
        # Display the current health and defense of each fighter
        print(f"{karate_man.name} HP: {karate_man.health}\n===========================\n{karate_man.name} DEF: {karate_man.defense}")
        print("===================================================")
        print(f"{streetfighter_man.name} HP: {streetfighter_man.health}\n===========================\n{streetfighter_man.name} DEF: {streetfighter_man.defense}")
        
        # Break the loop if either fighter's health drops to 0 or below
        if karate_man.health <= 0 or streetfighter_man.health <= 0:
            break

        input("\nPress Enter to continue...")

    clear_screen()
    # Display the winner
    if karate_man.health > 0:
        print(" _________________________")
        print(f"| {karate_man.name.center(21)} |")
        print("|        WINS!             |")
        print(" |_______________________|")
    else:
        print(" ________________________________")
        print(f"| {streetfighter_man.name.center(30)} |")
        print("|          WINS!                 |")
        print(" |______________________________|")

start()  # Run the game
