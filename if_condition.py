"""
egyptian = True

if(egyptian == True):
    print(egyptian)
else:
    print(False)

if egyptian:
    print(True)

if not egyptian:
    print(False)
"""
email = "mgogah@gmail.com"
password = 12345

if email == "m.gogah@gmail.com" and password == 1234:
    print("Welcome")
elif email == "m.gogah@gmail.com" and password != 1234:
    print("invalid password")
elif email != "m.gogah@gmail.com" and password == 1234:
    print("invalid email")
else:
    print("invalid email and password")