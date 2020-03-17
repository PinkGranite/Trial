from sys import argv
# argv指参数变量（argument variable）
# sys可以成为一个模组（module），也可以称作库（libraries）

script, first, second, third = argv
# 这里可以称之为“解包”，将每一个参数赋予一个变量名（依次赋予）
# 事实上应该是 sys.argv这是一个列表，用于存储输入的参数
# 注意，argv的第一个参数一定是script，即文件名作为 sys.argv[1]

print ("The script is called:", script)
# script就是脚本的意思（.py文件）
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)