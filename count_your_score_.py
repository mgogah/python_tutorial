def names(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


ahmed = int(input("Enter Ahmed's score: "))

if ahmed >= 90:
    print("Exellent")
elif ahmed >= 80:
    print("Very Good")
elif ahmed >= 70:
    print("Good")
elif ahmed >= 50:
    print("Successfull")
else:
    print("Not Successfull")