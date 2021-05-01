
class NewtonsMethod:

    def __init__(self, coeff_vec):
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
        return x - (self.eval_poly(x)/self.eval_derivative(x));















