num = int(input("Enter a number: "))   
if num > 0 :     # agar adad mosbat bashad az manfi an adad ta mosbate an ra chop kon
    for i in range (-num, num+1, 1):
        print(i)
elif num < 0 :   # agar adad manfi ast, az mosbat ta manfi an adad ra chap kon. chon yeki az 2 halat dosrost ast az elif estefadeh kardeem.
    for i in range (-num, num-1, -1):
        print(i)
else:   # 
    print("Invalid input")