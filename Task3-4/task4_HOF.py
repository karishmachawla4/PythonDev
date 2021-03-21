## 10 progrom to filter even numbers
nums = [ i for i in range(1,21)]
result = filter(lambda x : x%2==0 ,nums)
print(list(result))

##11 list of square numbers usign map() and filter()
numbers = [1,2,3,4,5,6,7,8,9,10]
result1 = list(filter(lambda x : x%2==0 ,numbers))

output = list(map(lambda y : y*y,result1))
print(output)


## compute 5/0 with try exception
def compute(n):
    val = n/0
try:
    compute(5)
except ZeroDivisionError:
    print("Division by zero")



#### 13 flatten a list using reduce
# from _functools  import reduce
# list1= [1,2,3,4,5,6,7]
# result= reduce(lambda res, n : 10* res + d,list1)
# print(result)

###14 program to find values divisible by 3 but not multiple of 7

input =[i for i in range(1,50)]
multi = list(filter(lambda i : i%3 !=0 and i%7==0,input))
print(multi)


##15 Multiple elements of list by itself

list_input = [ 1,2,3,4,5,6,7,8,9,10]
def multi(n):
    return n*n

print(list(map(multi,list_input)))


