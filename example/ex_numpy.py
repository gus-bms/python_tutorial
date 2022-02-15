import numpy as np

# m = np.array([[ 0,  1,  2,  3,  4],
#             [ 5,  6,  7,  8,  9],
#             [10, 11, 12, 13, 14]])
# #2-1
# print(m[1,2])
# #2-2
# print(m[-1,-1])
# #2-3
# print(m[1,1:3])
# #2-4
# print(m[1:3, 2:3])
# #2-5
# print(m[:2, 3:])

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#
# #3-1
# print(x[x % 3 == 0])
# #3-2
# print(x[x % 4 == 1])
# #3-3
# a = x % 4 == 1
# b = x % 3 == 0
# print(x[a&b])

# A = np.array([[1, 2, 3], [4, 5, 6]])
# print(A.T)

a = np.array((1,2,3,4,5,6,7,8,9,0))
print(a.reshape(-1,1,1))

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])
print(np.sort(a))

print(a)