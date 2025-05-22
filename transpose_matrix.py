def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b= []
    for i in range(0, len(a[0])):
        temp = []
        for j in range(0,len(a)):
            # print(f"i: {i} j:{j}")
            temp.append(a[j][i])
        b.append(temp)
    return b