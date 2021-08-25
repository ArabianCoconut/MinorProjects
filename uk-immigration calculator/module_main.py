points=[0,10,20]
data=["Offer of job by approved sponsor","Job at appropriate skill level","Speaks English at required level"]
cal_data=list()
def pass_data_Madatory():
    global cal_data
    a=points[2]
    cal_data.append(a)
    if sum(cal_data) == 60:
        a = sum(cal_data) - 50
        cal_data.pop(2)
        cal_data.append(a)
    print("\nThis is your Total Points:",str(sum(cal_data)))
def fail_data():
    global cal_data
    print("\nYou might not qualify for Uk immigration.")
    a=points[0]
    cal_data.append(a)
    print("\n This is your Total Points:",str(sum(cal_data)))

def data_fn1():
    global cal_data
    for repeat in data:
        input_1=input(repeat + ", Do you Qualify?:- ")
        if repeat and input_1 == "y":
            pass_data_Madatory()
        elif repeat and input_1 == "n":
            fail_data()
        else:
            return print('\nInput Recorded.')

       
print(data_fn1())