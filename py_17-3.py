Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
df=
df=pd.read_csv("C:/Users/G SHIVAPRAKASH/OneDrive/Attachments/Documents/Book5.csv")
df
   COURSE  MARKS
0     IVC     18
1  PYTHON     19
2      OS     20
df.shape
(3, 2)
len(df)
3
df.head(2)
   COURSE  MARKS
0     IVC     18
1  PYTHON     19
#ACCESSING FILES IN A FOLDER
import os
print(os.listdir("C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python"))
['accessing_files_in_a_folder.py', 'age.py', 'basic_try_except.py', 'Book1.csv', 'Book1.csv.xlsx', 'Book2.csv', 'Book3.csv', 'Book4.csv', 'catching_exception_object.py', 'count_num.py', 'csv.py', 'csv2.py', 'fac.py', 'fac2.py', 'factorial.py', 'fib.py', 'fibo.py', 'fibo2.py', 'file1.txt', 'file2.txt', 'handling_multiple_exceptions_in_one_line.py', 'handling_specific_exception.py', 'largest.py', 'list.py', 'max_min.py', 'multiple_except_blocks.py', 'p1.py', 'p12-3.py', 'p1_05.py', 'p2.py', 'p2_05.py', 'p3_10.py', 'p3_5.py', 'p4_17.py', 'p5_19.py', 'py_10-3.py', 'py_17-3.py', 'Raising_an_exception.py', 'rectangle.py', 'reshape.py', 'set.py', 'si.py', 'simple_calculator.py', 'statistics.py', 'sum.py', 'temperature_converter.py', 'try_except_with_file_handling.py', 'tuple.py', 'user_defined_exception.py', 'using_else_block.py', 'using_finally_block.py']
os.rename("file1.txt","newfile.txt")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.rename("file1.txt","newfile.txt")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'file1.txt' -> 'newfile.txt'
os.rename("p1.txt","file1.txt")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    os.rename("p1.txt","file1.txt")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'p1.txt' -> 'file1.txt'
os.rename("C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/p1.txt","file1.txt")
import os
import shutil
shutil.copy("file1.txt","C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/file2.txt")
'C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/file2.txt'
shutil.move("file1.txt","C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/file2.txt")
'C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/file2.txt'
import numpy as np
array_1d=np.array([1,2,3,4,5])

================================================= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/Creating_a_1D_numpy_array.py ================================================
1D array:
[1 2 3 4 5]
print("1D Array:\n",array_1d)
1D Array:
 [1 2 3 4 5]
arr_2d=array_1d_reshape(2,3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    arr_2d=array_1d_reshape(2,3)
NameError: name 'array_1d_reshape' is not defined
arr_2d=array_1d.reshape(2,3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    arr_2d=array_1d.reshape(2,3)
ValueError: cannot reshape array of size 5 into shape (2,3)
arr_2d=array_1d.reshape(2,2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    arr_2d=array_1d.reshape(2,2)
ValueError: cannot reshape array of size 5 into shape (2,2)
array_1d=np.array([1,2,3,4,5,6])
arr_2d=array_1d.reshape(2,3)
print("\n Reshaped to 2D Array(2x3):\n",array_2d)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("\n Reshaped to 2D Array(2x3):\n",array_2d)
NameError: name 'array_2d' is not defined. Did you mean: 'array_1d'?
print("\n Reshaped to 2D Array(2x3):\n",arr_2d)

 Reshaped to 2D Array(2x3):
 [[1 2 3]
 [4 5 6]]
print("\n Element at position(1,2):",array_2d[1,2])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("\n Element at position(1,2):",array_2d[1,2])
NameError: name 'array_2d' is not defined. Did you mean: 'array_1d'?
print("\n Element at position(1,2):",arr_2d[1,2])

 Element at position(1,2): 6
>>> arr_2d[0,1]=10
>>> print("\n modofied array(After changing element at position (0,1) to 10:\n",arr_2d)

 modofied array(After changing element at position (0,1) to 10:
 [[ 1 10  3]
 [ 4  5  6]]
>>> arr_sum=np.sum(arr_2d)
...                 
>>> print("\n sum of all elements in the array:\n",arr_sum)
...                 

 sum of all elements in the array:
 29
>>> matrix_A=np.array([[1,2],[3,4]])
...                 
>>> matrix_b=np.array([[7,8],[5,6]])
...                 
>>> matrix_sum=np.add(matrix_A,matrix_b)
...                 
>>> print("Matrix Addition(A+b):\n",matrix_sum)
...                 
Matrix Addition(A+b):
 [[ 8 10]
 [ 8 10]]
>>> matrix_product_elementwise=np.multiply(matrix_A,matrix_b)
...                 
>>> print("matrix multiplication(A*B):\n",matrix_product_elementwise)
...                 
matrix multiplication(A*B):
 [[ 7 16]
 [15 24]]
>>> matrix_dot_product=np.dot(matrix_A,matrix_b)
...                 
>>> print("matrix dot product(A.b):\n",matrix_dot_product)
...                 
matrix dot product(A.b):
 [[17 20]
 [41 48]]
>>> matrix_transpose=np.transpose(matrix_A)
...                 
>>> print("transpose of Matrix A:\n",matrix_transpose)
...                 
transpose of Matrix A:
 [[1 3]
 [2 4]]
