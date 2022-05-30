def calc_hours(age):
    x = age*365*24
    str1 = "Your age in hours is: " + str(x)
    return str1

print(calc_hours(int(input("Enter Your age: "))))