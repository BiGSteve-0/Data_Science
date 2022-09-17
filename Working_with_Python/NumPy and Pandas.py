import numpy as np

# brackets are used for indexing 
# array method used

a = np.array([1,2,3,4])
print("a:\n", a)

# curly braces used for string interpolation 
print(F"a: \n first array {a[2]}")

#numpy has property "shape" will show the array dimension
#even using the same variable and redeclaring the dimensions are easy
#and even reshaped...omg
a = np.array([[1,2],[3,6]])
print(a.shape)
print(a.reshape((4)))

#declare an array on "n" size, I imagine this could be good for sql: rank() function too
np.arrange(10)
np.arrange(10).reshape((5,2)) #wild

#fill array with zeros
np.zeros((2,5))

