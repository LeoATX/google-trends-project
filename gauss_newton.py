import numpy
from newtonsmethod import NewtonsMethod

class GaussNewton:

    def __init__(self, table):
        self.dataset = table

    def vector_addition(self, v1, v2):
        sum = []
        for i in range(0, len(v1)):
            sum.append(v1[i] + v2[i])

        return sum

    def jacobian(self, n):
        jac = []

        for i in range(0, len(self.dataset)):
            new_vec = []
            for j in range(0, n + 1):
                new_vec.append(self.dataset[i][0] ** j)

            jac.append(new_vec)

        return jac

    def find_residuals(self, coeff):
        res = []
        nm = NewtonsMethod(coeff)

        for i in range(0, len(self.dataset)):
            r = self.dataset[i][1] - nm.poly_eval(self.dataset[i][0])
            res.append(r)

        return res

    def Gauss_Newton(self, n):
        coeff_guess = []

        for i in range(0,n):
            coeff_guess.append(1)

        new_coeff = []

        return new_coeff






