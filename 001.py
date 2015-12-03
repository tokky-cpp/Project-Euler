#coding:utf-8

def multiple_n(x,n):
    if x%n == 0:
        return True
    return False

sum = 0
for i in range(1000):
    if multiple_n(i,3) or multiple_n(i,5):
        sum += i

print sum
