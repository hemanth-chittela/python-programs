# this palindrom works for negative integers and as well postive

def Pal(Number):
    if Number>=0:
        y=str(Number)
        y=y[::-1]
        y=int(y)
        if Number==y:
            return True
        else:
            return False
    else:
        return False

print(Pal(0))