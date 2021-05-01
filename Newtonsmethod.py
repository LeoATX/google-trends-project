

class NewtonsMethod:

    def eval_poly(self, x):
        return (x*x) - 2

    def eval_derivative(self, x):
        return 2*x

    def eval_newton(self, x):
        return x - (self.eval_poly(x)/self.eval_derivative(x))















