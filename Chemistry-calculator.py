# Chemical Calculator  Made by Maheir
def normality():
    print("To prepare normality solution")
    value_1=int(input("Input Molecular Weight:"))
    value_2=int(input("How many Normal you want(numerical value only):"))
    value_3=int(input("Input Final Volume:"))
    Value_4=input("Does it have Charge Difference or More than 2 Hydrogen? Y/N:").lower()
    
    if Value_4 == "y":
        value_x=int(input("Please Give the Charge or Hydrogen Value;eg H2SO4 so value 2:"))
        value_x= ((value_1/value_x)*value_2)
        print("To prepare",value_2,"N","In",(value_3/1000),"Litre","Dissolve:",((value_x*value_3)/1000),"gm")
    elif Value_4 == "n":
        print("To prepare",value_2,"N","In",(value_3/1000),"Litre","Dissolve:",((value_1*value_2*value_3)/1000),"gm")
    else:
        print("Try again")
        return normality()   
    input("Press Enter to exit")
def solution():
    print("To prepare volume solution")
    value_1=int(input("Input Grams of solute else press enter zero:"))
    value_2=int(input("Input volume of solute else press enter zero:"))
    value_3=int(input("Input Final volume required (Stock):"))
    print("Dissolve :",(value_1*value_3*10)//1000,"gms","In",value_3,"mL and its Percent Concentration is:",(value_1*value_3//value_3),"%")
    print("Add volume of",(value_2*value_3*10)//1000,"mL","In",value_3,"mL and its Percent Concentration is:",(value_2*value_3//value_3),"%")
    input("Press Enter to exit")

user=input("Do you want 1) Normality or 2)Solution Calculator? type 1 or 2:")

if user == "1":
    print(normality())
elif user == "2":
    print(solution())