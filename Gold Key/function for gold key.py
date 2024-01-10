def find_best_element(array : list):
    matrix = array
    num_columns = max(len(row) for row in matrix)  # Максимально длинная строка которая есть в матрице
    column_sums = [0] * num_columns  # Начальная сумма
    for j in range(num_columns):  # Итерация по столбцам
        for i in range(len(matrix)):  # Итерация по строкам
            if j < len(matrix[i]):
                column_sums[j] += matrix[i][j]
    row_sum = [0] * num_columns  # Начальная сумма для строк
    for index, x in enumerate(matrix):
        row_sum[index] = sum(x)
    diagonal_sum = [0] * num_columns
    start_cut = -1
    for y in range(num_columns):  # Итерация по столбцам
        for item, element in enumerate(matrix):  # Итерация по диагонали
            if y < len(element):
                diagonal_sum[y] += element[start_cut]
        start_cut -= 1
    max_element_in_column_sums = max(column_sums)
    max_element_in_row_sum = max(row_sum)
    max_element_in_diagonal_sum = max(diagonal_sum)

    if max_element_in_column_sums > max_element_in_row_sum and max_element_in_column_sums > max_element_in_diagonal_sum:
        max_el = max_element_in_column_sums
    elif max_element_in_row_sum > max_element_in_diagonal_sum:
        max_el = max_element_in_row_sum
    else:
        max_el = max_element_in_diagonal_sum
        return max_el
