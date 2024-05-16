print("Task:1 vote")
age=2
if(age>=18):
    print("you are elligible to vote")
else:
    print("you are not elligible to vote")
print()

print("Task:2 divisible by 7 or not")
num=14
if(num%7==0):
    print(num,"is divisible by 7")
else:
    print(num,"is not divisible by 7")
print()

print("Task:3 multiple of 5 ")
x=4
if(x%5==0):
    print("hello")
else:
    print("bye")
print()

print("Task:4 electric bill")
unit=1000
amt=0
if(unit<=100):
    amt=0
elif(unit>100 and unit<=200):
    amt=(unit-100)*5
elif(unit>200):
    amt=500+(unit-200)*10
print("You have to pay rs",amt)
print()

print("Task:5 last digit")
num1=145
lastDigit=num1%10
print("The last digit is:",lastDigit)
print()

print("Task:6 last digit is divisibel by 3 or not")
num1=149
lastDigit=num1%10
print("The last digit is:",lastDigit)
if(lastDigit%3==0):
    print("last digit is divisibel by 3")
else:
    print("last digit is not divisibel by 3")
print()

print("Task:7 Road tax for bike")
costOfBike=50000
tax=0
if(costOfBike>100000):
    tax=costOfBike*0.15
elif(costOfBike>50000 and costOfBike<=100000):
    tax=costOfBike*0.10
elif(costOfBike<=50000):
    tax=costOfBike*0.05
print("Cost of your bike:",costOfBike)
print("Tax to be paid:",tax)
print()

print("Task:8 sunday monday")
day=3
if(day==1):
    print("sunday")
if(day==2):
    print("monday")
if(day==3):
    print("tuesday")
if(day==4):
    print("wednesday")
if(day==5):
    print("thursday")
if(day==6):
    print("friday")
if(day==7):
    print("saturday")




    
    























    
    
