reading_file=open("sampleData.txt",'r')
for i in range(0,3):
    result=reading_file.read()
    print(result)
    again=reading_file.seek(0)