# number=input('Enter a number to find its factorial:')
# if number.isdigit():
#     number=int(number)
#     if number>=0:
#         factorial=1
#         for i in range(1,number+1):
#             factorial*=i                                   # factorial=factorial*i
#         print(f'The factorial of {number} is {factorial}')
#     else:
#         print('Factorial is not defined for negative numbers')
# else:
#     print('Please enter a valid non-negative integer')

"""
Factorial Calculator | 阶乘计算器 | 階乗計算機
Author: AAAsparrow
Description:
    English: A simple program to calculate the factorial of a non-negative integer.
    中文: 一个简单的程序，用于计算非负整数的阶乘。
    日本語: 非負整数の階乗を計算する簡単なプログラム。
"""
def factorial(n):
    if n <0:
        raise ValueError("Factorial is not defined for negative numbers")
    result=1
    for i in range(1,n+1):
        result*=i
    return result
def main():
    print('Welcome to the Factorial Calculator! | 欢迎使用阶乘计算器！| 階乗計算機へようこそ！')
    number=input('Enter a non-negative integer | 输入非负整数 | 非負整数を入力してください:')
    if number.isdigit():
        number=int(number)
        if number>=0:
            print(f'The factorial of {number} is {factorial(number)} | {number}的阶乘是{factorial(number)} | {number}の階乗は{factorial(number)}です')
        else:
            print('Factorial is not defined for negative numbers | 阶乘未定义负数 | 階乗は負の数には定義されていません')
    else:
        print('Please enter a valid non-negative integer | 请输入有效的非负整数 | 有効な非負整数を入力してください')
if __name__=='__main__':
    main()

