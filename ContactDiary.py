class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\nEnter contact details:")
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nContact list is empty.")
        else:
            print("\nAll Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        if not found_contacts:
            print(f"\nNo contacts found matching '{search_term}'.")
        else:
            print(f"\nSearch results for '{search_term}':")
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        return found_contacts

    def update_contact(self):
        print("\nEnter details to update a contact:")
        current_name = input("Current Name: ")
        current_phone_number = input("Current Phone Number: ")

        for contact in self.contacts:
            if contact.name == current_name and contact.phone_number == current_phone_number:
                new_name = input("New Name (leave blank to keep current): ")
                new_phone_number = input("New Phone Number (leave blank to keep current): ")
                new_email = input("New Email: ")
                new_address = input("New Address: ")

                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address

                print(f"\nContact '{current_name}' with phone number '{current_phone_number}' updated successfully.")
                return

        print(f"\nContact '{current_name}' with phone number '{current_phone_number}' not found.")

    def delete_contact(self):
        print("\nEnter details to delete a contact:")
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        for contact in self.contacts:
            if contact.name == name and contact.phone_number == phone_number:
                self.contacts.remove(contact)
                print(f"\nContact '{name}' with phone number '{phone_number}' deleted successfully.")
                return
        print(f"\nContact '{name}' with phone number '{phone_number}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("\nEnter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("\nExiting Contact Management System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
