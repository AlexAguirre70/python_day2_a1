def arb_args(*args):
    for i in args:
        print(i)
arb_args('Alex','Adrian','Travis',1)

def inner_func(a,b):
    def inner_add():
        return a+b
    def inner_sub():
        return a-b
    print(inner_add()+inner_sub())


inner_func(5,12)

def lunch_lady(name,lunch="Mystery Meat"):
    print(name + ' is eating ' +lunch)
lunch_lady ('Alex','Spam')

def sum_n_product (a,b):
    value1 = a+b
    value2 =a*b
    print(value1, value2)

sum_n_product(5,2)

from statistics import mean
def arb_mean(*args):
    print (mean(args))

arb_mean( 1,5,7,8)

def arb_longest_string(*args):
    return max(args,key=len)
print(arb_longest_string("aaa","bbbbb","cccccccccc"))