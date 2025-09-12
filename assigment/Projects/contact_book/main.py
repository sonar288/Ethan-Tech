contacts = [
    {"name": "Rahul Sonar", "contact": 9022358452}, {"name": "Prathmesh Patil", "contact": 1234567890}, {"name": "Sneha Kulkarni", "contact": 9876543210},
    {"name": "Amit Joshi", "contact": 8765432109}, {"name": "Pooja Deshmukh", "contact": 7654321098}, {"name": "Karan Sharma", "contact": 6543210987},
    {"name": "Anjali Verma", "contact": 9123456780}, {"name": "Rohan Shinde", "contact": 8899776655}, {"name": "Meena Jadhav", "contact": 9988776655},
    {"name": "Suresh Pawar", "contact": 9090909090}, {"name": "Priya Chavan", "contact": 9191919191}, {"name": "Manoj Patankar", "contact": 9292929292},
    {"name": "Neha Bhosale", "contact": 9393939393}, {"name": "Vikas Kadam", "contact": 9494949494}, {"name": "Alok Rane", "contact": 9595959595},
    {"name": "Shweta Naik", "contact": 9696969696}, {"name": "Deepak More", "contact": 9797979797}, {"name": "Ritika Gokhale", "contact": 9898989898},
    {"name": "Sameer Gaikwad", "contact": 9999999999}, {"name": "Komal Salunkhe", "contact": 9098765432},{"name":"Rahul Wagh" ,"contact": 9098765433}
]
#view all contact
def view_contact(contact):
    contact = contact
    for i in contact:
        print(f"\nname:{i["name"]}\nPhone number:{i["contact"]}")

# Search spefice contact
# search by name
def search_by_name():
    sn = input("Enter the name: ").lower()
    return [i for i in contacts if sn == i["name"][:len(sn)].lower() ]  

# search by number
def search_by_number():

    num = input("enter the number: ")
    if  num.isdigit():
        return [i for i in contacts if num == str(i["contact"])[:len(num)] ]
    else:
        print("print only numbers") # if given wrong input it gives: print only numbers Contact is not found both the errors




def view_selected_contact():
    search = input("""
    1. Search By name
    2. Search by number : """)
    if(int(search) == 1):
        names = search_by_name() #names is the list of contact which matches the search
        if names:  
            view_contact(names)
        else:
            print("Contact is not found")

    elif(int(search) == 2):
        num = search_by_number()  #num is the list of contact which matches the search
        if num:
            view_contact(num)
        else:
            print("Contact is not found")
    else:
        print("give valid input")



class Main():
    # view all contacts
    # view selected contact
    # add new contacts
    # delete contacts
    # modify the contact

    print("Welcome to contact application")
    print("""
    1. View all contacts
    2. Search the contact
    3. Add new contact
    4. Edite the contact
    5. Delete the contact
    6. exit
    """) 


    user = input("Select the operation you want to perform(select from 1-6): ")

    # value error should br resolve
    if(int(user) == 1):
        view_contact(contacts)
    elif(int(user) == 2):
        view_selected_contact()
    elif(int(user) == 3):
        print("Add new contact")
    elif(int(user) == 4):
        print("Edit the contact")
    elif(int(user) == 5):
        print("Delete the contact")
    elif(int(user) == 6):
        print("Exiting the contact  appliction")  
    else:
        print("Give the valid numbers")



my_contact = Main()

print(my_contact)
