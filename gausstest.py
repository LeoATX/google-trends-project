from gauss_newton import GaussNewton
import numpy

g = GaussNewton([[0, 1],[1, 8],[2, 17],[3, 32],[4, 67], [5, 94], [6, 121], [7, 163], [8, 194], [9, 245], [10, 290]])

print(g.Gauss_Newton([3, 2, 3]))

