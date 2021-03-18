# 1 assignment
a,b,c = 1,2.01,'string'
print(a,b,c)

#2 complex variable
a = 1 + 2j
b = 10
a, b = b, a
print(a, b)

#3a swapping two number with third
a , b = 5, 9
print("values before swapping:", a,b)
temp = a
a = b
b = temp
print("values after swapping:" ,a,b)

#3b swapping two numbers
a = a+b
b = a-b
a = a-b
print(a,b)

#4 user input
user_input  = input("Enter your name ")
print("Hello" , user_input)

#5 Program task
x = int(input("enter first number between 1 - 10: "))
y = int(input("enter second number between 1- 10: "))

z = x + y
result = z  + 30
print("The final output is :", result)


#6 Check datatype of the user input value

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print(" The data type of the input value is : int")
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print(" The data type of the input value is : float")
        except ValueError:
            print(" The data type of the input value is : String")

inp = input("Enter any input")
check_user_input(inp)


# 7 Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.

assignmentSection = "Task1" #lowerCamel
AssignmentSection = "Task1" #UpperCamel/Pascal Case
assignment_section = "Task1"  #snake_case
ASSIGNMENTSECTION = "Task11"  # UPPER CASE


#8 Data type value assignment
a = 12.3
print(a)
a = "Testing"
print(a)

#When a new data type value is assiged to a variable it gets updated with the new value and its data type.
