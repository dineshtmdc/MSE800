# Week 02 Activities (NumPy)

This folder contains NumPy activities focusing on 1D and 2D array manipulations.

## Activity 01 (`Activity01`)

This script demonstrates basic 1D array operations:
1.  Creates a NumPy array of the first 10 positive integers using `np.array()`.
2.  Prints the array.
3.  Prints the shape (`.shape`) and data type (`.dtype`) of the array.
4.  Multiplies each element by 2 using vectorized multiplication and prints the result.


*   **`numpy.array()`**: Creating a NumPy array from a Python list.
*   **`ndarray` Object**: NumPy's core 1D array structure.
*   **`.shape` Attribute**: Getting the dimensions of the array.
*   **`.dtype` Attribute**: Identifying the data type of array elements.
*   **Vectorized Operations**: Performing element-wise operations efficiently without explicit loops.

## Activity 02 (`Activity02`)

This script demonstrates basic 2D array operations using a student scores dataset:
1.  Creates a 2D NumPy array representing scores for multiple students across multiple subjects.
2.  Calculates the average score for each student using `np.mean(axis=1)`.
3.  Calculates the average score for each subject using `np.mean(axis=0)`.
4.  Identifies the student with the highest total score using `np.sum(axis=1)` and `np.argmax()`.


*   **2D `ndarray`**: Representing data.
*   **`np.mean(axis=...)`**: Calculating the mean along a specified axis (rows or columns). `axis=1` operates across columns (per student), `axis=0` operates down rows (per subject).
*   **`np.sum(axis=1)`**: Calculating the sum along rows (total score per student).
*   **`np.argmax()`**: Finding the index of the maximum value in an array.
*   **Array Indexing**: Accessing specific elements or rows/columns.
