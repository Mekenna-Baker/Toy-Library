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

def remove_toy(toy_index):
    if 0 <= toy_index < len(toy_library):
        return toy_library.pop(toy_index)
    return None

# TODO: Define the print library function


# TODO: Define a function to check if the user input is in the toy library


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