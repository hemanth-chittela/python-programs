def updating_server_file(path,key,value):
    with open(path,"r") as file:
        result=file.readlines()
    with open(path,"w") as file:
        for line in result:
            if key in line:
                file.write(f"{key} = {value}\n")
            else:
                #file.write(line.rstrip()+" hello\n")
                file.write(line)
        

    with open(path,"r") as file:
        print(file.read())

updating_server_file("C:/Users/pc/Desktop/python/server.conf","PORT",9090)