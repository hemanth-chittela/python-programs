string="successes"

list1=['a','e','i','o','u','A','E','I','O','U']
count=0
vowel=[]
for i in list1:
    for j in string:
        if i==j:
            count=count+1
            print(i,"count: ",count)
    count=0