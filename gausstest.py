from gauss_newton import GaussNewton
import numpy

g = GaussNewton([[0, 7],[1, 15],[2, 43],[3, 107],[4, 233],[5, 439],[6, 733],[7, 1160],[8, 1686],[9, 2370],[10, 3220]])
final_list = [3, 2, 1, 5]

for i in range(0,10):
    final_list = g.Gauss_Newton(final_list)
    print(final_list)

print(final_list)





# , [5, 94], [6, 121], [7, 163], [8, 194], [9, 245], [10, 290]