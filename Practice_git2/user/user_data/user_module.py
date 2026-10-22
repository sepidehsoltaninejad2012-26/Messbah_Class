from persian_tools.legal_id import validate
#legal_id.validate("09122574933")
#legal_id.validate("+989122574933")
#from persian_tools import national_id as nid_validator
#phone_number.validate("+989122574933")
#phone_number.operator_data("09122574933")
#1
def show_menu():
    print("1) national id")
    print("2) phone number")
    print("3) card number")
    print("4) plate")
    print("5) bill")
    print("0) exit")
    return int(input("Enter Option:"))

#2 tabe daryaft info
def get_user_data(user_list):
    national_id = str(input("Enter National ID: "))
    phone_number = str(input("Enter Phone Number: "))
    card_number = str(input("Enter Card Number: "))
    plate =str(input("Enter Plate: "))
    bill = str(input("Enter Bill: "))
    user_info = {"national_id": national_id, "phone_number": phone_number,"plate": plate,"bill_id": bill}
    user_list.append(user_info)
    return national_id, phone_number, card_number, plate, bill

#3 baray validation baray har dade be sorat jodaganeh eghdam minamaeiim.
def national_validate(national_id):
    if validate(national_id):
        print (national_id)
        return True
    else:
        print ("Invalid National ID !!!")
        return False

#4
def phone_number_validate(phone_number):
    if validate(phone_number):
        print (phone_number)
        return True
    else:
        print ("Invalid Phone Number !!!")
        return False

#5
def card_number_validate(card_number):
    if validate(Card_Number):
        print (Card_Number)
        return True
    else:
        print ("Invalid Card Number !!!")
        return False
#6
def plate_validator(plate):
    if validate(plate):
        print (plate)
        return True
    else:
        print ("Invalid Plate !!!")
        return False
#7
def bill_validator(bill):
    if validate(bill):
        print (bill)
        return True
    else:
        print ("Invalid Bill !!!")
        return False

#8 dar halat shekastan khat tolani moghabel print, pycharm error mideh :( :( :(
def show_user_list(user_list):
    for user in user_list():
        print()
        user_data = [
        f"user['National_ID']:10"
        f"user['Mobile_number']:11"
        f"user['Account_number']:16"
        f"user['Plate']:9"
        f"user['Bill_ID']:13 "
        ]
