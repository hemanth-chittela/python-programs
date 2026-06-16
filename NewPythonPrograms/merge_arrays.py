#example of merge arrays
def merge(array1, array2):
    array1=[1,2,3]
    array2=[4,5,6]
    sum=sorted(set(array1+array2))
    print(sum)
merge(3,4)
