from contact_modual import *

while True:
    option = show_menu()

match option:
    case 1:
        contact = get_contact_info()
        if contact_list["phone"]:
            print("Error, contact already exists!!!")
        else:
            contact_list.append(contact)
            print("contact added to contact list")
    case 2:
        print_contact_list(contact_list)
    case 3:
        phone = int(input("Enter phone number by search : ")
        result = find_contact_by_phone(contact_list, phone)
        if result:
            print("Info : Contact Found :")
        else:
            print("Error : Contact Not Found !!!")

    case 0:
        break

    case _:
        print("Error : Invalid Option !!!")






















while True:
    option = show_menu()




