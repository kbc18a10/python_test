import math

def CalcDistance(ax, ay, bx, by):
    dx = ax - bx
    dy = ay - by
    result = math.sqrt(dx ** 2 + dy ** 2)
    return result

def IsPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for j in range(3, x, 2):
        if x % j == 0:
            return False
    return True

