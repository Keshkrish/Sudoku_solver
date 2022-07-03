def make(vec):
    mat=[]
    for i in range(9):
        mat.append(vec[i*9:(i+1)*9])

    return mat

