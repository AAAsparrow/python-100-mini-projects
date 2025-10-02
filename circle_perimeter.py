"""
Calculate the perimeter of a circle given its radius.
auther:AAAsparrow
Description:
    English: A simple program to calculate the perimeter of a circle given its radius.
    中文: 一个简单的程序，用于计算给定半径的圆的周长。
    日本語: 半径が与えられた円の周囲長を計算する簡単なプログラム。
"""
# num=input('please enter the radius of the circus:')
# if num.replace('.','',1).isdigit() and num.count('.')<2:
#     num=float(num)
#     if num>=0:
#         perimeter=3.14*2*num
#         print(f'The perimeter of the circle with radius{num}is {perimeter}')
#     else:
#         print('The radius cannot be negative')
#         exit()
# else:
#     print('please enter a valid number')
#     exit()

def perimeter_of_circle(radius):
    if radius<0:
        raise ValueError("Perimeter is not defined for negative numbers")
    return 3.14*2*radius
# perimeter = perimeter_of_circle(2)    # Example usage_1
# print(perimeter)

# def main():   # Example usage_2
#     print('welcome to the Circle Perimeter Calculator! | 欢迎使用圆周长计算器！| 円周長計算機へようこそ！')
#     radius=input('Enter the radius of the circle | 输入圆的半径 | 円の半径を入力してください:')
#     if radius.repalce('.','',1).isdigit() and radius.count<2:
#         radius=float(radius)
#         if radius>=0:
#             print(f'The perimeter of the circle with radius {radius} is {perimeter_of_circle(radius)} | 半径为{radius}的圆的周长是{perimeter_of_circle(radius)} | 半径{radius}の円の周囲長は{perimeter_of_circle(radius)}です')
#         else:
#             print('The radius cannot be negative | 半径不能为负数 | 半径は負の数にはなりません')
#     else:
#         print('Please enter a valid number | 请输入有效的数字 | 有効な数字を入力してください')
# if __name__=='__main__':
#     main()


