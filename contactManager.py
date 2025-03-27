# Global dictionary to store contacts

contacts_emails = []
contacts_phone = []
contacts_name = []
contacts_list = {}

def main():

    choice = int(input("Please select the option you'd like (1-6): "))

    while True: # This only took 40 minutes to properly fix <- This statement was a lie

        if choice == 1: # Outside adding things to the dictionary, it actually works
            
            contacts_name[name] = input("Please add the users contact name (or type done to be finished): ").strip() #Invalid syntax and I do not understand why

            if contacts_name[name] == 'done'.lower():
                return

            contacts_phone = input("Please add the users contact number (Please include dashes.): ").strip()
            
            contacts_emails = input("Please add the users contact email: ").strip()
 
            print("Contact added successfully!")
            
            profile = [contacts_name, contacts_emails, contacts_list].append 
        # I love when literally nothing works and I can't figure out why
        if choice == 2:  
            print("=-=-All Contacts-=-=") 
            print(f"Contact Name, Email and Number:", )
            print("-=-=-=-=-=-=-=-=-=-")
            return

        if choice == 3: # Still needs to be worked on 
            print("-=-Search For a Contact-=-")
            input("Please type the name you are searching for: ")
            if contacts_name[name] is not contacts_list{}:
                print("I'm sorry, the user you're looking for is not here.")
            else:
                print("This user is in your contacts.")
            

        if choice == 4: 
            print("-=-=Remove A Contact=-=-")
            print([contacts_list])
            input("Type the name of the contact you'd like to remove:", {contacts_name})
            if contacts_name[name] is not contacts_list[]:
                print("I'm sorry, the user you're looking for is not here.")
            else:
                contacts_list[contacts_name].pop
            # if input == 'y':

        if choice == 5:
            print("-=-=Update A Contact=-=-")
            print(contacts_name)
            print("Which contact would you like to update?: ") 
            
        
        if choice == 6:  
            print("Thank you for using this program, have a swell day!") 
            break 


def display_contacts_list():
    print(" -=-=-=-=-=-=-=-=- ")
    print("| Contact Manager |")
    print(" -=-=-=-=-=-=-=-=- ")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Update a contact")
    print("6. Quit") 
    print("-=-=-=-=-=-=-=-=-=-")

# Main function to run the menu-driven system


if __name__ == "__main__":
    display_contacts_list()
    main()
    
