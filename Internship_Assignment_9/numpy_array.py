import numpy as np

a1 = np.array([10, 20, 30])
a2 = np.array([[1,2,3], [4,5,6]])

# Combining 1D To 2D Numpy Arrays -->
def concatenate_array(a1, a2):
    reshape_a = np.reshape(a1, (1,-1))
    newaxis_a = a1[np.newaxis, :]

    global a3_bottom
    a3_bottom = np.concatenate((a2, reshape_a), axis=0)
    a3_top = np.concatenate((newaxis_a, a2), axis=0)

    new_a1 = a1[a1 != 30]
    new_a1re = np.reshape(new_a1, (-1,1))
    a3_columnf = np.concatenate((new_a1re, a2), axis=1)
    a3_columnl = np.concatenate((a2, new_a1re), axis=1)

    return print('Concatenate at the bottom [axis = 0] : \n', a3_bottom, '\n', '\n',
                 'Concatenate at the top [axis = 0] : \n', a3_top, '\n', '\n',
                 'Concatenate  at the first column [axis 1] : \n', a3_columnf, '\n', '\n',
                 'Concatenate  at the last column [axis 1] : \n', a3_columnl)

print(concatenate_array(a1, a2))

# Flatting the Numpy Array -->
def flatten_array(a2):
    flatten_a2_re = a2.reshape(-1)
    flatten_a2 = a2.flatten()
    flatten_a2_ravel = np.ravel(a2)

    return print('\nFlattening the array using reshape(-1) : \n', flatten_a2_re, '\n Base : \n', flatten_a2_re.base,  '\n', '\n',
                 'Flattening the array using flatten() : \n', flatten_a2, '\n Base : ', flatten_a2.base, '\n', '\n',
                 'Flattening the array using ravel() : \n', flatten_a2_ravel, '\n Base : \n', flatten_a2_ravel.base)
print(flatten_array(a2))

# Reversing Numpy Arrays Using Different Methods -->
def reverse_array(a3_bottom):
    re_ind_a3_row = a3_bottom[::-1, :]
    re_ind_a3_col = a3_bottom[:, ::-1]
    re_ind_a3_both = a3_bottom[::-1, ::-1]

    re_flip_a3_row = np.flip(a3_bottom, axis=0)
    re_flip_a3_col = np.flip(a3_bottom, axis=1)
    re_flip_a3_both = np.flip(a3_bottom, axis=(0, 1))

    return print('\nReversed 1D array [row]: \n', re_ind_a3_row, '\n', '\n',
                 'Reversed 1D array [col]: \n', re_ind_a3_col, '\n', '\n',
                 'Reversed 1D array [both axis] : \n', re_ind_a3_both, '\n', '\n',
                 'Flipped rows [flip()] : \n', re_flip_a3_row, '\n', '\n',
                 'Flipped columns [flip()] : \n', re_flip_a3_col, '\n', '\n',
                 'Flipped both [flip()] : \n', re_flip_a3_both)
print(reverse_array(a3_bottom))

# Various Common Operations On Numpy Arrays -->
def operations_numpy_array(arr):
    result = {}
    max_val = arr.max()
    result['max_val'] = max_val
    print(f'\nMaximum Value in the array : {max_val}')
    min_val = arr.min()
    result['min_val'] = min_val
    print(f'Minimum Value in the array : {min_val}')

    no_rows = None
    no_cols = None

    if arr.ndim >= 2:
        no_rows = arr.shape[0]
        no_cols = arr.shape[1]
    elif arr.ndim == 1:
        no_rows = arr.shape[0]
        no_cols = 1
    else:
        no_rows = 1
        no_cols = 1
    result["no_rows"] = no_rows
    result["no_cols"] = no_cols
    print(f"\nNumber of Rows : {no_rows}")
    print(f"Number of Columns : {no_cols}")

    print("\nIterating through each element -->")

    if arr.ndim == 1:
        print("\nArray is 1D :")
        for i in arr:
            print(i)
    elif arr.ndim == 2:
        print("\nArray is 2D (row by row iteration):")
        for rows in arr:
            for elements in rows:
                print(elements)
    elif arr.ndim == 0:
        print("\nArray is a scalar (0-D):")
        print(arr.item())
    else:
        print('\nArray in n-D (row-major)')
        for elements in np.nditer(arr, order='C'):
            print(elements)
        print('\nArray in n-D (column-major)')
        for elements in np.nditer(arr, order='F'):
            print(elements)

    print("\nSelecting a specific element -->")
    sp_ele = None
    if arr.ndim == 0:
        sp_ele = arr.item()
        print(f"\nArray is a scalar, value is: {sp_ele}")
        result["specific_element"] = sp_ele
    elif arr.ndim == 1:
        if arr.size > 0:
            sp_ele = arr[0]
            print(f"\nFor 1D Array, element at index 0: {sp_ele}")
            result["specific_element"] = sp_ele
        else:
            print("\n1D Array is empty")
            result["specific_element"] = None
    elif arr.ndim == 2:
        if arr.shape[0] > 0 and arr.shape[1] > 0:
            sp_ele = arr[0,1]
            print(f"\nFor 2D Array, element at (0, 1): {sp_ele}")
            result["specific_element"] = sp_ele
        else:
            print("\n2D Array is empty")
            result["specific_element"] = None
    elif arr.ndim == 3:
        if arr.shape[0] > 0 and arr.shape[1] > 0 and arr.shape[2]:
            sp_ele = arr[0,1,1]
            print(f"\nFor 3D Array, element at (0, 1, 1): {sp_ele}")
            result["specific_element"] = sp_ele
        else:
            print("\n3D Array is empty")
            result["specific_element"] = None
    else:
        print("\nError: Dimensions of this Array is > 3.")
        result["example_specific_element"] = None

    sum_ = None
    print("Sum of values (using for loop for 2D arrays):")
    if arr.ndim == 2:
        curr_sum = 0
        for row in arr:
            for element in row:
                curr_sum += element
        sum_ = curr_sum
        result["sum_2d_for_loop"] = sum_
        print(f"Sum of 2D array elements: {sum_}")
    else:
        print(f"Error: This array is {arr.ndim}-D.")
        result["sum_2d_for_loop"] = "N/A (not 2D)"

    print()
    return result

arr1 = np.array(42)
results_scalar = operations_numpy_array(arr1)

arr2 = np.array([5, 15, 2, 25, 8])
results_1d = operations_numpy_array(arr2)

arr3 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
results_2d = operations_numpy_array(arr3)
"""
arr4 = np.array([])
results_empty = operations_numpy_array(arr4)
"""
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
results_3d = operations_numpy_array(arr5)

print(operations_numpy_array(arr3))

# Arithmetic Operations On Numpy Arrays -->
def arithmetic_op_array(ar1, ar2):
    return {
        'add': ar1 + ar2,
        'sub': ar1 - ar2,
        'mul': ar1 * ar2,
        'div': ar1 / ar2
    }

ar_1 = np.array([10, 20, 30])
ar_2 = np.array([2, 5, 10])
print("\nArray A:", ar_1)
print("Array B:", ar_2)
result1 = arithmetic_op_array(ar_1, ar_2)
print("Results :")
for k, val in result1.items():
    print(f"{k}: {val}")

ar_3 = np.array([1, 2, 3])
ar_4 = np.array([[1, 2]])
print("\nArray C: ", ar_3)
print("Array D: ", ar_4)
try:
    result4 = arithmetic_op_array(ar_3, ar_4)
    print("\nResults (incompatible shapes):")
    for k, val in result4.items():
        print(f"{k}: {val}")
except ValueError as e:
    print(f"Error for incompatible shapes: {e}")