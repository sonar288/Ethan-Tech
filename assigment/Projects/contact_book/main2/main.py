import os, json

# Get absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_FILE = os.path.join(BASE_DIR, "contacts.json")

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # start with empty list if file missing
    except json.JSONDecodeError:
        return []   # start with empty if file is corrupted

def save_contacts():
    global contacts
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
    print(f"✓ Contacts saved to {CONTACTS_FILE}")



# ---------- Contacts ----------
contacts = load_contacts()

# View all contacts
def view_contact(contact):
    if not contact:
        print("No contacts available.")
        return
    print("=" * 30)
    for i, c in enumerate(contact, 1):
        print(f"{i}. {c['name']} - {c['contact']}")
    print("=" * 30)

# Search specific contact
def search_by_name(search):
    sn = search.lower()
    return [i for i in contacts if sn == i["name"][:len(sn)].lower()]

def search_by_number(search):
    if len(search) <= 10:
        return [i for i in contacts if search == str(i["contact"])[:len(search)]]
    else:
        print("Invalid number")
        return None

def view_selected_contact():
    search = input("""
    Search contact
    Enter name or number: """).strip()
    
    try:
        if search.isdigit():
            num = search_by_number(search)
            if num:
                view_contact(num)
            elif num is None:
                pass
            else:
                print("Contact not found")
        else:
            names = search_by_name(search)
            if names:
                view_contact(names)
            else:
                print("Contact not found")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


# Add new contact
def add_new_contact():
    print("To create new contact provide name and contact number:\n")
    try:
        user_name = input("Name: ").strip()
        if not user_name:
            print("Error: Name cannot be empty")
            return

        for contact in contacts:
            if contact["name"].lower() == user_name.lower():
                print(f"Error: Contact '{user_name}' already exists!")
                return
            
        user_no = input("Phone No.: ").strip()
        if not user_no:
            print("Error: Phone number cannot be empty")
            return

        cleaned_number = user_no.replace("-", "").replace(" ", "").replace("(", "").replace(")", "").replace("+", "")
        if not cleaned_number.isdigit():
            print("Error: Please enter only numbers")
            return
        
        if len(cleaned_number) < 10:
            print("Error: Phone number should be at least 10 digits")
            return
        
        for contact in contacts:
            if contact["contact"] == int(cleaned_number):
                print(f"Error: Contact '{cleaned_number}' already exists!")
                return
    
        contacts.append({"name": user_name, "contact": int(cleaned_number)})
        save_contacts()

        print(f"\nName: {user_name}\nPhone number: {user_no}\n✓ Added to contacts")

    except Exception as e:
        print(f"Error: {e}")


# Update contact
def update_contact():
    try:
        if not contacts:
            print("No contacts available!")
            return False
        
        print("\n=== CURRENT CONTACTS ===")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['contact']}")
        
        user_name1 = input("\nEnter name of contact to update: ").strip()
        if not user_name1:
            print("Error: Name cannot be empty")
            return False
        
        matching_contacts = [(i, contact) for i, contact in enumerate(contacts) if user_name1.lower() in contact["name"].lower()]
        
        if not matching_contacts:
            print(f"Error: No contacts found matching '{user_name1}'")
            return False
        
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
        
        print(f"\n=== CURRENT CONTACT ===")
        print(f"Name: {target_contact['name']}")
        print(f"Phone: {target_contact['contact']}")
        
        print(f"\n=== UPDATE CONTACT ===")
        new_name = input(f"New Name (press Enter to keep '{target_contact['name']}'): ").strip()
        if not new_name:
            new_name = target_contact["name"]

        new_phone = input(f"New Phone (press Enter to keep '{target_contact['contact']}'): ").strip()
        if not new_phone:
            new_phone = str(target_contact["contact"])
        
        cleaned_number = new_phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "").replace("+", "")
        if not cleaned_number.isdigit():
            print("Error: Phone number should contain only digits")
            return False
        
        if len(cleaned_number) < 10 or len(cleaned_number) > 15:
            print("Error: Phone number should be between 10-15 digits")
            return False
        
        for i, contact in enumerate(contacts):
            if i != contact_index:
                if contact["name"].lower() == new_name.lower():
                    print(f"Error: Contact name '{new_name}' already exists!")
                    return False
                if str(contact["contact"]) == cleaned_number:
                    print(f"Error: Phone number '{cleaned_number}' already exists!")
                    return False
        
        print(f"\n=== CONFIRM UPDATE ===")
        print(f"Name: {target_contact['name']} → {new_name}")
        print(f"Phone: {target_contact['contact']} → {cleaned_number}")
        
        confirm = input("Confirm update? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Update cancelled.")
            return False
        
        contacts[contact_index]["name"] = new_name
        contacts[contact_index]["contact"] = int(cleaned_number)
        
        save_contacts()
        print(f"\n✓ Contact updated successfully!")
        return True
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


# Delete contact
def delete_the_contact():
    view_contact(contacts)
    try:
        user_name = input("Enter name to delete: ").strip()
        if not user_name:
            print("Error: Name cannot be empty")
            return
        for contact in contacts:
            if user_name.lower() == contact["name"].lower():
                contacts.remove(contact)        
                save_contacts()
                print(f"✓ Contact '{user_name}' deleted")
                break
        else:
            print("No such user found")
    except Exception as e:
        print(f"Error: {e}")


# Main menu
def main():
    print("Welcome to Contact Application")
    while True:
        print(f"""
{'=' * 40}
1. 👀 View all contacts
2. 🔍 Search contacts  
3. ➕ Add new contact
4. ✏️  Edit contact
5. 🗑️  Delete contact
6. 🚪 Exit
{'=' * 40}""")

        user = input("Select the operation you want to perform (1-6): ")

        try: 
            if int(user) == 1:
                view_contact(contacts)
            elif int(user) == 2:
                view_selected_contact()
            elif int(user) == 3:
                add_new_contact()
            elif int(user) == 4:
                update_contact()
            elif int(user) == 5:
                delete_the_contact()
            elif int(user) == 6:
                print("Exiting the contact application")  
                break
            else:
                print("Select the correct option (1-6)")
        except ValueError:
            print("\nSelect the correct option (1-6)")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
