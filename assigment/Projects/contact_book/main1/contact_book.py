from contact import contacts
#view all contact
def view_contact(contact):
    cn = contact
    print("=" * 30)
    for i, contact in enumerate(cn, 1):
            print(f"{i}. {contact['name']} - {contact['contact']}")
    print("=" * 30)

# Search spefice contact
# search by name
def search_by_name(search):
    sn = search.lower()
    return [i for i in contacts if sn == i["name"][:len(sn)].lower() ]  

# search by number
def search_by_number(search):
    num = search
    
    if len(num) <= 10:
            return [i for i in contacts if num == str(i["contact"])[:len(num)] ]
    else:
        print("these is not valid number")
        return None
    

def view_selected_contact():
    search = input("""
    1. Search By name
    2. Search by number: """)
    
    try:
        if(search.isdigit()):
            num = search_by_number()  #num is the list of contact which matches the search
            if num:
                view_contact(num)
            elif num == None:
                pass
            else:
                print("Contact is not found")
        else:
            names = search_by_name(search) #names is the list of contact which matches the search
            if names:  
                view_contact(names)
            else:
                print("Contact is not found")

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

    # try:
    #     if(int(search) == 1):
    #         names = search_by_name() #names is the list of contact which matches the search
    #         if names:  
    #             view_contact(names)
    #         else:
    #             print("Contact is not found")
    #     elif(int(search) == 2):
    #         
    #     else:
    #         print("give valid input")
    # except ValueError:
    #     print("\nSelect valid input")
    #     return []
    # except Exception as e:
    #     print(f"Unexpected error: {e}")
    #     return []
# Adds the new contact
def add_new_contact():

    print("to create new contact provide name and contact number:\n")
    try:
        user_name = input("Name: ").strip()
        if not user_name:
            print("Error: Name cannot be empty")
        # Check for duplicates
        for contact in contacts:
            if contact["name"].lower() == user_name.lower():
                print(f"Error: Contact '{user_name}' already exists!")
            
        user_no = input("Phone No.: ").strip()
        if not user_no:
            print("Error: Phone number cannot be empty")

        cleaned_number = user_no.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
        if not cleaned_number.isdigit():
            print("Error: Please enter only numbers")
        
        if len(cleaned_number) < 10:
            print("Error: Phone number should be at least 10 digits")
        
        
        for contact in contacts:
            if contact["contact"]== int(cleaned_number):
                print(f"Error: Contact '{cleaned_number}' already exists!")
    
        contacts.append({"name": user_name,"contact": int(cleaned_number)})
    
        with open("contact.py", "w") as f:
            f.write("contacts = " + str(contacts))
    
        print(f"\nname:{user_name}\nPhone number:{user_no}\nis added to your contact")

    except Exception as e:
        print(f"Error: {e}")

# update the contact
def update_contact():
    try:
        if not contacts:
            print("No contacts available!")
            return False
        
        # Show all contacts first
        print("\n=== CURRENT CONTACTS ===")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['contact']}")
        
        
        print("\nSelect the contact you want to update:")
        user_name1 = input("Enter name: ").strip()
        
        if not user_name1:
            print("Error: Name cannot be empty")
            return False
        
        # Search for contacts (partial match)
        matching_contacts = []
        for i, contact in enumerate(contacts):
            if user_name1.lower() in contact["name"].lower():
                matching_contacts.append((i, contact))
        
        if not matching_contacts:
            print(f"Error: No contacts found matching '{user_name1}'")
            return False
        
        # If multiple matches, let user choose
        if len(matching_contacts) > 1:
            print(f"\nFound {len(matching_contacts)} matching contacts:")
            for i, (original_index, contact) in enumerate(matching_contacts, 1):
                print(f"{i}. {contact['name']} - {contact['contact']}")
            
            try:
                choice = int(input("Select contact number: ")) - 1
                if choice < 0 or choice >= len(matching_contacts):
                    print("Invalid selection!")
                    return False
                contact_index, target_contact = matching_contacts[choice]
            except ValueError:
                print("Please enter a valid number!")
                return False
        else:
            contact_index, target_contact = matching_contacts[0]
        
        # Show current contact details
        print(f"\n=== CURRENT CONTACT ===")
        print(f"Name: {target_contact['name']}")
        print(f"Phone: {target_contact['contact']}")
        
        print(f"\n=== UPDATE CONTACT ===")
        
        # Get new name
        new_name = input(f"New Name (current: {target_contact['name']}): ").strip()
        if not new_name:
            print("Error: Name cannot be empty")
            return False
        
        # Get new phone number
        new_phone = input(f"New Phone (current: {target_contact['contact']}): ").strip()
        if not new_phone:
            print("Error: Phone number cannot be empty")
            return False
        
        # Clean and validate phone number
        cleaned_number = new_phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "").replace("+", "")
        
        if not cleaned_number.isdigit():
            print("Error: Phone number should contain only digits")
            return False
        
        if len(cleaned_number) < 10 or len(cleaned_number) > 15:
            print("Error: Phone number should be between 10-15 digits")
            return False
        
        # Check for duplicates (excluding current contact)
        for i, contact in enumerate(contacts):
            if i != contact_index:
                if contact["name"].lower() == new_name.lower():
                    print(f"Error: Contact name '{new_name}' already exists!")
                    return False
                if str(contact["contact"]) == cleaned_number:
                    print(f"Error: Phone number '{cleaned_number}' already exists!")
                    return False
        
        # Confirm update
        print(f"\n=== CONFIRM UPDATE ===")
        print(f"Name: {target_contact['name']} → {new_name}")
        print(f"Phone: {target_contact['contact']} → {cleaned_number}")
        
        confirm = input("Confirm update? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Update cancelled.")
            return False
        
        # Update the contact
        old_name = target_contact["name"]
        old_phone = target_contact["contact"]
        
        contacts[contact_index]["name"] = new_name
        contacts[contact_index]["contact"] = int(cleaned_number)
        
        print(f"\n✓ Contact updated successfully!")
        print(f"Updated contact: {contacts[contact_index]}")

        with open("contact.py", "w") as f:
            f.write("contacts = " + str(contacts))
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# delete the new contact
def delete_the_contact():
    view_contact(contacts)
    try:
        user_name = input("Name: ").strip()
        if not user_name:
            print("Error: Name cannot be empty")
        # Check for duplicates
        for contact in contacts:
            if user_name.lower() == contact["name"].lower():
                contacts.remove(contact)        
                with open("contact.py", "w") as f:
                    f.write("contacts = " + str(contacts))
                break
        else:
            print("no such user found")
    except Exception as e:
        print(f"Error: {e}")




def main():
    # view all contacts(done)
    # view selected contact(done)
    # add new contacts(done)
    # delete contacts(done)
    # modify the contact(done)
    

    print("Welcome to contact application")
    print("""
    {'=' * 40}
1. 👀 View all contacts
2. 🔍 Search contacts  
3. ➕ Add new contact
4. ✏️  Edit contact
5. 🗑️  Delete contact
6. 🚪 Exit
{'=' * 40}""")


    user = input("Select the operation you want to perform(select from 1-6): ")

    # value error should br resolve
    try:
        if(int(user) == 1):
            view_contact(contacts)
        elif(int(user) == 2):
            view_selected_contact()
        elif(int(user) == 3):
            add_new_contact()
        elif(int(user) == 4):
            update_contact()
        elif(int(user) == 5):
            delete_the_contact()
        elif(int(user) == 6):
            print("Exiting the contact  appliction")  
        else:
            print("Select the correct option(between 1-6)")
    except ValueError:
        print("\nSelect the correct option(between 1-6)")
    except Exception as e:
        print(f"Unexpected error: {e}")

my_contact = main()

my_contact