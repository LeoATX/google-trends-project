import numpy
from newtonsmethod import NewtonsMethod


class GaussNewton:

    def __init__(self, table):
        self.dataset = table

    def jacobian(self, n):
        jac = []

        for i in range(0, len(self.dataset)):
            new_vec = []
            for j in range(0, n):
                new_vec.append(self.dataset[i][0] ** j)

            jac.append(new_vec)

        jac = numpy.array(jac)

        return jac

    def find_residuals(self, coeff):
        res = []
        nm = NewtonsMethod(coeff)

        for i in range(0, len(self.dataset)):
            r = self.dataset[i][1] - nm.eval_poly(self.dataset[i][0])
            res.append(r)

        res = numpy.array(res)

        return res

    def gauss_newton(self, guess):

        n = len(guess)

        r = self.find_residuals(guess)  # residuals

        guess = numpy.array(guess)

        jac = self.jacobian(n)  # Jacobian

        jt = jac.transpose()  # transpose of Jacobian

        inv = numpy.linalg.inv(numpy.matmul(jt, jac))  # pseudoinverse

        mj = numpy.matmul(inv, jt)

        delta = numpy.matmul(mj, r)  # change in beta

        new_coeff = numpy.add(guess, delta)

        return new_coeff
