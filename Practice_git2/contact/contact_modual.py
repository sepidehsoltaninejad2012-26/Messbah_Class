contact_list = []
def show_menu():
    print("1. Add contact")
    print("2. contact_list")
    print("3. search_by_phone")
    print("4. exit")
    option = int(input("Option: "))
    return option
def get_contact_info():
    name = input("Name: ")
    family = input("Family Name: ")
    phone = int(input("Phone number: "))
    title = input("Title: ")
    return {"name": name, "family": family, "phone" : phone, "title": title}
def find_contact_by_phone(contact_list, phone):
    print("Contact List")
def print_contact_list(contact_list):
    print("Contact List")
    contact = contact_list
    for phone in contact:
        print(f'{contact["name"]:10} {contact["family"]:15} {contact["phone"]:15} {contact["title"]:10}')
def search_by_phone():
    for search_by_phone in contact_list:
        if phone["contact"] == search_by_phone:
            return phone
        else:
            contact_list.append(get_contact_info)
            print("Info : contact Added to contact list")
