# tavaghti ke exit vared nashodeh ast esm begirad v be tartib alefba yeki yeki chop namayd.

name_list = []    # yk list khali az esm entekhb mikoneem.

while True:
    name = input("enter Name")

    if name.lower() == "exit":      #az barname kharej sho
        break

    name_list.append(name)

name_list.sort()
print(name_list)






