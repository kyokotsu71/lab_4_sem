def can_transform(str1, str2):
    if len(str1) != len(str2):
        return False

    arr1 = list(str1)
    arr2 = list(str2)

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            j = i + 1
            while j < len(arr1) and arr1[j] != arr2[i]:
                j += 1

            if j == len(arr1):
                return False

            arr1[i], arr1[j] = arr1[j], arr1[i]

    return arr1 == arr2


def count_permutations(str1, str2):
    if not can_transform(str1, str2):
        return "Преобразование невозможно"

    arr1 = list(str1)
    arr2 = list(str2)

    count = 0
    i = 0
    while i < len(arr1):
        if arr1[i] != arr2[i]:
            j = i + 1
            while j < len(arr1) and arr1[j] != arr2[i]:
                j += 1

            arr1[i], arr1[j] = arr1[j], arr1[i]
            count += 1

        i += 1

    return count


str1 = "123321"
str2 = "321123"

print(count_permutations(str1, str2))
