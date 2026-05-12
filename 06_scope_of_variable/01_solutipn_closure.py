def chaicode(num):
    def actual(x):
        return x**num
    return actual
f = chaicode(5)
g = chaicode(4)

print(g)
print(f)

print(f(3))
print(g(3))