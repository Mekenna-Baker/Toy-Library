"""This script represents a toy library"""

# Define the toy library collection globally
toy_library = [
    {
        "toy": "Barbie Extra Fashion Doll with Afro-Puffs",
        "type": "Doll",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 24.75
    },
    {
        "toy": "Forbidden Island",
        "type": "Board Game",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 19.99
    },
    {
        "toy": "LEGO Minecraft The Axolotl House",
        "type": "Building Set",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 29.99
    }
]


# TODO: Define the checkout function
# This function changes the status of a toy to Checked Out, and updates its attributes

def checkout(toy_index):
    toy = toy_library[toy_index]
    if toy['status'] == 'Available':
        toy['status'] = 'Checked Out'
        toy['checkout_date'] = 'Checkout out now'
        toy['due_date'] = 'Due in 14 days'
        toy['checkout_count'] += 1
        return True
    else:
        return False


# TODO: Define the return_toy function
# This function changes resets the status of a toy, and removes its checkout information

def return_toy(toy_index):
    toy = toy_library[toy_index]
    if toy['status'] == 'Checked Out':
        toy['status'] = 'Available'
        toy['checkout_date'] = ''
        toy['due_date'] = ''
        return True
    else:
        return False
        

# TODO: Define the add_toy function
# This function creates a new toy dictionary and appends it to the toy library

def add_toy(toy_name, toy_type='', status='Available', replacement_cost=0.0):
    new_toy = {
        'toy': toy_name,
        'type': toy_type,
        'status': status,
        'checkout_date': '',
        'due_date': '',
        'checkout_count': 0,
        'replacement_cost': replacement_cost
    }
    toy_library.append(new_toy)


# TODO: Define the remove_toy function
# This function removes a toy by its index

def remove_toy(toy_index):
    if 0 <= toy_index < len(toy_library):
        return toy_library.pop(toy_index)
    return None

# TODO: Define the print library function
# This function prints the toy library items

def print_library(library):
    print('\nToy Library:')
    for idx, toy in enumerate(toy_library):
        print(f"{idx + 1}. {toy['toy']} - {toy['type']} - {toy['status']}")


# TODO: Define a function to check if the user input is in the toy library
# This function looks to see if a toy is in the library and returns the index if found
# 

def in_library(toy_name):
    for idx, toy in enumerate(toy_library):
        if toy['toy'].lower() == toy_name.lower():
            return idx
    return None

# Define the main function
if __name__ == "__main__":

    library_menu = {
        "1": "Checkout a Toy",
        "2": "Return a Toy",
        "3": "View Toy Library",
        "4": "View Detailed Toy Library",
        "5": "Add a Toy",
        "6": "Remove a Toy",
        "7": "Exit"
    }

    # Print the library menu
    print("Welcome to the Toy Library!")

    # TODO: Implement the main menu loop

    # Prompt user to enter a toy index
    while True:
        print('\nMenu:')
        for key, value in library_menu.items():
            print(f"{key}. {value}")

            choice = input('\nEnter  your choice: ').strip()

            #  checkout a toy
            if choice == '1':
                print_library()
                toy_index = int(input('Enter the toy number you want to checkout: ')) - 1
                if 0 <= toy_index < len(toy_library) and checkout(toy_index):
                    print(f"Successfully checked out '{toy_library[toy_index]['toy']}'!")
                else:
                    print("Sorry, that toy is not available to checkout.")

            # Return a toy
            elif choice == '2':
                print_library()
                toy_index = int(input('Enter the toy number you want to return: ')) - 1
                if 0 <= toy_index < len(toy_library) and return_toy(toy_index):
                    print(f"Successfully returned '{toy_library[toy_index]['toy']}'!")
                else:
                    print("Sorry, failed to return toy. It may not be checked out.")

            # View Toy Library
            elif choice == '3':
                print_library()

            #Add a toy 
            elif choice == '4':
                toy_name = input('Enter the toy name: ').strip()
                toy_type = input('Enter the toy type: ').strip()
                replacement_cost = float(input('Enter the replacement cost: '))
                add_toy(toy_name, toy_type, replacement_cost=replacement_cost)
                print(f'Added {toy_name} to the library.')
            
            # Remove a toy
            elif choice == '5':
                print_library()
                toy_index = int(input('Enter the toy number you want to remove: ')) - 1
                removed_toy = remove_toy(toy_index)
                if removed_toy:
                    print(f"Successfully removed '{removed_toy['toy']}' from the library.")
                else:
                    print("Sorry, failed to remove toy. Invalid index.")

            # Exit
            elif choice == '6':
                print('Thank you for vising the Toy  Library! Goodbye!')
                # End the loop
                break 

            else:
                print('Invalid choice. Please try again.')



