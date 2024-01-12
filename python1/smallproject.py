import sys
import time
type=sys.argv[1]

if type=="t2.micro":
    list=[]
    print("creating 3 t2.micros")
    for i in range(3):
        time.sleep(2)
        print("creating...")
        time.sleep(2)
        print("looking for dependencies...")
        time.sleep(2)
        print("verifying the dependencies...")
        time.sleep(2)
        print("almost done...")
        time.sleep(2)
        print("completed !")
        x=time.localtime()
        y=time.asctime(x)
        print("instance created at:",y)
        list.append(y)
    print(list)
elif type=="t2.medium":
    print("it will cost you 4$ a day")
elif type=="t2.xlarge":
    print("it will charge you 8$ a day")
else:
    print("please enter a valid instance type")
