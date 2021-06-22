import datetime
choose='y'
while choose.upper()=='Y':
    userdata = input('Please Enter Your DOB (dd/mm/yyyy) :')
    birthday = datetime.datetime.strptime(userdata,'%d/%m/%Y').date()
    #print(birthday)s
    currentDate = datetime.date.today()
    #print(currentDate)
    days =currentDate - birthday
    #print(type(days))
    inte=days.days
    #print(type(int))
    if inte > 1830:
        print("You Can Take a Aadhaar With Bio-Metric Data")
    else:
        print("You Can't Take a Aadhaar With Bio-Metric Data")
    while True:
        ch=input("Enter Y to continue and N to Exit:")
        if ch.upper()=='Y' or ch.upper()=='N':
            choose=ch
            break
        else:
            print("Please Enter The Correct Choose  :")
            continue
        