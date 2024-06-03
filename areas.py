import os

def main():
    # The main loop of the system
    while True:
        clear_terminal()
        print("AREAS")
        print("Select the figure of which you wish to get the AREA")
        # Prompt the user to choice a figure
        print_figures()
        choice = get_valid_option(["S", "R","T","E","C"])
        area = 0.0
        figure = ""
        try:
            match choice:
                case "S": #Square
                    area = square_area()
                    figure = "SQUARE"
                case "R": #Rectangle
                    area = rectangle_area()
                    figure = "RECTANGLE"
                case "T":
                    area = triangle_area() # Triangle
                    figure = "TRIANGLE"
                case "C":
                    area = circle_area() # Circle
                    figure = "CIRCLE"
                case "E":
                    return
            if area == EOFError: # If ctrl -z has been introduced
                raise EOFError
            print(f"THE AREA OF THE {figure} IS EQUAL TO: {area}")
            print("Do you want to comeback to the menu (Y for yes | N for get out of the system): ")
            comeback = get_valid_option(["Y", "N"])
            if comeback == "Y":
                continue
            if comeback == "N":
                return
        except EOFError: # To comeback to the menu
            continue
        
def print_figures():
    # Function that prints the available options
    print("[S] for square")
    print("[R] for rectangle")
    print("[T] for triangle")
    print("[C] for circle")
    print("[E] for exit")
    
def get_valid_option(options):
    # Function that recieves a list of str which contains the available options for the user to prompt
    # Returns a char with the user's choice
    user_choice = ""
    # Loop to prompt the user until it introduces a valid option
    while True:
        try:
            user_choice = input("Introduce a valid choice: ")
            user_choice = user_choice.upper()
            if user_choice not in options:
                continue
            break
        except EOFError:
            continue
    return user_choice

def square_area():
    #Function that calcules the area of a square
    clear_terminal()
    print("SQUARE")
    print("CTRL - Z to comeback to the menu")
    while True:
        try:
            #Prompt the user for the numeric value of the SIDE
            side = float(input("SIDE: "))
            if side <= 0.0:
                print("The value of te side must be greater than 0")
                raise ValueError
            return side * side 
        except ValueError:
            continue
        except EOFError:
            return EOFError
        
def get_base_height():
    # A function that prompts the user for the height and the base of certain figures
    while True:
        try:
            base = float(input("BASE: "))
            if base <= 0.0: # If the user has introduced either 0 or a negative value
                print("THE BASE MUST BE GREATER THAN 0")
                raise ValueError
            height = float(input("HEIGHT: "))
            if height <= 0.0: # Same as up
                print("THE HEIGHT MUST BE GREATER THAN 0")
                raise ValueError
            break
        except ValueError:
            continue
    # If no exceptions occurred then:
    return base, height

def rectangle_area():
    # Function that calcule the area of a rectangle
    clear_terminal()
    print("RECTANGLE")
    print("Ctrl - Z for comeback to the menu")
    try:
        # Prompt the user for the base and the height
        base, height = get_base_height()
        return base * height
    except EOFError:
        return EOFError
    
def triangle_area():
    # Function that calcules the area of a triangle
    clear_terminal()
    print("TRIANGLE")
    print("Ctrl - Z for comeback to the menu")
    try:
        # Get the base and the height with its function
        base, height = get_base_height()
        return (base * height) / 2
    except EOFError:
        return EOFError
        

def circle_area():
    # Get the area of a circle
    clear_terminal()
    print("CIRCLE")
    print("CTRL - Z to comeback to the MENU")
    while True:
        try:
            # Prompt the user for the radio 
            radio = float(input("RADIO: "))
            if radio <= 0.0:
                raise ValueError
            # Call pi from the function calcule pi
            pi = 3.1416
            return pi * (radio * radio)
        except ValueError:
            print("INVALID RADIO")
            continue
        except EOFError:
            return EOFError
        
def clear_terminal():
    # A function to clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__": 
    # Call the main function
    main()