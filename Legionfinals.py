import os
#ACTIVITIES

def act1():
    print("Hello World")

def act2():
    name = input( "Please enter a name -----> " )
    print ( "Hi!" + name )

def act3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")

    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")
def act4():
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)

    print("The sum of", number1 ,"and",number2,"is",answer)

def act5():

    print("\nThis is my activity 5\n")
    print("\nFARENHEIT TO CELCIUS CONVERTER")
    temp = eval(input("\nEnter a temperature in Farenheit ---> "))
    celcius = (temp -32) * 5 / 9
    print("\nThe conversion of ", temp , " degrees Farenheit is ", celcius , " degrees Celcius.")
    print(f"\nThe conversion of {temp} degrees Farenheit is {celcius} degrees Celcius")
    (round(celcius, 2))
    print(f"\nThe convertion of {temp} degrees Farenheit is {round(celcius,2)} degrees Celcius.")


def act6():

    x = 5

    print(x)

    x = x + 10

    print(x)

    x = x +15

    print(x)

    x += 10 

    print(x)

    x+=20

    print(x)

def act7():
    gold = 0
    name=input('Hi, enter your name:  ')
    hasMine=input('Did you mine gold today?  ')
    if hasMine.lower() == "yes":
        gold +=1
        print(f'Hi! {name}, Today you have a total of {gold} gold')
    else:
        print(f'Hi! {name}, Today you have a total of {gold} gold')

def act8():
    print("\nThis is my activity 8\n")
    password = input('Enter your password---> ')
    if password.lower() == "password" :
        print('Access Granted!!!!')
        print('Enjoy using the system')
    elif password.lower() =='secret':
        print('Access Granted!!!!')
        print('Enjoy using the system')
    else:
        print('Access Denied!!!!!')
    print('Thank you for using the system')

def act9():

    age = eval(input("\nEnter your age here ---> "))

    if age >=100:
        print("\nWelcome to Ancient bracket")

    elif age >= 60:
        print("\nWelcome to Senior Citizen bracket")

    elif age >=46:
        print("\nWelcome to Post Adulthood bracket")

    elif age >=32:
        print("\nWelcome to Mid Adulthood bracket")

    elif age >=19:
        print("\nWelcome to Early Adulthood bracket")

    elif age >=14:
        print("\nWelcome to Teenager bracket")

    elif age >=8:
        print("\nWelcome to Pre-Teen bracket")

    elif age >=1:
        print("\nWelcome to Toddler bracket")


def act10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Cotta')

    else:
        print('Thanks for stopping by')
def act11():
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')
def act12():
    for cycle in range (10,0,-1):
        print(cycle)
def act13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")

def act14():
        for x in range ( 0, 11,):
            print(x,end =" ")
        for y in range (0, 11):
            print("*",end = " ")
        print("")

def act15():
    for x in range ( 0, 11,):
        print(x,end =" ")
        for y in range (0, x):
            print("*",end = " ")
        print("")
def act16():
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(11, x, -1):
            print(" * ",end=" ")
        print()

def act17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()

def act18():
    tri = eval(input("Enter a number of triangle---> "))

    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()

def act19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
        
def act20():

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
            continue

def act21():

    def pang_hi():
        print("HI IT1C")

    def pang_hi_v2(name):
        print(f"Hello {name}")

    def termi():
        print("PROGRAM TERMINATED")

    def activity_2():
        number1 = eval (input("enter a number--->" ))
        number2 = eval (input("enter another number--->" ))
        answer = (number1 + number2)
        print(f"The sum of {number1} and {number2} is {answer}")

    tuloy =  True
    while tuloy == True:
        ask = input("Enter a name---> ")

        if ask.lower() != "stop":
            pang_hi_v2(ask)
            if ask == "2":
                activity_2()
                continue
        else:
            termi()
            break

def act22():
    def activity22():
        def activity1():
            print("Hello World")
        activity1()
    activity22()

def act23():
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"THe factorial of 13 is {factorial(13)}")

def act24():
    pass
def act25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)


    # END OF ACTIVITIES

    
    # START CODE_CHALLENGES


def code_challenge1():
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")
def code_challenge2():
    name = input("\nType your name here --->")
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*","  Hi",name,"\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")
def code_challenge3():
    lname = input("\nPlease type your last name ---> ")
    fname = input("\nPlease type your first name ---> ")
    mname = input("\nPlease type your middle name ---> ")
    age = input("\nPlease type your age ---> ")
    gender = input("\nPlease type your gender ---> ")
    birthdate = input ("\nPlease type your birth date ---> ")
    birthmonth = input ("\nPlease type your birth month ---> ")
    birthyear = input ("\nPlease type your birth year ---> ")
    maritalStatus = input("\nPlease type your marital status ---> ")
    religion = input("\nPlease type your religion ---> ")
    nationality = input("\nPlease type your nationality ---> ")
    height = input("\nPlease type your height in cm ---> ")
    weight = input("\nPlease type your weight in kg ---> ")
    contactnumber = input("\nPlease type your contact number ---> ")
    email = input ("\nPlease type your e-mail ---> ")
    address = input("\nPlease type your home address ---> ")
    fname = input("\nPlease type your father's full name ---> ")
    mname = input("\nPlease type your mother's full name ---> ")
    hobby = input ("\nPlease type your hobby ---> ")
    print ("\nHello, My name is" , lname , fname , mname ,  "and I'm" , str(age) , "years old," , gender , "\n I was born on" , birthmonth , birthdate , birthyear , "\n And right now I am" , maritalStatus , "\n My religion is" , religion , "\n I am" , nationality ,  "and my height is" , height , "cm" " and I'm" , weight , "kl" , "\n You can contact me at my number" , contactnumber , "\n And you may also contact me through my e-mail" , email , "\n I live in" , address , "\n My father is" , fname , "and my mother is" , mname , "\n And lastly, I love" , hobby )

    
def code_challenge4():
    number1 = eval(input("\nEnter a number ---> "))
    number2 = eval(input("\nEnter another number ---> "))
    answer1 = number1 + number2 
    answer2 = number1 - number2 
    answer3 = number1 * number2 
    answer4 = number1 / number2 
    answer5 = number1 % number2 
    answer6 = number1 ** number2 
    answer7 = number1 // number2 

    print("\nThe sum of " , number1 , " and " , number2 , " is " , answer1)
    print("The difference of " , number1 , " and " , number2 , " is " , answer2)
    print("The product of " , number1 , " and " , number2 , " is " , answer3)
    print("The quotient of " , number1 , " and " , number2 , " is " , answer4)
    print("The remainder of " , number1 , " and " , number2 , " is " , answer5)
    print("The exponent of " , number1 , " and " , number2 , " is " , answer6)
    print("The floor division of " , number1 , " and " , number2 , " is " , answer7)
def code_challenge5():
    lname = input("\nType your last name ---> ")
    fname = input("\nType your first name ---> ")
    mname = input("\nType your middle name ---> ")

    prtt1 = eval(input("\nAmount to deposit ---> "))

    blck1 = prtt1 // 1000
    brtt1 = prtt1 % 1000

    blck2 = brtt1 // 500
    brtt2 = brtt1 % 500

    blck3 = brtt2 // 200
    brtt3 = brtt2 % 200

    blck4 = brtt3 // 100
    brtt4 = brtt3 % 100

    blck5 = brtt4 // 50
    brtt5 = brtt4 % 50

    blck6 = brtt5 // 20
    brtt6 = brtt5 % 20

    blck7 = brtt6 // 10
    brtt7 = brtt6 % 10

    blck8 = brtt7 // 5
    brtt8 = brtt7 % 5

    blck9 = brtt8 // 1
    brtt9 = brtt8 % 1

    print("\nHello", fname , mname , lname ,"this is the breakdown of your deposit: \n")
    print(blck1 ," - 1000")
    print(blck2 ," - 500")
    print(blck3 ," - 200")
    print(blck4 ," - 100")
    print(blck5 ," - 50")
    print(blck6 ," - 20")
    print(blck7 ," - 10")
    print(blck8 ," - 5")
    print(blck9 ," - 1")
def code_challenge6():
    blck1 = eval(input("\nEnter your grades in Prelims ---> "))
    blck2 = eval(input("\nEnter your grades in Midterms ---> "))
    blck3 = eval(input("\nEnter your grades in Semi-Finals ---> "))
    blck4 = eval(input("\nEnter your grades in Finals ---> "))
    blck5 = eval(input("\nEnter your grades in Quizzes ---> "))
    blck6 = eval(input("\nEnter your grades in Projects ---> "))

    if (blck1 >= 65 and blck1 <=100) and (blck2 >= 65 and blck2 <=100) and (blck3 >= 65 and blck3 <=100) and (blck4 >= 65 and blck4 <=100) and (blck5 >= 65 and blck5 <=100) and (blck6 >= 65 and blck6 <=100):
        brtt = (blck1 * 0.15) + (blck2 * 0.15) + (blck3 * 0.15) + (blck4 * 0.15) + (blck5 * 0.25) + (blck6 * 0.15) 
        if brtt >= 75:
            print("\nCongratulations for passing the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
        else:
            print("\nYou failed for the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
    else:
        print("\nINVALID GRADES")
def code_challenge7():
    name = input("\nEnter your name ---> ")
    grocery = input("\nDid you buy a grocery? (yes/no) ---> ")
    if grocery.lower() == "yes":

        item = input("\nName of the item ---> ")
        price = eval(input("\nPrice of the item ---> "))
        amount = eval(input("\nExact amount given ---> "))
        age = eval(input("\nAge ---> "))
        
        tax = 0.123
        ttm = price * tax
        total = price + ttm
        
        if age <= 59:
            change = amount - total

            print(f"\nHi {name} you purchased a {item} , with a price of {price} plus 12.3% of tax ({ttm}) total of ({total}) ")
            print(f"\nAmount given ---> ({amount})php ")
            print(f"\nChange ---> [round(change , 2)] ")
            print("\nThank you for shopping! ")

        if age >= 60:	
            discount = 0.052
            ddm = price * 0.052
            dtotal = price - ddm
            cchange = amount - dtotal

            print(f"\nHi {name} you paid a price of {price}, for an {item} with a discount of 5.2% ({ddm}). The total amount you paid is (round{dtotal , 2}) ")
            print(f"\nAmount given ---> ({amount})php ")
            print(f"\nChange ---> {cchange} ")
            print("\nThank you for shopping! ")
        
        
    else:
        print("\nThank you for checking in")	
def code_challenge8():
    sum = 0
    odd = 0
    even = 0

    for j in range(1,11):
        num = int(input(f"\nEnter a Number {j}:  "))
        sum += num 
        if num % 2 == 0:
            odd+=num
        else:
            even+=num

    print(f"\nThe sum of all given numbers is {sum}")
    print(f"\nThe even of all given numbers is {even}")
    print(f"\nThe odd of all given numbers is {odd}")
def code_challenge9():
    for x in range(0,11):
        print(" ",end=" ")
        for y in range(0,x):
            print(" ",end=" ")
        for z in range(x,10):
            print("*",end=" ")
        print()
def code_challenge10():
    for x in range (6, 1, -1):
        for y in range(x, 1, - 1):
            print(" ", end =" ")
        for z in range(x, 7, 1):
            print("*",end=" ")
        for j in range (x, 6, 1):
            print("^",end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x, 1):
            print(" ", end =" ")
        for z in range(7, x, -1):
            print("^",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print()
def code_challenge11():
    for x in range (7, 1, -1):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(7, x,- 1):
            print("*",end=" ")
        for j in range (5, x ,- 1):
            print("*",end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(4, x, -1):
            print("*",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print()
def code_challenge12():
    for j in range(6,1-1):
        for v in range(1,j):
            print(" ",end=" ")
        for q in range(7,j -1):
            print("*",end=" ")
        for q in range(6,j -1):
            print("*",end=" ")
        print()

    for t in range(1,7):
        for p in range(1,5):
            print(" ",end=" ")
        for s in range(1,4):
            print("*",end=" ")
        print()
def code_challenge13():
    for x in range (6, 1, -1):
        for z in range(x, 1, +1):
            print(" ", end =" ")
        for y in range(6, x, 1):
            print(y, end =" ")
        for j in range (x, 1, +1):
            print(j, end =" ")
        print()

    for x in range (1,7):
        for y in range(6, x, - 1):
            print(" ", end =" ")
        for z in range(x, 1, -1):
            print(z, end =" ")
        for j in range (1, x + 1):
            print(j, end =" ")
        print()

    for x in range (6, 1, -1):
        for y in range(x, 1, - 1):
            print(" ", end =" ")
        for z in range(x, 7, +1):
            print(z,end=" ")
        for j in range (x, 6, 1):
            print(j,end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x, 1):
            print(" ", end =" ")
        for z in range(7, x, -1):
            print(z,end=" ")
        for j in range (x, 6, +1):
            print(j,end=" ")
        print()
def code_challenge14():
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number--->  "))
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break

        else:
            a += number
            continue
def code_challenge15():
    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue
def code_challenge16():
    def bankacc():
        print(f"\nWelcome to Kabayan Bank")
        print(f"Create account first to enjoy our service")
    bankacc()
    while bankacc:
        zapp = input("\nSelect an option: \n\n\t1 - Create an account \n\t2 - Withdraw \n\t3 Check Balance \n\t4 - Stop \n\nEnter your option: ").lower()
        if zapp == "1":
            name = input("\nEnter your name:  ")
            deposit = int(input(f"\nEnter amount to deposit: "))
            print(f"\nAccount for {name} has been created, with a deposit of {deposit} PHP")
            continue
        elif zapp == "2":
            withdraw = int(input("\nEnter the amount you want to withdraw:  "))
            deposit -= withdraw
            print(f"\nYou withdraw, {withdraw} PHP.")
            if withdraw > deposit:
                print("\nSorry you have Insufficient Balance.")
                break
            else:
                continue
        elif zapp =="3":
            print(f"\nYour current balance is {deposit}PHP.")
            a1 = deposit // 1000
            aa1 = deposit % 1000
            a2 = aa1 // 500
            aa2 = aa1 % 500
            a3 = aa2 // 200
            aa3 = aa2 % 200
            a4 = aa3 // 100
            aa4 = aa3 % 100
            a5 = aa4 // 50
            aa5 = aa4 % 50
            a6 = aa5 // 20
            aa6 = aa5 % 20
            a7 = aa6 // 10
            aa7 = aa6 % 10
            a8 = aa7 // 5
            aa8 = aa7 % 5
            a9 = aa8 // 1
            aa9 = aa8 % 1
            print("\nThe current balance of your account is: ")
            print("\n" , a1 ,"-  1000" , "\n" , a2 ,"-  500" , "\n" , a3 ,"-  200" , "\n" , a4 ,"-  100" ,"\n" , a5 ,"-  50" , "\n" , 6 ,"-  20" ,"\n" , a7 ,"-  10" , "\n" , a8 ,"-  5" ,"\n" , a9 ,"-  1\n")
            print(f"Total balance--->{deposit}")
            continue
        elif zapp == "4":
            print(f"\nProgram terminated, Thank you for supporting our company.")
            break
        else:
            print("Invalid Choice, Please try again.")
            continue

#MENU

def menu():
    while True:
        print(f"\n\t\t\t||INFORMATION TECHNOLOGY 1-C||\t\t\n")
        print(f"\n\t\t\t||WELCOME TO MY ACTIVITY PROGRAM||\t\t\n")
        print("\n\t\t\t_______________________| Activities |__________________\n")
        print("\t\t\t 1 - act1                       15 - act13 ")
        print("\t\t\t 2 - act2                       14 - act14 ")
        print("\t\t\t 3 - act3                       15 - act15 ")
        print("\t\t\t 4 - act4                       16 - act16 ")
        print("\t\t\t 5 - act5                       19 - act17 ")
        print("\t\t\t 6 - act6                       20 - act18 ")
        print("\t\t\t 7 - act7                       21 - act19 ")
        print("\t\t\t 8 - act7                       22 - act20 ")
        print("\t\t\t 9 - act9                       23 - act21 ")
        print("\t\t\t 10 - act10                     24 - act22 ")
        print("\t\t\t 11 - act11                     23 - act23 ")
        print("\t\t\t 12 - act12                     24 - act24 ")
        print(f"act 0 \t\t\t type 'Back'to back menu")
        print("\n\t\t\t______________________________________________\n\n")

        print(f"n\t\tINFORMATION TECHNOLOGY 1-C")
        print(f"\n\t\tWELCOME TO MY CODE_CHALLENGE")
        print("\n\t\t\t_____________________| code_challenge |_____________________\n")
        print("\t\t\t|| CC_1 - code_Challenge 1               CC_9 - code_Challenge 9   ||")
        print("\t\t\t|| CC_2 - code_Challenge 2               CC_10 - code_Challenge 10 ||")
        print("\t\t\t|| CC_3 - code_Challenge 3               CC_11 - code_Challenge 11 ||")
        print("\t\t\t|| CC_4 - code_Challenge 4               CC_12 - code_Challenge 12 ||")
        print("\t\t\t|| CC_5 - code_Challenge 5               CC_13 - code_Challenge 13 ||")
        print("\t\t\t|| CC_6 - code_Challenge 6               CC_14 - code_Challenge 14 ||")
        print("\t\t\t|| CC_7 - code_Challenge 7               CC_15 - code_Challenge 15 ||")
        print("\t\t\t|| CC_8 - code_Challenge 8               CC_16 - code_Challenge 16 ||")
        print(f"CC  0 \t\t\t type u")
        print("\n\t\t\t______________________________________________\n\n")

        LEGION = input("ENTER A NUMBER:")
        if LEGION == "Exit" or LEGION == "0":
            break
        elif LEGION != "Exit":
            if LEGION == "1":
                y = input("Enter your name here:")
                act1 (y)
                continue
            elif LEGION == "2":
                act2()
                continue
            elif LEGION == "3":
                act3()
                continue
            elif LEGION == "4":
                act4()
                continue
            elif LEGION == "5":
                act5()
                continue
            elif LEGION == "6":
                act6()
                continue
            elif LEGION == "7":
                act7()
                continue
            elif LEGION == "8":
                act8()
                continue
            elif LEGION == "9":
                act9()
                continue
            elif LEGION == "10":
                act10()
                continue
            elif LEGION == "11":
                act11()
                continue
            elif LEGION == "12":
                act12()
                continue
            elif LEGION == "13":
                act13()
                continue
            elif LEGION == "14":
                act14()
                continue
            elif LEGION == "15":
                act15()
                continue
            elif LEGION == "16":
                act16()
                continue
            elif LEGION == "17":
                act17()
                continue
            elif LEGION == "18":
                act18()
                continue
            elif LEGION == "19":
                act19()
                continue
            elif LEGION == "20":
                act20()
                continue
            elif LEGION == "21":
                act21()
                continue
            elif LEGION == "22":
                act22()
                continue
            elif LEGION == "23":
                act23()
                continue
            elif LEGION == "24":
                act24()
                continue
            elif LEGION == "25":
                act25()
                continue



            elif LEGION == "CC_1":
                code_challenge1()
                continue
            elif LEGION== "CC_2":
                code_challenge2()
                continue
            elif LEGION == "CC_3":
                code_challenge3()
                continue
            elif LEGION == "CC_4":
                code_challenge4()
                continue
            elif LEGION == "CC_5":
                code_challenge5()
                continue
            elif LEGION == "CC_6":
                code_challenge6()
                continue
            elif LEGION == "CC_7":
                code_challenge7()
                continue
            elif LEGION == "CC_8":
                code_challenge8()
                continue
            elif LEGION == "CC_9":
                code_challenge9()
                continue
            elif LEGION == "CC_10":
                code_challenge10()
                continue
            elif LEGION == "CC_11":
                code_challenge11()
                continue
            elif LEGION == "CC_12":
                code_challenge12()
                continue
            elif LEGION == "CC_13":
                code_challenge13()
                continue
            elif LEGION == "CC_14":
                code_challenge14()
                continue
            elif LEGION == "CC_15":
                code_challenge15()
                continue
            elif LEGION == "CC_16":
                code_challenge16()
                continue
            elif LEGION.lower()== "Back":
                return menu
            else:
                print("SORRY TRY AGAIN.")
                continue
menu()