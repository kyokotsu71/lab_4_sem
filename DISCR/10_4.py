def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(k, p):
    g, x, y = extended_gcd(k, p)
    return x % p
'''
 сначала находит обратный элемент к 15 по модулю 109, 
 а затем умножает его на 6 и берет остаток от деления на 109, 
 чтобы получить решение уравнения
'''
k = 15
p = 109
b = 6

k_inv = mod_inverse(k, p)
x = (k_inv * b) % p
print(f"Решение: x = {x}")
