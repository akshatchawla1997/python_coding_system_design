def powerOf4(n:int)->bool:
    if n < 0:
        return False
    if n == 1:
        return True
    if n%4 != 0: 
        return False
    return powerOf4(n // 4)

print(powerOf4(4))