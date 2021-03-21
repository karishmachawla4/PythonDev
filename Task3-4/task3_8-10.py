### 8 Dictionary concatination
a={1:10,2:20}
b={3:30,4:40}
for key, val in b.items():
    if key in a:
        a[key] = val + 1
    else:
        a[key] = val
print(a)


##9 dictionary in form x : x*x
def dict_sqaure(n):
    result = {}
    for i in range(1,n+1):
        result[i] = i*i
    return result

print(dict_sqaure(5))

## 10 list and tuple
sample_input = input("enter the number: ")
sample_input = sample_input.replace(",","")
print(list(sample_input))
print(tuple(sample_input))