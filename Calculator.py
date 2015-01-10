print("Hello this is a calculator")
print("You need to provide some details details to figure out your sum")
print(" ")
#Addition
def add(nb1, nb2):
    return nb1 + nb2
#Subtract
def sub(nb1, nb2):
    return nb1 - nb2
#Multply
def mul(nb1, nb2):
    return nb1 * nb2
#Divide
def div(nb1, nb2):
    return nb1 / nb2

def main():
    mySym = input(": ")
    if(mySym != '+' and mySym != '-' and mySym != '*'and mySym != '/'):
        #Invalid Operation
            print("Invalid Operation")
    else:
        myNum1 = int(input("First Number: "))
        myNum2 = int(input("Second Number: "))
        if(mySym == '+'):
            print(add(myNum1, myNum2))
            return False
        elif(mySym == '-'):
             print(sub(myNum1, myNum2))
             return False
        elif(mySym == '*'):
             print(mul(myNum1, myNum2))
             return False
        elif(mySym == '/'):
             print(div(myNum1, myNum2))
             return False
while True : 
    myPoo = main()
    if myPoo == False:
        break
