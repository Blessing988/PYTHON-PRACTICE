def outer_func(msg):

    def inner_func():
        print(msg)
    return inner_func()

outer_1 = outer_func('good')
outer_2 = outer_func('bad')

print(outer_1)
print(outer_2)