from persian_tools import phone_number

def age_validator(age):
    if type(age) ==  int and 0<age<150:
        return age
    else:
        raise ValueError("سن غیر مجاز است")


def phone_validator(phone):
    if not phone_number.validate(phone):
        raise ValueError("شماره موبایل معتبر نیست")
    return phone_number.normalize(phone)

print(phone_validator("+989171231234"))