import os
from unittest import case

import numpy as np

print("Hello! Welcome to the Contact Number! \n")

contact_numbers = np.array([])
loaded_txt = np.loadtxt('contact_numbers.txt', dtype=str)
while True:
    os.system("cls")
    print("Please Choose what you want to do:")
    print("1. Add a contact number")
    print("2. View a contact number")
    print("3. Select a contact number")
    print("4. Edit a contact number")
    print("5. Delete a contact number")
    print("6. Exit \n\n")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter the name of the contact: ")
            number = input("Enter the contact number: ")
            contact_numbers = np.append(contact_numbers, f"{name}:{number}")
            np.savetxt('contact_numbers.txt', contact_numbers, fmt='%s')
            print("Contact added successfully!")
        case 2:
            print("Loaded from text:", loaded_txt)
        case 3:
            name = input("Enter the name of the contact: ")

            if name in loaded_txt:
                for item in loaded_txt:
                    if item.startswith(name + ":"):
                        print(f"{name}'s contact number is: {item.split(':')[1]}")
                        break
            else:
                print("Contact not found.")

        case 4:
            name = input("Enter the name of the contact: ")

            if name in loaded_txt:
                new_number = input("Enter the new contact number: ")
                updated_numbers = []
                for item in loaded_txt:
                    if item.startswith(name + ":"):
                        updated_numbers.append(f"{name}:{new_number}")
                    else:
                        updated_numbers.append(item)
                np.savetxt('contact_numbers.txt', updated_numbers, fmt='%s')
                print("Contact number updated successfully!")
            else:
                print("Contact not found.")
        case 5:
            name = input("Enter the name of the contact: ")
            
            if name in loaded_txt:
                updated_numbers = []
                for item in loaded_txt:
                    if not item.startswith(name + ":"):
                        updated_numbers.append(item)
                np.savetxt('contact_numbers.txt', updated_numbers, fmt='%s')
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")
        case 6:
            print("Exiting the program. Goodbye!")
        case _:
            print("Invalid choice. Please try again.")

    goBack = input("Do you want to perform another operation? (yes/no) : ")

    if goBack.lower() != "yes":
        print("Exiting the program. Goodbye!")
        break
