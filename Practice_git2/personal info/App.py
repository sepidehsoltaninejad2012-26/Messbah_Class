from file_manager import *
from persian_tools import national_id

from personal_module im

file_name = "Personal.data"
personal_list = read_from_file(file_name)


def national_id_validator(param):
    pass


while True:
    option = show_menu()
    print("*", 50)

    match option:
        case 1:
            personal = get_national_id()
            if national_id_validator(personal["National_ID"]):
                personal_list.append(personal)
            print("Added personal id: ", personal)

        case 2:
            personal = get_mobile_number()
            if mobile_validator() == personal():
                personal_list.append(personal)
            print("Added personal id: ", personal)
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 0:
            break
        case _:
            print("Invalid option")