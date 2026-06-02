def display_menu():
    print("\n" + "="*50)
    print("        CONTACT BOOK MENU")
    print("="*50)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("="*50)

def add_contact(contacts):
    print("\n--- ADD CONTACT ---")
    try:
        name = input("Enter contact name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        # Check if contact already exists
        if any(c['name'].lower() == name.lower() for c in contacts):
            print(f"⚠️  Contact '{name}' already exists!")
            return
        
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("❌ Phone number cannot be empty!")
            return
        
        email = input("Enter email address: ").strip()
        address = input("Enter address (optional): ").strip()
        
        # Create contact dictionary
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        
        contacts.append(contact)
        print(f"✅ Contact '{name}' added successfully!")
    
    except Exception as e:
        print(f"❌ Error adding contact: {e}")

def view_all_contacts(contacts):
    print("\n--- ALL CONTACTS ---")
    if not contacts:
        print("📭 No contacts found!")
        return
    
    for idx, contact in enumerate(contacts, 1):
        print(f"\n{idx}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        if contact['address']:
            print(f"   Address: {contact['address']}")
    
    print(f"\n{'='*50}")
    print(f"Total contacts: {len(contacts)}")

def search_contact(contacts):
    print("\n--- SEARCH CONTACT ---")
    search_name = input("Enter name to search: ").strip().lower()
    
    found_contacts = [c for c in contacts if search_name in c['name'].lower()]
    
    if not found_contacts:
        print(f"❌ No contacts found with '{search_name}'")
        return
    
    print(f"\n✅ Found {len(found_contacts)} contact(s):\n")
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        if contact['address']:
            print(f"Address: {contact['address']}")
        print("-" * 30)

def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")
    name_to_delete = input("Enter name of contact to delete: ").strip()
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name_to_delete.lower():
            contacts.pop(i)
            print(f"✅ Contact '{name_to_delete}' deleted successfully!")
            return
    
    print(f"❌ Contact '{name_to_delete}' not found!")

def contact_book():
    print("\n" + "="*50)
    print("    WELCOME TO CONTACT BOOK")
    print("="*50)
    
    contacts = []  # List to store contacts
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_all_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("\n👋 Thank you for using Contact Book! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    contact_book()
