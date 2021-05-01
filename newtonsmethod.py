
class NewtonsMethod:

    def __init__(self, coeff_vec):
        self.coeff = coeff_vec

    def set_coeff(self, coeff_vec):
        self.coeff = coeff_vec

    def eval_poly(self, x):

        x_ans = 0

        n = 0

        while n < len(self.coeff):

            x_ans += (self.coeff[n] * (x**(len(self.coeff) - n - 1)))

            n += 1

        return x_ans

    def eval_derivative(self, x):

        x_ans = 0

        n = 0

        while n < len(self.coeff)-1:

            x_ans += x_ans + (self.coeff[n] * (len(self.coeff) - n - 1) * (x**(len(self.coeff) - n - 2)))

            n += 1

        return x_ans

    def eval_newton(self, x):
        return x - (self.eval_poly(x)/self.eval_derivative(x))

    def eval_ntimes(self, n, x):

        xnew = x

        for i in range(0,n):
            xnew = self.eval_newton(xnew)

        return xnew

    def to_string(self):

        poly = ""

        for i in range(0,len(self.coeff)):
            poly += str(self.coeff[i]) + "x^" + str(len(self.coeff) - 1 - i) + " + "

        poly = poly[:len(poly)-3]

        return "Current polynomial being used: " + poly














