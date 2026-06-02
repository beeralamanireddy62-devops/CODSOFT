"""Contact Book Application - Professional Version"""

contacts = {}


def display_menu():
    """Display main menu."""
    print("\n" + "="*50)
    print("          [*] CONTACT BOOK MANAGER")
    print("="*50)
    print("1. [+] Add Contact")
    print("2. [V] View All Contacts")
    print("3. [?] Search Contact")
    print("4. [E] Update Contact")
    print("5. [X] Delete Contact")
    print("6. [Q] Exit")
    print("="*50)


def add_contact():
    """Add a new contact with details."""
    print("\n--- Add New Contact ---")
    
    name = input("Enter contact name: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty!")
        return
    
    if name in contacts:
        print(f"[ERROR] Contact '{name}' already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("[ERROR] Phone number cannot be empty!")
        return
    
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"[OK] Contact '{name}' added successfully!")


def view_all_contacts():
    """Display all contacts in a formatted way."""
    if not contacts:
        print("\n[ERROR] No contacts in the book yet!")
        return
    
    print("\n" + "="*80)
    print(f"{'Name':<20} {'Phone':<20} {'Email':<25} {'Address':<15}")
    print("="*80)
    
    for name, details in contacts.items():
        print(f"{name:<20} {details['phone']:<20} {details['email']:<25} {details['address']:<15}")
    
    print("="*80)


def search_contact():
    """Search contact by name or phone number."""
    print("\n--- Search Contact ---")
    search_choice = input("Search by (1)Name or (2)Phone number? Enter choice: ").strip()
    
    if search_choice == "1":
        name = input("Enter contact name to search: ").strip()
        if name in contacts:
            print(f"\n[OK] Contact Found!")
            print(f"Name:    {name}")
            print(f"Phone:   {contacts[name]['phone']}")
            print(f"Email:   {contacts[name]['email']}")
            print(f"Address: {contacts[name]['address']}")
        else:
            print(f"[ERROR] Contact '{name}' not found!")
    
    elif search_choice == "2":
        phone = input("Enter phone number to search: ").strip()
        found = False
        for name, details in contacts.items():
            if details['phone'] == phone:
                print(f"\n[OK] Contact Found!")
                print(f"Name:    {name}")
                print(f"Phone:   {details['phone']}")
                print(f"Email:   {details['email']}")
                print(f"Address: {details['address']}")
                found = True
                break
        if not found:
            print(f"[ERROR] No contact found with phone number '{phone}'!")
    else:
        print("[ERROR] Invalid choice!")


def update_contact():
    """Update an existing contact."""
    print("\n--- Update Contact ---")
    
    name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print(f"[ERROR] Contact '{name}' not found!")
        return
    
    print(f"\nCurrent details for '{name}':")
    print(f"1. Phone:   {contacts[name]['phone']}")
    print(f"2. Email:   {contacts[name]['email']}")
    print(f"3. Address: {contacts[name]['address']}")
    
    choice = input("\nWhat would you like to update? (1/2/3): ").strip()
    
    if choice == "1":
        new_phone = input("Enter new phone number: ").strip()
        if new_phone:
            contacts[name]['phone'] = new_phone
            print(f"[OK] Phone number updated successfully!")
        else:
            print("[ERROR] Phone number cannot be empty!")
    
    elif choice == "2":
        new_email = input("Enter new email: ").strip()
        if new_email:
            contacts[name]['email'] = new_email
            print(f"[OK] Email updated successfully!")
        else:
            print("[ERROR] Email cannot be empty!")
    
    elif choice == "3":
        new_address = input("Enter new address: ").strip()
        if new_address:
            contacts[name]['address'] = new_address
            print(f"[OK] Address updated successfully!")
        else:
            print("[ERROR] Address cannot be empty!")
    
    else:
        print("[ERROR] Invalid choice!")


def delete_contact():
    """Delete a contact."""
    print("\n--- Delete Contact ---")
    
    name = input("Enter contact name to delete: ").strip()
    if name not in contacts:
        print(f"[ERROR] Contact '{name}' not found!")
        return
    
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower().strip()
    if confirm in ("yes", "y"):
        del contacts[name]
        print(f"[OK] Contact '{name}' deleted successfully!")
    else:
        print("[ERROR] Deletion cancelled!")


def main():
    """Main application loop."""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                add_contact()
            elif choice == "2":
                view_all_contacts()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                update_contact()
            elif choice == "5":
                delete_contact()
            elif choice == "6":
                print("\n[BYE] Thank you for using Contact Book. Goodbye!\n")
                break
            else:
                print("[ERROR] Invalid choice! Please enter a number between 1 and 6.")
        
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")


if __name__ == "__main__":
    main()

