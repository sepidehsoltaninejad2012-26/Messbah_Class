# yek tabeh baray shomaresh horof seda dar (count_vowel)
def count_vowels(name   ):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

names_list = []
print (names_list)

# ta zamani ke quit nagerefteh ast, esm begid va dakhel list ezafeh kon.
while True:
    user_name = str(input("Enter Name:"))
    if user_name.lower() == "quit":
        break
    if user_name:
        names_list.append(user_name)
# list ra bar asase tedad horof sedadar sort kon
sorted_names_list = sorted(names_list, key=count_vowels, reverse=True)
for user_name in sorted_names_list:
    v_count = count_vowels(user_name)
print(f"{user_name} : v_count)")








