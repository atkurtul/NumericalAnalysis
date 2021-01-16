import math


def interpolate(y0, y1, h):
  return (y1-y0)/h


def lr_diff(data, h):
  return list(map(lambda y0, y1: interpolate(y0, y1, h), data[:-1], data[1:]))


def center_diff(data, h):
  return [interpolate(data[i-1], data[i+1], 2*h) for i in range(len(data) - 2)]
    

# data=[(2.36, 0.85866),(2.37, 0.86289),(2.38, 0.86710),(2.39, 0.87129)]
data=[0.85866, 0.86289, 0.86710, 0.87129]


o1 = lr_diff(data, 0.1)
o2 = lr_diff(o1, 0.1)
central = center_diff(data, 0.1)


print("FD => f'(2.38) ≈",  o1[-1])
print("BD => f'(2.38) ≈",  o1[-2])
print("CD => f'(2.38) ≈", central[-1])
print("BD => f''(2.38) ≈", o2[-1])



print("2nd order derivative cannot be approximated with forward amd central difference from given data")


# f'(x) = (f(x+h) - f(x))/h - f''(x)/2 + o(h^2)

# f''(x) = (f'(x+h) - f'(x))/h - f'''(x)/2 + o(h^2)