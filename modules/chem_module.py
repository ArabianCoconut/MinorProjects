# Chemical Calculator  Made by ArabianCoconut
from time import sleep
def normality():
    print("To prepare normality solution")
    value_1=float(input("Input Molecular Weight:"))
    value_2=float(input("How many Normal you want(numerical value only):"))
    value_3=float(input("Input Final Volume:"))
    Value_4=input("Does it have Charge Difference or More than 2 Hydrogen? Y/N:").lower()
    
    if Value_4 == "y":
        value_x=int(input("Please Give the Charge or Hydrogen Value;eg H2SO4 so value 2:"))
        value_x= ((value_1/value_x)*value_2)
        print("To prepare",value_2,"N","In",(value_3/1000),"Litre","or",value_3,"mL","Dissolve:",((value_x*value_3)/1000),"gm")
    elif Value_4 == "n":
        print("To prepare",value_2,"N","In",(value_3/1000),"Litre","or",value_3,"mL","Dissolve:",((value_1*value_2*value_3)/1000),"gm")
    else:
        print("Try again")
    sleep(1)
    print("going back to main menu")
    return start()   
def solution():
    print("To prepare volume solution")
    value_1=float(input("Input Grams of solute else press enter zero:"))
    value_2=float(input("Input volume of solute else press enter zero:"))
    value_3=float(input("Input Final volume required (Stock):"))
    print("Dissolve :",(value_1*value_3*10)/1000,"gms","In",value_3,"mL and its Percent Concentration is:",(value_1*value_3/value_3),"%")
    print("Add volume of",(value_2*value_3*10)/1000,"mL","In",value_3,"mL and its Percent Concentration is:",(value_2*value_3/value_3),"%")
    return start()
def converter():
    print("Convert Grams to miligrams vice versa.")
    data=["Select the Option's:-","1) Gram to miligram","2) Miligrams to Grams","3) To go back\n"]
    for i in data:
        print(i)
    a=input("What is your Selection?: ")
    if a == "1":
        gm=input("Please Enter gram value digit only: ")
        value= (float(gm)*1000)
        print("Miligram Value is:",value,"Mg\n")
        converter()
    elif a =="2":
        mg=input("Please Enter miligrams value digit only: ")
        value=(float(mg)/1000)
        print("Gram value is:",value,"gm's\n")
        converter()
    elif a == "3":
        start()
    else:
        print("Try Again! \n")
        return converter()

def start():
    data=["Version 1.0","Choose options:-", "1) Normality calculator","2) Solution Calculator","3) Gram and miligram converter","4) Select exit or type exit\n"]
    for i in data:
        print(i)
    user=input("Select the number to proceed: ")
    if user == "1":
        normality()
    elif user == "2":
        solution()
    elif user == "3":
        converter()
    elif user == "exit".lower() or user=="4":
        print("Exiting...")
        sleep(1)
        exit()
    else:
        print("Their is an input error.Try again!\n")
        return start()

print(start())
