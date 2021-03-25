### SyntaxError
def add(a,b):
    try:
        if a == b:
            print("testing")
            raise SyntaxError
    except SyntaxError:
        print("Synatx error in file")

add("3",2)


### 2 open file with the use of argv
import sys
try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("File Not found. Please enter the correct file again.")


## 3
### Handle error if length
try:
    nums = input("Enter any four digit number")
    if len(nums) == 4:
        print("The four digit number is ", nums)
    else:
        raise OverflowError

except OverflowError:
    print("The length is too short/long !!! Please provide only four digits")