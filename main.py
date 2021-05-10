import gtrends_data
from gauss_newton import GaussNewton
import matplotlib.pyplot as plt

# This will return a list
covid_list = gtrends_data.get("Coronavirus")
print(len(covid_list))
print(covid_list)

data = []
for index in range(len(covid_list) - 1):
    data.append([index, covid_list[index]])

print(data)

gn = GaussNewton(data)

n = 10
beta = [1, 1, 1, 1, 1, 1, 1]
for i in range(0, n):
    print(gn.gauss_newton(beta))
    beta = gn.gauss_newton(beta)

plt.plot(covid_list)
plt.show()
