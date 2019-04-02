# !/usr/bin/python
# coding=utf-8


def stringTest(str, *str1, **dictq):
    """

    :param str:
    :param str1:
    :param dictq:
    :return:
    """
    print("参数一的值：", str)
    for i in str1:
        print("元祖的信息", str1)
        pass
    for key, value in dictq.items():
        print("字典的信息", key, value)


if __name__ == '__main__':
    stringTest("asfasfasgfg",
               str1=("sfa", 2543, "sgsdgds", {353, "sfasg", "sdgs", 464, "af"}), dictq={
            "name": "fang", "password": 124343, "age": 22
        })


class MyView(object):
    """
    可以迭代的对象
    """

    def __iter__(self):  # 可迭代对象
        pass

    def __getitem__(self, item):  # 可迭代对象
        return item

    def __next__(self):  # 迭代器对象
        pass


