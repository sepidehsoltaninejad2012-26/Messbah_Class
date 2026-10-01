from user import *

file_name = "user/user_data"
user_list = read_from_file(user_data)

while True:
    option = show_menu()
    print("--------------------------")

    match option:
        case 1:
            if national_id_validate(user["national_id"]):
                user_list.append("national_id")
                write_to_file(user_data, user_list)
                print("Added")
            else:
                print("Invalid national id!!!")

        case 2:
            if phone_number_validate(user["phone_number"]):
                user_list.append("phone_number")
                write_to_file(user_data, user_list)
                print("Added")
            else:
                print("Invalid phone number!!!")

        case 3:
            user = get_user_data()
            if card_number_validate(user["card_number"]):
                user_list.append("card_number")
                write_to_file(user_data, user_list)
                print("Added")
            else:
                print("Invalid card number!!!")

        case 4:
            if plate_validate(user["plate"]):
                user_list.append("plate")
                write_to_file(user_data, user_list)
                print("Added")
            else:
                print("Invalid plate!!!")

        case 5:
            if bill_validate(user["bill"]):
                user_list.append("bill")
                write_to_file(user_data, user_list)
                print("Added")
            else:
                print("Invalid bill!!!")

        case 0:
            break

        case _:
            print("invalid option")

    print("--------------------------")