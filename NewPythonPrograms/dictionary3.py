dicto={'name':'Harry','Age':11,'House':'Gryffindor'}
dicto['Food']='Vegetables'
dicto['name']='Potter'
print(dicto)
print(dicto.pop('House'))
print(dicto)

for i,j in dicto.items():
    print(i,j)