numbers=[1,2,3,4,5]


def square(x):
    return x*x

sq=list(map(square,numbers))
print(sq)

square=list(map(lambda x:x**2,numbers))
print(square)