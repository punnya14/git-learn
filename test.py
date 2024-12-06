weight=int(input("enter the weight="))
height=int(input("enter the height="))
def bmi(weight,height):
    bmi = weight/(height**2)
    print(bmi)
bmi(weight,height)
