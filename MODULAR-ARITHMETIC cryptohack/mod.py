# calculate the mode of two numbers and return the smallest
def mod(a, b):
    r = a%6
    c = b%17
    if r < c:
        return r
    return c
print(mod(11,8146798528947))


