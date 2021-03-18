#1 Program to find divisible and print details
def divisible(num):
    if ((num%3==0) and (num%5 ==0)):
        return ("Consultadd - Python Training")
    elif (num%3 ==0) :
        return ("Consultadd")
    elif (num%5 ==0) :
        return ("Python Training")
    else:
        return ("Your number is not divisible by any")



# num = int(input("Enter the input :"))
# print(divisible(num))
#2 Operator check and function

def calculation(op,num1,num2):
    if op == 1:
        return  (num1 + num2)
    elif op ==2:
        return (num1 - num2)
    elif op==3:
        return (num1/num2)
    elif op ==4:
        return (num1 * num2)


# print("Please choose operation 1: Addition , 2: Substraction , 3: Division, 4: Multiplication , 5: Average")
# operation = int(input("please choose the operation option you want to perform "))
# if operation <= 4:
#     num1, num2= (input("Enter two numbers: ")).split()
#     # num2 = int(input("Enter two number"))
#     num1, num2 = int(num1), int(num2)
#     result = (calculation(operation,num1,num2))
# else:
#     first = int(input("Enter first number : "))
#     second = int(input("Enter second number: "))
#     result = (first + second)/2
# if result < 0 :
#     print("NEGATIVE")
# print(result)

### 4
## Break and Continue
while True:
    inp = int(input("Enter the number :"))
    if inp < 0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue



### 5 Program for divisible of 7 but not 5 between  2000 and 3200
# list1 = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i%5 != 0:
#         list1.append(i)
# print(list1)



##6 Output for the cases given

## 123
## 0 error
## 1 error
## 2 error
## 01234

### 7 Continue
# for i in range(0,7):
#     if i ==3 or i ==6:
#         continue
#     else:
#         print(i)



# 8 Count the letter and digits
def check_input(user_input):
    let_count, dig_count = 0 ,0
    for i in user_input:
        if i.isdigit():
            dig_count += 1
        elif i.isalpha():
            let_count +=1
    print("Letters :", let_count , end= "   ")
    print("Digits : ", dig_count)

# user_input = input(" Enter any string input ")
# (check_input(user_input))


#### 9 Guess the lucky number
import random
number = int(input(" Guess the lucky number between 1 - 10: "))
lucky = random.randint(1, 10)
while number != "lucky":
        if lucky == number:
            print("You guess it right")
        else:
            number = int(input(" Guess the lucky number between 1 - 10: "))





