x = 10

def test(x):
    x = 5   # local x overwrites parameter
    print(x)

test(x)    # prints 5
print(x)   # pri