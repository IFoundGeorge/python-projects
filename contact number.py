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
    print("3. Edit a contact number")
    print("4. Delete a contact number")
    print("5. Exit \n\n")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter the name of the contact: ")
            number = input("Enter the contact number: ")
            contact_numbers = np.append(contact_numbers, f"{name}:{number}")
            np.savetxt('contact_numbers.txt', contact_numbers, fmt='%s')
            print("Contact added successfully!")
        case 2:
            loaded_txt = np.loadtxt('contact_numbers.txt', dtype=str)  # reload latest data
            print("Loaded contacts:", loaded_txt, "\n") 
        case 3:
            loaded_txt = np.atleast_1d(np.loadtxt('contact_numbers.txt', dtype=str))
            print("Loaded contacts:", loaded_txt, "\n")

            name = input("Enter the name of the contact to edit: ")

            matches = np.char.startswith(loaded_txt, name + ":")

            if np.any(matches):
                new_number = input("Enter the new contact number: ")
                updated_numbers = np.where(matches, f"{name}:{new_number}", loaded_txt)
                np.savetxt('contact_numbers.txt', updated_numbers, fmt='%s')
                print("Contact number updated successfully!")
            else:
                print("Contact not found.")
        case 4:
            loaded_txt = np.atleast_1d(np.loadtxt('contact_numbers.txt', dtype=str))
            print("Loaded contacts:", loaded_txt, "\n")

            name = input("Enter the name of the contact to delete: ")

            matches = np.char.startswith(loaded_txt, name + ":")

            if np.any(matches):
                updated_numbers = loaded_txt[~matches]
                np.savetxt('contact_numbers.txt', updated_numbers, fmt='%s')
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")
        case 5:
            print("Exiting the program. Goodbye!")
        case _:
            print("Invalid choice. Please try again.")

    goBack = input("Do you want to perform another operation? (yes/no) : ")

    if goBack.lower() != "yes":
        print("Exiting the program. Goodbye!")
        break
