def pair(size):
    num = []
    for i in range(size):
        add_num = int(input(f"Ingrese el elemento {i+1}:\t"))
        num.append(add_num)
    for j in num:
        if j % 2 == 0:
            print(j)
    pass

size = int(input("Longitud de la lista:\t"))

pair(size)