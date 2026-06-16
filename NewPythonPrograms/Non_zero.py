for i in range(1,20+1):
    to_string=str(i)
    if "0" not in to_string:
        convert_back=int(to_string)
        print(convert_back,end=" ")
