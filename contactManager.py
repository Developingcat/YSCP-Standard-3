# Global dictionary to store contacts

contacts_emails = {}
contacts_phone = {}
contacts_list = [contacts_emails, contacts_phone]

def main():

    choice = int(input("Please select the option you'd like (1-6): "))

    while True: # This only took 40 minutes to properly fix <- This statement was a lie

        if choice == 1: # Outside adding things to the dictionary, it actually works
            
            profile = input("Please add the users contact name (or type done to be finished): ").strip()
            # Do the append tommorrow, do not focus on it now. 
            if profile == 'done'.lower():
                break
            numbers = input("Please add the users contact number (Please include dashes.): ").strip()
            
            email = input("Please add the users contact email: ").strip()
 
            print("Contact added successfully!")

            profile = [contacts_list,contacts_emails, contacts_phone,].append

        if choice == 2: # <- Makes a infinite loop, try to fix the append 
            print("---All Contacts---") 
            print(f"Contact Name:" ,[contacts_list] )
            print(f"Contacts Email:" ,[contacts_emails])
            print(f"Contacts Number: " ,[contacts_phone])
            print("-------------------")

        if choice == 3: # Still needs to be worked on 
            print("---Search For a Contact---")
            input("Please type the name you are searching for: ")
            # if profile not in contacts_list:
            #     print("This user is not in your contacts") 
            

        if choice == 4: 
            print("----Remove A Contact----")
            print([contacts_list])
            input("Would you like to remove a contact? Type Y for yes and N for no: ") 
        if choice == 5:
            print("----Update A Contact----")
        
        if choice == 6:  
            print("Thank you for using this program, have a swell day!") 
            break 


def display_contacts_list():
    print(" ----------------- ")
    print("| Contact Manager |")
    print(" ----------------- ")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Update a contact")
    print("6. Quit") 
    print("------------------")

# Main function to run the menu-driven system


if __name__ == "__main__":
    display_contacts_list()
    main()
    
