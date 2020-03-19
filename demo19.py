# 整篇文档中只有函数，可以在其他文件中通过import调动这个文件，调用时无需加.py，直接输入文件名即可
# 调用后即可使用本文档的方法，使用的方法为：demo19.(方法名）(参数）

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    # .split是对字符串用的方法，意在以'?'的字符对字符串进行分割
    return words
    
def sort_words(words):
    """Sorts the words."""
    # sorted()方法是对字符数组内的元素进行排序，由a-z
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    # .pop()方法将字符串数组中的元素弹出，0表示1号元素，-1表示最后一个元素。返回弹出的字符
    print (word)
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print (word)
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)