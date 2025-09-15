// worksheet 4:-



// import numpy as np

// # Q1
// arr1 = np.arange(5, 26)
// print("Q1:", arr1)

// arr2 = np.random.randint(10, 51, size=(3, 4))
// print("Q1:\n", arr2)



// # Q2
// print("\nQ2 - arr1:")
// print("Shape:", arr1.shape)
// print("Size:", arr1.size)
// print("Data type:", arr1.dtype)




// print("\nQ2 - arr2:")
// print("Shape:", arr2.shape)
// print("Size:", arr2.size)
// print("Data type:", arr2.dtype)



// # Q3
// array1 = np.array([2, 4, 6, 8, 10])
// array2 = np.array([1, 3, 5, 7, 9])
// print("\nQ3 Addition:", array1 + array2)
// print("Q3 Subtraction:", array1 - array2)
// print("Q3 Multiplication:", array1 * array2)
// print("Q3 Division:", array1 / array2)




// # Q4
// arr3 = np.arange(1, 10).reshape(3, 3)
// print("\nQ4:\n", arr3)
// print("Q4 Multiplied by 5:\n", arr3 * 5)




// # Q5
// arr4 = np.arange(10, 26).reshape(4, 4)
// print("\nQ5 Array:\n", arr4)
// print("Q5 Second row:", arr4[1, :])
// print("Q5 Last column:", arr4[:, -1])
// arr4[0, :] = 0
// print("Q5 First row replaced with zeros:\n", arr4)





// # Q6
// arr5 = np.random.randint(20, 41, size=10)
// print("\nQ6 Array:", arr5)
// print("Q6 Elements > 30:", arr5[arr5 > 30])



// # Q7
// arr6 = np.arange(11, 23)
// reshaped_arr6 = arr6.reshape(3, 4)
// print("\nQ7 Array:", arr6)
// print("Q7 Reshaped (3x4):\n", reshaped_arr6)



// # Q8
// A = np.array([[1, 2], [3, 4]])
// B = np.array([[5, 6], [7, 8]])
// print("\nQ8 Matrix Multiplication:\n", np.dot(A, B))
// print("Q8 Transpose of A:\n", A.T)



// # Q9
// arr7 = np.random.randint(10, 61, size=15)
// print("\nQ9 Array:", arr7)
// print("Q9 Mean:", np.mean(arr7))
// print("Q9 Median:", np.median(arr7))
// print("Q9 Standard Deviation:", np.std(arr7))



// # Q10
// A = np.array([[2, 1, 3],
//               [0, 5, 6],
//               [7, 8, 9]])
// det_A = np.linalg.det(A)
// inv_A = np.linalg.inv(A)
// eigvals, eigvecs = np.linalg.eig(A)
// print("\nQ10 Determinant:", det_A)
// print("Q10 Inverse:\n", inv_A)
// print("Q10 Eigenvalues:", eigvals)
// print("Q10 Eigenvectors:\n", eigvecs)




// # Q11
// positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
// dist_first_last = np.linalg.norm(positions[-1] - positions[0])
// print("\nQ11 Distance first to last:", dist_first_last)
// step_diffs = np.diff(positions, axis=0)
// step_distances = np.linalg.norm(step_diffs, axis=1)
// total_distance = np.sum(step_distances)
// print("Q11 Total distance traveled:", total_distance)
