def main():
    sum = 0
    oper = 0
    print("Simpel Paython Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    oper = int(input("Enter 1(+)2(-)3(*)4(/): "))
    if oper ==1:
        answer = num1+num2
        print("answer",answer)

    elif oper == 2:
        answer = num1-num2
        print("answer",answer)

    elif oper == 3:
        answer = num1*num2
        print("answer",answer)

    elif oper == 4:
        answer = num1/num2
        print("answer",answer)

main()




