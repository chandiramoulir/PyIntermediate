### Intermediate python sample programs

### *vars & **Kwargs ### -- working
# arg_x1 = ''
# other_args = []
# def func_vars(arg_1, *rest_args):
#     arg_x1 = arg_1
#     other_args = rest_args
#     print("Demo of *vars")
#     print("1st argument: ", arg_x1)
#     print("Other arguments in *vars: ", other_args)
#
# func_vars("1st arg", 1, 2, 3, "End of args")

### **KWARGS-KeyWord args -- working
#
# def func_kwargs(**star):
#     if star is not None:
#         for i,j in star.items():
#             print("%s = " "%s" %(i, j))
#
# func_kwargs(arg1="Mouli", arg2=2, arg3="It works!")


#### Generators ####

# def gen_func():
#     for i in range(0,10):
#         yield(i)
#
# Gen = gen_func()
# print(next(Gen))
# print(next(Gen))
# print(next(Gen))

### Fibonacci series using generators

# def fibonacci_gen(n):
#     a=b=1
#     for i in range(n):
#         yield a
#         a, b = b, a+b
#
# for x in fibonacci_gen(50):
#     print(x)


#### MAP - LAMDA - FILTER - REDUCE ####
# import functools
##def funct(x):
##    return x**2
#
# listx = [1,20,3,40,5]
# #listy = [1,20,3,40,5]
# fx_map = map(lambda x : x**2, listx )
# fx_reduce = functools.reduce(lambda x,y : x*y, listx )
# print(*fx_map)
# print(fx_reduce)

#
# for i in listx:
#     if fx(i):
#         print(fx(i))


