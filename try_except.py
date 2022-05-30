try:
    n = float(input("Enter Number: "))
    print(n)
    x = 10/0
except ZeroDivisionError as error1:
    print(error1)
except ValueError as error2:
    print(error2)