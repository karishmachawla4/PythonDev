### 1 list of different data types
list1 = [1,"John",54.5,1+2j]

####2 list of 5
list= []


#### 3 sum and multiplication of all items
test = [1,2,3,4,5]
sum1, mult1 = 0,1
for i in test:
    sum1 = sum1 + i
    mult1 = mult1 * i
## another way for sum
sum2 = sum(j for j in test)
print("sum of all nums", sum1)
print("product of all nums in list", mult1)
# print("another way for sum2",sum2)

###4 largest and smallest in list
nums =[47,34,56,7,12,4,16,22,23]
min = nums[0]
max= nums[0]

for i in nums:
    if min > i:
        min = i
    if max < i:
        max = i
print("smallest element  of the list", min)
print("largest element of the list", max)

#### 5 list remove even numbers
predefined = [56,33,55,67,48,81,25,10]
new_list=[]
for i in predefined:
    if i % 2 != 0:
        new_list.append(i)
print(new_list)

###6 list of sqaure of nums
square_list = []
for i in range(1,31):
    if i <=5 or i> 25:
        square_list.append(i*i)
print(square_list)

##7 list replace and concatination
input1 = [1,3,5,7,9,10]
input2 = [2,4,6,8]
input1.pop(-1)
input1 = input1 + input2
print(input1)



