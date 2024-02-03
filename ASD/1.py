def jarvis(A):
    def rotate(p, q, r):
        """
        Функция для определения ориентации трех точек
        Возвращает: отрицательное значение, если r находится справа от вектора pq,
                    положительное значение, если r находится слева от вектора pq,
                    нулевое значение, если точки коллинеарны
        """
        return (q[0] - p[0]) * (r[1] - q[1]) - (r[0] - q[0]) * (q[1] - p[1])

    n = len(A)
    P = list(range(n))

    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:
            P[i], P[0] = P[0], P[i]
    H = [P[0]]
    del P[0]
    P.append(H[0])
    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(A[H[-1]], A[P[right]], A[P[i]]) < 0:
                right = i
        if P[right] == H[0]:
            break
        else:
            H.append(P[right])
            del P[right]
    return H


A = [(0, 0), (1, 1), (2, 0), (2, -2), (0, -1), (1, -1), (1.5, -1.5)]
print(jarvis(A))
