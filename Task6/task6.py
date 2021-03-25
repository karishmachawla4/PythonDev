
### Task 6
### 1 List comprehension

statement = "India is the BEST"
res =[]
for ch in statement:
    if ch.isupper():
        res.append(ch)
print(res)

## option2
res1 = [ ch for ch in statement if ch.isupper()]
print(res1)

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


###4
input_s = " Consultadd Training"
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str(input_s):
    print(char)
