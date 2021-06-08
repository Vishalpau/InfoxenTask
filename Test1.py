Ex = [1,[2,3,[4,5,6],[7,[8,9,[10,11],[12]]]]]
n = len(Ex)
X = []

def flatten(input_list, output_list=[]):
    for i in input_list:
        if isinstance(i, list):
            flatten(i, output_list)
        else:
            output_list.append(i)
    return output_list

input_list = [1,[2,3,[4,5,6],[7,[8,9,[10,11],[12]]]]]

print(flatten(input_list))

'''
for i in range(n):
    if type(Ex[i]) is list:
        if len(Ex[i])>1:
            for j in range(len(Ex[i])):
                if type(Ex[i][j]) is list:
                    if len(Ex[i][j])>1:
                        for h in range(len(Ex[i][j])):
                            if type(Ex[i][j][h]) is list:
                                if len(Ex[i][j][h])>1:
                                    for hp in range(len(Ex[i][j][h])):
                                        if type(Ex[i][j][h][hp]) is list:
                                            if len(Ex[i][j][h][hp])>1:
                                                for Q in range(len(Ex[i][j][h][hp])):
                                                    if type(Ex[i][j][h][hp][Q]) is int:
                                                        X.append(Ex[i][j][h][hp][Q])
                                        else:
                                            X.append(Ex[i][j][h][hp])
                            else:
                                X.append(Ex[i][j][h])
                else:
                    X.append(Ex[i][j])
    else:
        X.append(Ex[i])
'''
# print(X)