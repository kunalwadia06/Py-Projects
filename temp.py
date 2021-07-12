# ------------------------Sorting a list[Using sort taking function input]-------------------------------
# ka=lambda s:s[0]
# a=[[1,4],[6,3],[5,7],[9,3]]
# j=a.sort(key=ka)
# print(a)

#
#
# ---------------------Factorial [Using Recursion]--------------------------
# def factorial(l):
#     return 1 if l == 1 or l == 0 else l * factorial(l - 1)
#
# k = int(input("Enter the number you wanna factorial of:~"))
# j = factorial(k)
# print("The factorial of ",k," is ",j)
#
# ---------------------Factorial [Using Recursion]--------------------------
# def factorial(n):
#     fac=1
#     for i in range (n):
#         fac=fac*(i+1)
#     print(fac)
#     return 0
#
# factorial(4)
#
#
#
#---------------------------Fibonacci Series------------------------------
# n = int(input("Enter the nth value for Fibonacci: "))
# a = 0
# b = 1
# sum = 0
# count = 0
# print("Fibonacci Series: ", end = " ")
# while(count <= n):
#   print(sum, end = " ")
#   count += 1
#   a = b
#   b = sum
#   sum = a + b

                         # -------------Using lambda with reduce function----------------------
# from functools import reduce
# fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
# print(fib(10))




#---------------------------Fibonacci nth Value------------------------------
# def fibonacci(n):
#     if n==0:return 0
#     elif n==1:return 1
#     else:return fibonacci(n-1)+fibonacci(n-2)
#
# j=int(input("Enter nth value of fibonacci series:~"))
# k=fibonacci(j)
# print(k)
#
#
#
#
# ----------------FAULTY CALCULATOR------------------------
# num1=int(input("enter number 1:-"))
# num2=int(input("enter number 2:-"))
# sign=input("enter + for plus , - for minus , * for multiply , / for division:-")
#
# if num1==54 and num2==3 and sign=='*':
#     print("answer is:555")
# elif num1==56 and num2==9 and sign=='+':
#     print("answer is:77")
# elif sign=='+':
#     print("answer is:",num1+num2)
# elif sign=='-':
#     print("answer is:",num1-num2)
# elif sign=='*':
#     print("answer is:",num1*num2)
# elif sign=='/':
#     print("answer is:",num1/num2)
#
#
# ------------------INPUT NUMBER GRATER THAN 100 TO WIN O.W. IT WILL RUN AND RUN------------
# while(1):
#     io=int(input("enter any number:-"))
#     if io>100:
#         print("you have entered number above 100")
#         break
#     else:
#         continue
#
#
# print("--------------------------GUESS THE NUMBER IN 5 TRIES [GAME]------------------")

# import random
#
# number=random.randint(0,100)
# attempts=1
# print("You have only 10 chances to win , Guess the number between 0 to 100....best of luck")
# while attempts<=10:
#     io = int(input("Guess any number:-"))
#
#     if io>number:
#         print("\nGuess LESSER number")
#
#     elif io<number:
#         print("\nGuess GREATER number")
#
#     else:
#         print("you won the game...")
#         print("You took ",attempts,"rounds to win")
#         break
#     print("\t\t\t\t\t\tLeft no. of guesses:-",10-attempts)
#     attempts+=1
#
# if attempts>10: print("Game over")
#
#
#
#
# -------------------SHORT HAND IF ELSE STATEMENT-------------------
# a=int(input("enter a:-"))
# b=int(input("enter b:-"))
#
# print("a is greater than b")if a>b else print("a is lesser than b")
#
#
#
# ---------------------------Functions and docstrings-----------------------------
# def jk(a, b):
#     """It returns the average of given two numbers"""
#     avg = (a + b) / 2
#     return avg
#
# i = jk(5, 3)
# print(jk.__doc__)
#
#
#
#
# -------------------TRY EXCEPT EXCEPTION HANDLING-----------------
# n1=(input("enter num1:-"))
# n2=(input("enter num2:-"))
# try:
#     print("sum of them is",int(n1)+int(n2))
# except Exception as e:
#     print(e)
#
# print("Done")
#
#
# --------------python files open() read() write() etc..-----------------
#
# v=open("knal.txt","r+")
#
# section:- print the file content
# vanch=v.read()
# print(vanch)
#
# section:- print file content line by line--[default mode]
# for line in v:
#     print(line,end="")
#
# section:-print file content line by line--[default mode]
# print(v.readline())
# print(v.readline())
# print(v.readline())
#
# section:- add content in the file--[when mode is on "a"]
# f=v.write("\ni wanna suck your tities so badly")
# print(f)
#
# section:- remove the content of file and add--[when mode is on "w"]
# v.write("\ni wanna suck your tities so badly")
#
# section:- access reading and writing both at the same time [when mode is on "r+"]
# print(v.read())
# v.write("\nwanna taste your wet pussy")
#
# v.close
#
#
#
# -----------------Astrologer's STARS--[Complex Method]-------------------
# n=int(input("How many rows you want to print:-"))
# o=int(input("Enter 0 or 1:-"))
# new=bool(o)
#
# if new==1:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new==0:
#     for i in range(n,0,-1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
#
# -----------------Astrologer's STARS--[Easy method]-----------------------
# n=int(input("How many rows you want to print:-"))
# option=int(input("Enter 0 or 1:-"))
#
# if option==1:
#     for i in range(1,n+1):
#         print("* "*int(i))
#
# elif option==0:
#     for i in range(n,0,-1):
#         print("* " * int(i))
#
# else:print("\n invalid option chosen!!!")
#
#
# ----------------------------Health management System [Using function]--------------------------------
#
# def gettime():
#     import datetime
#     return datetime.datetime.now()
#
#
# def take(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("kunal(exe).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("kunal(Diet).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("krish(exe).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("krish(Diet).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("nats(exe).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("nats(Diet).txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
#
#
# def retrieve(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("kunal(exe).txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("kunal(Diet).txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("krish(exe).txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("krish(Diet).txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("nats(exe).txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("nats(Diet).txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (kunal,krish,nats)")
#
#
# print("health management system: ")
# a = int(input("Press 1 for log the value and 2 for retrieve "))
#
# if a == 1:
#     b = int(input("Press 1 for kunal 2 for krish 3 for nats "))
#     take(b)
# elif a == 2:
#     b = int(input("Press 1 for kunal 2 for krish 3 for nats "))
#     retrieve(b)
# else:
#     print("Invalid Input !!!")

# ---------------------------- Health management System --------------------------------
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# x = int(input("Enter Patient name:~~\n1 for kunal  ||  2 for krish  ||  3 for nats:~ "))
# y = int(input("Enter Diet or Exercise:~~\n1 for Diet  ||  2 for Exercise:~ "))
# z = int(input("Enter Retrieve or Lock:~~\n1 for Retrieve  ||  2 for Lock:~ "))
#
# if x == 1 and y == 1 and z == 1:
#     with open("kunal(Diet).txt") as a:
#         b=a.read()
#         print("\n",b)
# elif x == 1 and y == 2 and z == 1:
#     with open("kunal(exe).txt") as c :
#         d=c.read()
#         print("\n",d)
#
# elif x == 1 and y == 1 and z == 2:
#     with open("kunal(Diet).txt") as m:
#         n=input("Write the new diet for kunal:~")
#         m.write("Time "+str([str(getdate())])+" :~\t"+n)
# elif x == 1 and y == 2 and z == 2:
#     with open("kunal(exe).txt","a") as o:
#         p=input("Write the new Exercise for kunal:~")
#         o.write("Time "+str([str(getdate())])+" :~\t"+p)
#
# elif x == 2 and y == 1 and z == 1:
#     with open("krish(Diet).txt") as e:
#         f=e.read()
#         print("\n",f)
# elif x == 2 and y == 2 and z == 1:
#     with open("krish(exe).txt") as g :
#         h=g.read()
#         print("\n",h)
#
# elif x == 2 and y == 1 and z == 2:
#     with open("krish(Diet).txt") as q :
#         r=input("Write the new diet for krish:~")
#         q.write("Time "+str([str(getdate())])+" :~\t"+r)
# elif x == 2 and y == 2 and z == 2:
#     with open("krish(exe).txt") as s:
#         t=input("Write the new Exercise for krish:~")
#         s.write("Time "+str([str(getdate())])+" :~\t"+t)
#
# elif x == 3 and y == 1 and z == 1:
#     with open("nats(Diet).txt") as i :
#         j=i.read()
#         print("\n",j)
# elif x == 3 and y == 2 and z == 1:
#     with open("nats(exe).txt") as k :
#         l=k.read()
#         print("\n",l)
#
# elif x == 3 and y == 1 and z == 2:
#     with open("nats(Diet).txt") as u :
#         v=input("Write the new diet for nats:~")
#         u.write("Time "+str([str(getdate())])+" :~\t"+v)
# elif x == 3 and y == 2 and z == 2:
#     with open("nats(exe).txt") as w :
#         wx=input("Write the new Exercise for nats:~")
#         w.write("Time "+str([str(getdate())])+" :~\t"+wx)
#
# else:
#     print("Invalid Input !!!")
#
#
#
#
#
# ---------------------------------- Rock Paper Scissor [GAME] ----------------------------------
#
# import random
# he=0
# me=0
# d=0
#
# k=1
# while k<=5:
#     a = ['Rock', 'Paper', 'Scissor','Rock', 'Paper', 'Scissor','Rock', 'Paper', 'Scissor']
#     b = random.choice(a)
#     j = input("Press r for Rock\t||\t  Press p for Paper\t||\t  Press s for Scissor:~ ")
#     if b == 'Rock' and j == "r":
#         print("His choise was", b)
#         print("Match Draww !!!")
#         d+=1
#
#     elif b == 'Rock' and j == "p":
#         print("His choise was", b)
#         print("You won !!!")
#         me+=1
#
#     elif b == 'Rock' and j == "s":
#         print("His choise was", b)
#         print("He won !!!")
#         he+=1
#
#     elif b == 'Paper' and j == "r":
#         print("His choise was", b)
#         print("He won !!!")
#         he+=1
#
#     elif b == 'Paper' and j == "p":
#         print("His choise was", b)
#         print("Match Draww !!!")
#         d+=1
#
#     elif b == 'Paper' and j == "s":
#         print("His choise was", b)
#         print("you won !!!")
#         me+=1
#
#     elif b == 'Scissor' and j == "r":
#         print("His choise was", b)
#         print("You won !!!")
#         me+=1
#
#     elif b == 'Scissor' and j == "p":
#         print("His choise was", b)
#         print("He won !!!")
#         he+=1
#
#     elif b == 'Scissor' and j == "s":
#         print("His choise was", b)
#         print("Match Draww !!!")
#         d+=1
#
#     else:
#         print("Invalid Input")
#         break
#     print("\t\t\t\t\t\t\t\t\t\t\t\t",5-k," Round left")
#     k+=1
#
# if k>5 :print("\n------------------------------------ Result ------------------------------------\n")
# print("You won ",me,"Times\t\t","he won ",he," Times\t\t",d,"Time Match Drawed")
# if me>he:
#     print("\n\t\t\t\t\t\tYou won the Game...Congratulations :)")
# else:print("\n\t\t\t\t\t\tHe won the Game... :(")
#
#
#
#
#
#
# ----------------------------------- To Play Audio -----------------------------------------
# from playsound import playsound
#
# n = '/home/kunal/Music/Malhari.mp3'
# playsound(n)
