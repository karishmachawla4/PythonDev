#### 3 flowchart

a,b,c = 10,20,30
avg = (a+b+c)/3
print("average =", avg)
if avg > a and avg > b and avg >c:
    print("avg is higher than a,b,c")
elif avg > a and avg > b:
    print("avg is higher than a and b")
elif avg > a and avg> c:
    print("avg is higher than a and c")
elif avg > a:
    print("print is higher than a")
else:
    if avg > b:
        print("avg is higher than b")
    else:
        print("avg is higher than c")

