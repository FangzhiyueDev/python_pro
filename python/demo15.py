# !/usr/bin/pyhton


def demo1():
    for i in range(1, 5):
        for j in range(1, 5):
            for z in range(1, 5):
                if (i != z) and (j != z) and (i != j):
                    print(i, j, z);


def demo2():

    pass



if __name__ == '__main__':
    demo1()

