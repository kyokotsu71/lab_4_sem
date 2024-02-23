def find_solution(n, a_n_m2=1, a_n_m1=1):
    if n == 0:
        return a_n_m2
    elif n == 1:
        return a_n_m1
    else:
        return find_solution(n - 1, a_n_m1, -3 * a_n_m1 + 10 * a_n_m2)


n = 100
solution = find_solution(n)
print(f"a({n}) = {solution}")

number = ((1 / 7) * ((-5) ** n)) + ((6 / 7) * (2 ** n))
print(f"a({n}) = {number}")
