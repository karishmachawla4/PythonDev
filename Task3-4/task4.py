### 1 reverse a string

test = "1234abcd"
test2 = ""
print(test[::-1])
n =len(test) -1
while n >= 0:
    test2 = test2 + test[n]
    n = n -1
print(test2)

### 2 No of upper and lower case in string
def cases(s):
    lower_count, upper_count = 0,0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count +=1
    return upper_count,lower_count

s ="abcSdefPghijQkl"
u,l= cases(s)
print("No.of Uppercase characters: ", u,"No.of lower case characters:", l)

#### 3 unique list
def unique(lm):
    uni =[]
    for i in lm:
        if i in uni:
            continue
        else:
            uni.append(i)
    return uni

temp1 = [1,2,3,4,2,4,6,7,3,5,8,8]
print(unique(temp1))

### 4 hypen handling
###Write a program that accepts a hyphen-separated sequence of words as input and prints the words
### in a hyphen-separated sequence after sorting them alphabetically
sample_string = "this-is-a-good-practice-test"
sample_list = sample_string.split("-")
sorted_list = sorted(sample_list)
print("-".join(sorted_list))


### captilalized all charcater from input
input1 = "Hello world Practice makes man perfect"
##option1 to just print upper
##print(input1.upper())

## option two iterate the string an make every word upper
output1 = ""
for i in input1:
    output1 = output1 + i.upper()
print(output1)

##funtion to perform sum of two string input
def sum_string(a,b):
    print(int(a)+int(b))

sum_string("3","5")


#### print max string
def longeststring(x,y):
    if len(x)>len(y):
        print(x)
    elif len(x) < len(y):
        print(y)
    else:
        print(x)
        print(y)

x="Python is very easy"
y="AWS is very intresting"
longeststring(x,y)


### Show number and if they are even or odd
def showNumbers(limit):
    type = ""
    for i in range(0,limit+1):
        if i %2 == 0 :
            type = " EVEN"
        else:
            type = " ODD"
        print( str(i) + type)

showNumbers(3)


