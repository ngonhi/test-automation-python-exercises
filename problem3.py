a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}

x = [0, 0, 0, 0, 1, 1, 1, 1, 1]
y = (0, 1, 0, 1)
z = {0, 1}

m = [0, 0, 0]
n = (1, 1, 1)
o = {0, 1}


def contain_same_nums(a, b, c):
    a = set(a) # Remove duplicates in a
    b = set(b) # Remove duplicated in b
    print(a == b and b == c)


contain_same_nums(a, b, c)
contain_same_nums(x, y, z)
contain_same_nums(m, n, o)
