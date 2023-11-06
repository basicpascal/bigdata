A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

result_dict = {}

for i in range(len(A)):
    key = B[i]
    value = A[i]

    if key in result_dict:
        result_dict[key] += value
    else:
        result_dict[key] = value

print(result_dict)
