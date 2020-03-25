def add_some(a, b):
    print (a+b)
    # 若不设置返回内容，则会自动返回一个None
    return 1
    
haha = {}
haha['_add'] = add_some# 这里传入的是一个地址
print (haha['_add'](10, 20))# 若上设函数中不添加一个return None，则还会多输出一个None