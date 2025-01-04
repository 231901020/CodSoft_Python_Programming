class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")
        print()

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Updating contact: {contact.name}")
                contact.phone = input("Enter new phone number: ") or contact.phone
                contact.email = input("Enter new email: ") or contact.email
                contact.address = input("Enter new address: ") or contact.address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def menu(self):
        while True:
            print("\n--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
