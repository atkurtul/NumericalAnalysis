import numpy as np
import matplotlib.pyplot as plt

def taylor(x, a, n):
	d = [lambda x: np.sin(x),
		lambda x: np.cos(x),
		lambda x: -np.sin(x),
		lambda x: -np.cos(x)]
	re = 0
	for i in range(n):
		re += d[i%4](2 * a) * ((x - a) * 2) ** i  / np.math.factorial(i)
	return re

a=np.pi/4
x = np.linspace(a-15.0, a+15.0, num=1000)

measured = lambda x: taylor(x, a=np.pi/4, n=5)
real = lambda x: np.sin(2*x)
diff = lambda x: abs(real(x) - measured(x))
rela = lambda x: abs(diff(x) / measured(x))
percent = lambda x: rela(x) * 100

plt.plot(x, real(x), label="sin2x curve")
plt.plot(x, measured(x), label=f"taylor series approx. at π/4")
plt.plot(x, diff(x), label=f"abs err")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.tight_layout()
plt.axis([-5+a, a+5, -5, 5])
plt.savefig("taylor")
plt.subplots(1,1)
x = np.linspace(a, a+15.0, num=1000)
plt.plot(x, rela(x), label=f"relative err")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.tight_layout()
plt.axis([a, a+5, 0, 40])
plt.savefig("err")
plt.show()
