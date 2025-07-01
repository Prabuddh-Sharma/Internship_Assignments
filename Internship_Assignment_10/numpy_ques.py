import numpy as np

def numpy_array():

    arr1 = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
    print("Original Array:")
    print(arr1)

    def replace_nan_with_zero(arr):
        return np.nan_to_num(arr, nan=0.0)

    arr1_without_nan = replace_nan_with_zero(arr1.copy())
    print("\nArray after replacing NaN with 0:")
    print(arr1_without_nan)

    arr2 = arr1_without_nan.copy()

    arr2[[0, 1]] = arr2[[1, 0]]
    print("\nArray after directly interchanging Row 0 and Row 1:")
    print(arr2)

    arr2[:, [0, 2]] = arr2[:, [2, 0]]
    print("\nArray after directly interchanging Column 0 and Column 2:")
    print(arr2)

    print("\nMove axes of 3D array")
    arr_3d = np.arange(24).reshape((2, 3, 4))
    print("Original 3D Array (shape: {}):".format(arr_3d.shape))
    print(arr_3d)

    moved_axes_arr = np.transpose(arr_3d, axes=(1, 2, 0))
    print("\n3D Array after moving axes from (0,1,2) to (1,2,0) (new shape: {}):".format(moved_axes_arr.shape))
    print(moved_axes_arr)

    print("\nReplace NaN values with average of columns")
    arr3 = np.array([
        [1, 2, np.nan, 4],
        [5, np.nan, 7, 8],
        [9, 10, 11, np.nan],
        [np.nan, 14, 15, 16]
    ], dtype=float)
    print("Original Array with NaNs (for column average replacement):")
    print(arr3)

    column_averages = np.nanmean(arr3, axis=0)
    print("\nColumn Averages (ignoring NaNs):")
    print(column_averages)

    for col_ in range(arr3.shape[1]):
        nan_in_column = np.isnan(arr3[:, col_])
        arr3[nan_in_column, col_] = column_averages[col_]

    print("\nArray after replacing NaNs with column averages:")
    print(arr3)

    print("\nReplace negative values with zero")
    arr4 = np.array([
        [1, -5, 10, -20],
        [3, 0, -7, 15],
        [-2, 12, 6, -1]
    ], dtype=int)
    print("Original Array with negative values:")
    print(arr4)

    arr4[arr4 < 0] = 0
    print("\nArray after replacing negative values with 0:")
    print(arr4)

    print("\nMean, Median, Mode of 2D Arrays")

    arr_2d_a = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    arr_2d_b = np.array([
        [10, 20, 30, 40],
        [10, 50, 60, 70],
        [80, 90, 10, 100]
    ])

    print("First 2D Array (arr_2d_a):")
    print(arr_2d_a)
    print("\nSecond 2D Array (arr_2d_b):")
    print(arr_2d_b)

    mean_a = np.mean(arr_2d_a)
    mean_b = np.mean(arr_2d_b)
    print(f"\nMean of arr_2d_a: {mean_a:.2f}")
    print(f"Mean of arr_2d_b: {mean_b:.2f}")

    median_a = np.median(arr_2d_a)
    median_b = np.median(arr_2d_b)
    print(f"\nMedian of arr_2d_a: {median_a:.2f}")
    print(f"Median of arr_2d_b: {median_b:.2f}")

    def get_mode(arr):
        flat_arr = arr.flatten()
        unique_elements, counts = np.unique(flat_arr, return_counts=True)
        max_count = np.max(counts)
        modes = unique_elements[counts == max_count]
        return modes, max_count

    modes_a, count_a = get_mode(arr_2d_a)
    print(f"\nMode of arr_2d_a: {modes_a} (occurred {count_a} times)")

    modes_b, count_b = get_mode(arr_2d_b)
    print(f"Mode of arr_2d_b: {modes_b} (occurred {count_b} times)")

    print("\nSolving Linear Equations (linalg and Inverse Method)")

    # Define the coefficient matrix (A) from the equations:
    # x - 2y + 3z = 9
    # -x + 3y - z = -6
    # 2x - 5y + 5z = 17
    A = np.array([
        [1, -2, 3],
        [-1, 3, -1],
        [2, -5, 5]
    ])
    print("Coefficient Matrix (A):")
    print(A)

    # Define the constants matrix (B).
    B = np.array([9, -6, 17])
    print("\nConstants Matrix (B):")
    print(B)

    solution_linalg = np.linalg.solve(A, B)
    print("\nSolution using np.linalg.solve():")
    print(f"x = {solution_linalg[0]:.2f}")
    print(f"y = {solution_linalg[1]:.2f}")
    print(f"z = {solution_linalg[2]:.2f}")

    # Calculate the inverse of matrix A.
    A_inverse = np.linalg.inv(A)
    print("\nInverse of Matrix A:")
    print(A_inverse)

    solution_inverse = np.dot(A_inverse, B)
    print("\nSolution using Inverse Matrix Method:")
    print(f"x = {solution_inverse[0]:.2f}")
    print(f"y = {solution_inverse[1]:.2f}")
    print(f"z = {solution_inverse[2]:.2f}")

numpy_array()