import gtrends_data
from gauss_newton import GaussNewton
# This will return a list
covidlist = gtrends_data.get("Coronavirus")
print(len(covidlist))
print(covidlist)

data = []
w = 0
for i in covidlist:
    data.append([w, int(i)])
    w+=1

print(data)

gn = GaussNewton(data)

n = 10
beta = [1, 1, 1, 1, 1, 1, 1]
for i in range(0,n):
    print(gn.gauss_newton(beta))
    beta = gn.gauss_newton(beta)