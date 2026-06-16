def palindrome(x):
    x=str(x)
    s=x[::-1]
    if s==x:
        return True
    else:
        return False
palindrome(121)
