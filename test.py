import math
from newtonsmethod import NewtonsMethod

print("In this program we will be attempting to match the accuracy of the square root of two from the math library "
      "using\n" 
      "Newton's method, which uses derivatives to approximate zeroes. We will be using the polynomial x^2 - 2 for this"
      " purpose.")

print(" ")
print(" ")

library_val = math.sqrt(2)

newtons_method_val = 2.25

init_x = 1.5

i = 1

nm = NewtonsMethod([1, 0, -2])

while True:

    xl = nm.eval_newton(init_x)

    if xl > library_val:
        init_x = xl
        i += 1

    else:
        print("Value from Python's math library: " + str(library_val))
        print(" ")
        print("Value obtained from Newton's method: " + str(xl))
        print(" ")
        print("error: " + str(library_val - xl))
        print(" ")
        print("Number of iterations of Newton's method: " + str(i))
        print(" ")
        break

print("Now that we have the same value as python's math library, let's try to one up it by getting a number more"
      " precise, simply by doing another iteration of the method")

print(" ")


x_one_up = nm.eval_newton(xl)

print("More precise Newton's method value of sqrt(2): " + str(x_one_up))

print(" ")

print("Python's value is off by: " + str(library_val - x_one_up))

print(" ")

if library_val - x_one_up == 0.0:
    print("Can't be more precise with just one iteration more!")

print(" ")

print("Let's try the new function, eval_ntimes, which allows the user to set the number of iterations of Newton's "
      "method needed from the get go")

print(" ")

print(nm.eval_ntimes(9, 1.5))

print(" ")

print("Let's try the set_coeff function")

nm.set_coeff([1, 0, -3])

print(nm.eval_ntimes(20, 2))

print(math.sqrt(3))

print(" ")

print("Lets try the to_string function that outputs the polynomial currently being used according to the coefficient "
      "vector:")

print(nm.to_string())

print("+++++++++++++leo+++++++")
obj = NewtonsMethod([1, 0, -2])

print(obj.eval_poly(2))
