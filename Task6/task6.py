### Task 6
### 1 List comprehension

statement = "India is the BEST"
res =[]
for ch in statement:
    if ch.isupper():
        res.append(ch)
print(res)

## option2
#res1 = [ ch for ch in statement if ch.isupper()]
#print(res1)

### 2 Two dictionary to one dictionary
students=['Smit','Jaya','Rayyan']
subjects = ['CSE','Networking','Operating System']
#option 1 using one loop
result = {}
for i in range(len(students)):
    result[students[i]] = subjects[i]
# print(result)

## using 2 loops
result1 = {}
for key in students:
    for val in subjects:
        result1[key] = val
# print(result1)

## with the use of zip
list1 ={}
list1 = dict(zip(students,subjects))
print("Final students details :" , str(list1))



### 3 yield ,next , generators
#   3_1. yield and Generator
def yieldexample():
    yield 5
    yield 10


for val in yieldexample():
    print(val)

#   3_2. next
test = [1, 2, 3]
r1 = iter(test)
print(next(r1))
print(next(r1))


###4
input_s = " Consultadd Training"
print("Input_string :", input_s)
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
output_str = ""
for char in rev_str(input_s):
    # print(char)
    output_str = output_str + char
print("Output reversed string: ",output_str)

##5 decorator
def decorator_fun(func):
    def inner():
        print("Inside the decoration")
        func()
        print("I got decorated")
    return inner()

@decorator_fun
def ordinary():
    print("I am ordinary")




