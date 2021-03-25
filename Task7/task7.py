## 1 Square root
import math
def square_root(D):
    C =50
    H=30
    Q = math.sqrt((2*C*D)/H)
    return Q


D = int(input("Enter the value"))

print(square_root(D))

###2 class and subclass
class Shape:
    def setArea(self):
        self.area = 0


class Square:
    def __init__(self,len):
        self.len = len