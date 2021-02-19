# @Time : 2021/1/27 15:48
# @Author : DengZh
# @File : Demo.py
# @Software: PyCharm

# import sklearn as sk
# print(sk.__version__)
from random import randint


def play():
    random_int = randint(1, 10)
    while True:
        # print("111")
        user_gress = int(input("a number:"))
        if user_gress == random_int:
            print("yes")
            break
        if user_gress < random_int:
            print("bigger")
            continue
        if user_gress > random_int:
            print("smaller")
            continue
    print("game is over")


if __name__ == '__main__':
    play()
