def functions(numbers):
    new_list=[]
    for i in range(numbers):
        inputs=int(input(f"Enter the number {i+1}: "))
        new_list.append(inputs)
    print(new_list)
functions(5)
