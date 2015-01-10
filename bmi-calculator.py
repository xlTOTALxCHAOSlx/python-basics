print("Hello this is a BMI calculator")
print("You need to provide some details and we will determine if you are fat")
print(" ")
height = float(input("How tall are you (metres):"))
weight = float(input("How much do you weigh (kilograms):"))

def calcbmi(ht1, wt1):
    nb3 = wt1 / ht1
    print("Wt1: ",wt1)
    print("Ht1: ",ht1)
    print("Nb3: ",nb3)
    print("Executed")
    return round(nb3 / ht1, 2)

print("You have a BMI of", calcbmi(height, weight))
