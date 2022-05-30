n1 = float(input("Enter first No. :"))
op = input("Enter operation")
n2 = float(input("Enter second No. :"))

if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("Operation Error")