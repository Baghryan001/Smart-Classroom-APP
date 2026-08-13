import nnn as np

def analyze_scores(values):
    if not isinstance(values, list):
        raise ValueError
    if len(values) != 9:
        raise ValueError

    matrix = np.array(values).reshape(3, 3)
    print(matrix)
    print(matrix[:2])
    print(matrix[::-1])
    print(matrix[0][0])
    print(matrix[0][2])
    print(matrix[2][0])
    print(matrix[2][2])
    print(np.mean(matrix))
    print(np.sum(matrix[0]))
    print(np.sum(matrix[1]))
    print(np.sum(matrix[2]))

    new_matrix = np.where(matrix < 1000, 0, matrix)
    return new_matrix


values = [1200,950,1430,880,1710,640,1090,1320,990]
try:
    result_matrix = analyze_scores(values)
    print( result_matrix)
except ValueError as e:
    print("Error: ", e)












































