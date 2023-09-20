import numpy as np

# Создание двумерного массива
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Расчет суммы двух любых элементов второй строки массива
sum_of_elements = array[1, 0] + array[1, 2]
print("Сумма двух элементов второй строки массива:", sum_of_elements)

# Расчет произведения главной диагонали матрицы
diagonal_product = np.prod(np.diagonal(array))
print("Произведение главной диагонали матрицы:", diagonal_product)

