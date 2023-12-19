class Contact():
    def __init__(self, name, email, telephone):
        self.name       = name
        self.email      = email
        self.telephone  = telephone
        
    def description(self):
        return f"Name: {self.name}, email: {self.email}, phone: {self.telephone}"

class Contact_List():
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        contact1 = Contact(name, email, phone)
        self.contacts.append(contact1.description())
    
    def show_list(self):
        for i in self.contacts:
            print(i)

list1 = Contact_List()
list1.add_contact("Janusz", "realsteel@phonk.pl", "+48 537 110 041")
list1.add_contact("Ewa", "eden@wonsz.pl", "+48 666 110 241")
list1.show_list()