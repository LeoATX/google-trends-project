class GaussNewton:

    def __init__(self, table):
        self.dataset = table

    def jacobian(self, n):
        j = []

        for i in range(0, len(self.dataset)):
            new_vec = []
            for j in range(0, n + 1):
                new_vec.append(self.dataset[i][0] ** j)

            j.append(new_vec)

        return j

