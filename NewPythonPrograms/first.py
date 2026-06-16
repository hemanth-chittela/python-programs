# entering the value of 2 
pao=2
print(pao)
name="cat"
print(name)
a,b,c=1,4,5
print(a)
a=['apple','van','zebra']
print(a[2])
c=('apple','van',"zebra")
print(c)

# list []
# tuple ()
# dict {}

a=2
b=5
if(a>b):
    print(a)
else:
    print(b)

terraform={"country":"india", "people":"100_million"}
print(terraform["country"], terraform["people"])

a=0
b=1
c=0
num=int(input("enter the range"))
print(0, end=" ")
for i in range(num-1):
    c=a+b
    print(c, end=" ")
    b=a
    a=c 