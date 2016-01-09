import numpy as np
import numpy.linalg as la
import scipy.stats as sp
import matplotlib.pyplot as plt
from io import StringIO
from collections import OrderedDict

from data import get_prices, get_nutrition

prices = get_prices()
nutrition = get_nutrition()

data = {}
for k, v in prices.items():
	if k in nutrition:
		data[k] = {'price': v, 'calories': nutrition[k]}

points = []
for key, value in data.items():
	points.append((value['price'], value['calories']))
points = np.array(points)

def f(x):
	A = np.zeros((points.shape))
	A[:, 0] = 1
	A[:, 1] = points[:, 0]
	b = points[:, 1]
	coeff = la.lstsq(A, b)[0]
	return coeff[0] + coeff[1] * x

plt.axis([0.99, 4.80, 0, 810])
plt.xlabel("Price ($)")
plt.ylabel("Calories")
plt.title("McDonald's Calories vs. Price -- " + str(sp.pearsonr(points[:, 0], points[:, 1])[0]))
plt.plot(points[:, 0], points[:, 1], 'bo')
plt.plot(points[:, 0], f(points[:, 0]))
plt.savefig("Output.png")
plt.show()