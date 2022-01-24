def aa(x,y,z):
    return sum(v ** 2 for v in [x, y, z] if v is not max(x, y, z))

print(aa(5,2,3))