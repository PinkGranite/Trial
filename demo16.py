
from sys import argv

script, input_file = argv

def print_all(f):
    # 输出文本内容
    print (f.read())
    
def rewind(f):
    # 重新回到文本开头
    f.seek(0)
    # seek用来找到对应位置
    
def print_a_line(line_count, f):
    # 打印一行文本
    print (line_count, f.readline())
    
current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines")

current_line = 1
print_a_line(current_line, current_file),
# 这里在print语句后面加一个,可以使print语句不自动输出一个\n
# 不同类型的数据同时输出时，要用,分格，而不能用+号。

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)