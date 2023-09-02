num1 = input("Enter the first number : ")
num2 = input("Eneter the second number : ")
operator = input("enter arithmetic operator : ")
if operator == '+' :
    sum = float(num1) +float(num2)
    print(sum)
elif operator =='-' :
    subs = float(num1) - float(num2)
    print(subs)
elif operator == '*' :
    multi = float(num1) * float(num2)
    print(multi)
elif operator == '/' :
    dev = float(num1) / float(num2)
    print(dev)
elif operator == '%' :
    rem = int(num1) % int(num2)
    print(rem)
else :
    print("invalid operator")
