count = 0
def tailRecursionGreet(count):

    if count == 4:
        return
    count += 1
    tailRecursionGreet(count)
    print(f"hello tail {count}")

def headRecursionGreet(count):

    if count == 4:
        return
    count += 1
    print(f"hello head {count}")
    headRecursionGreet(count)
    
tailRecursionGreet(0)
print("_"*50)
headRecursionGreet(0)